'use strict';
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');

const read = p => JSON.parse(fs.readFileSync(p, 'utf8'));
const excerpt = read(path.join(__dirname, 'companyscope-workflow-evidence-excerpt.json'));
const fixture = read(process.argv[2] || path.join(__dirname, 'synthetic-data-flow-input.json'));
const state = {
  'Select Exact Entity': { registry_match: fixture.registry_match },
  'Tavily Search': fixture.search_response
};
const first = json => ({ first: () => ({ json }) });
// Replays trusted, pinned workflow code. The synthetic input is JSON data, not code.
function node(name, current) {
  const code = excerpt.code_nodes[name];
  assert.equal(typeof code, 'string');
  const output = new Function('$input', '$', code)(first(current), ref => {
    assert.ok(ref in state, 'Missing node stub: ' + ref);
    return first(state[ref]);
  });
  return state[name] = output[0].json;
}
const normalized = node('Normalize Input', fixture.form);
assert.equal(normalized.valid, true);
const query = node('Prepare Tavily Query', {body: fixture.registry_details});
const rag = node('Local RAG', query);
const evidence = node('Assemble Evidence', rag);
const prepared = node('Prepare OpenAI Input', evidence);

function body(expression, scope) {
  // n8n wraps a JavaScript expression with ={{ ... }}.
  assert.ok(expression.startsWith('={{') && expression.endsWith('}}'));
  return new Function('$json', 'return (' + expression.slice(3, -2) + ');')(scope);
}
const tavilyBody = JSON.parse(body(excerpt.tavily_http_body_expression, query));
const openaiBody = JSON.parse(body(excerpt.openai_http_body_expression, prepared));
const openaiEvidence = JSON.parse(openaiBody.input.find(item => item.role === 'user').content);
const dimensions = value => Object.fromEntries(Object.entries(fixture.markers)
  .map(([label, marker]) => [label, JSON.stringify(value).includes(marker)]));
const out = {
  source_commit: excerpt.source_commit,
  external_requests_made: 0,
  scope: 'Pinned code nodes and HTTP body expressions with synthetic upstream responses',
  exported_execution_settings: excerpt.execution_settings,
  normalized_input_keys: Object.keys(normalized),
  tavily: {
    query: tavilyBody.query,
    accepted_sources: evidence.tavily_accepted_count,
    rejected_reasons: evidence.tavily_rejected_reasons,
    markers_in_request: dimensions(tavilyBody)
  },
  openai: {
    endpoint: '/v1/responses',
    model: openaiBody.model,
    store: openaiBody.store,
    sources: [...openaiEvidence.registry_evidence, ...openaiEvidence.public_web_research].map(s => s.id),
    markers_in_user_evidence: dimensions(openaiEvidence)
  }
};
console.log(JSON.stringify(out, null, 2));
