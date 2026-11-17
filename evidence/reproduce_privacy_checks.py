"""Reproduce audit evidence against an unchanged Model Intake Brief checkout.

Usage: python reproduce_privacy_checks.py --project PATH --out OUTPUT_DIRECTORY
Only synthetic content is used. HTTP and socket connections are blocked.
"""
import argparse
from collections import Counter
import contextlib
import io
import json
from pathlib import Path
import socket
import subprocess
import sys
from unittest.mock import patch

parser = argparse.ArgumentParser()
parser.add_argument('--project', type=Path, required=True)
parser.add_argument('--out', type=Path, required=True)
args = parser.parse_args()
sys.dont_write_bytecode = True
sys.path.insert(0, str(args.project.resolve() / 'src'))
args.out.mkdir(parents=True, exist_ok=True)

def blocked(*a, **kw):
    raise AssertionError('Network access is forbidden in this audit evidence run.')

with patch.object(socket.socket, 'connect', blocked), patch('requests.sessions.Session.request', blocked):
    from intake.graph import APP
    from intake.cli import main
    from intake.assessment import call_openai_assessment
    from intake.checklist import load_checklist

    payload = {'live_mode': False, 'provider': None, 'model': 'Qwen/Qwen3-8B'}
    result = APP.invoke(payload)
    report = result['report_markdown']
    (args.out / 'offline-qwen3-8b-report.md').write_text(report, encoding='utf-8')
    counts = dict(Counter(f['status'] for f in result['assessment']['findings']))
    assert counts == {'Not checked': 18}

    stdout, stderr = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
        invalid_exit = main(['run', '--model', 'not-a-valid-id'])
    assert invalid_exit == 2
    assert 'ORG/MODEL' in stderr.getvalue()

    synthetic_text = 'Example model documentation. Contact: Audit Example, audit.person@example.invalid.'
    sources = [{'name': 'Synthetic source', 'requested_url': 'https://example.invalid/model',
                'usable': True, 'http_status': 200, 'snippet': synthetic_text,
                'full_text': synthetic_text, 'metadata': {}}]
    captured = {}

    class FakeResponse:
        status_code = 200
        def raise_for_status(self):
            pass
        def json(self):
            return {'status': 'completed', 'output_text': '{"findings": []}', 'usage': {}}

    def intercept(url, **kwargs):
        captured['endpoint'] = url
        captured['body'] = kwargs['json']
        return FakeResponse()

    with patch('intake.assessment.requests.post', intercept):
        call_openai_assessment('synthetic-not-a-real-key', load_checklist(),
                               {'exact_model_id': 'ExampleOrg/ExampleModel'}, sources, 1)
    preserved = 'audit.person@example.invalid' in captured['body']['input']
    assert preserved
    assert captured['body']['store'] is False
    (args.out / 'synthetic-outbound-payload.json').write_text(
        json.dumps(captured, indent=2, ensure_ascii=False), encoding='utf-8')

commit = subprocess.check_output(['git', '-C', str(args.project), 'rev-parse', 'HEAD'], text=True).strip()
summary = {
    'audit_date': '2026-11-17', 'source_commit': commit,
    'python_version': sys.version.split()[0],
    'network_policy': 'HTTP requests and socket connections blocked; assessment POST intercepted locally.',
    'offline_run': {'input': payload, 'status_counts': counts, 'error': result.get('error'),
                    'output_file': 'offline-qwen3-8b-report.md'},
    'invalid_input': {'argv': ['run', '--model', 'not-a-valid-id'], 'exit_code': invalid_exit,
                      'stdout': stdout.getvalue(), 'stderr': stderr.getvalue()},
    'synthetic_privacy_probe': {'input_text': synthetic_text,
        'contact_preserved_in_outbound_prompt': preserved, 'store': captured['body']['store'],
        'actual_external_requests': 0,
        'limitation': 'Local payload inspection only; fake response is not an LLM assessment or a vendor retention test.'}
}
(args.out / 'privacy-check-results.json').write_text(json.dumps(summary, indent=2), encoding='utf-8')
print(json.dumps(summary, indent=2))
