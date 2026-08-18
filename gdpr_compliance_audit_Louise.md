# GDPR Compliance Audit --- Previously On: Love Is Blind

**Project 3:** Autonomous Research and Report Generation Agent\
**Author:** Louise Plessis\
**Audit type:** First-pass GDPR compliance assessment\
**Date:** 18 August 2026

> **Scope note:** This assessment is based on the Project 3 prototype
> and its current architecture. Where production configuration, vendor
> contracts, retention settings, hosting region, or exact API payloads
> are not documented, the assessment marks them as **TBD --- legal /
> technical review** rather than assuming compliance.

------------------------------------------------------------------------

# Data Processing Brief

*Previously On: Love Is Blind* is an AI-powered companion that creates
spoiler-aware recaps for viewers of *Love Is Blind*. A viewer selects
the edition, season, and last episode watched. The system retrieves show
information and public online material, including episode/cast metadata,
web sources, and YouTube comments used to represent fan reactions. It
then retrieves and synthesises relevant information into a generated
recap while trying to exclude events from episodes beyond the viewer's
selected cutoff.

The viewer inputs used for the core recap are mainly **edition, season,
episode number, and the request itself**. These are not necessarily
personal data in isolation. However, the system also processes public
content written by or about identifiable people. YouTube comments may
include usernames/channel identifiers, comment text, opinions, and other
information voluntarily disclosed by commenters. Web sources and
entertainment metadata contain names and information about identifiable
contestants and other public figures. Free-text public material could
also contain special-category information, even though the system is not
designed to infer or profile such attributes.

The purposes are separate. Show metadata and public web material are
used to establish factual context for the recap. YouTube comments are
used to identify and summarise audience reactions. Retrieved material is
also used as context for the generative model so that the final response
is grounded and spoiler-aware.

The processing stack includes the Project 3 application plus third-party
services used for search, metadata, model inference/embeddings, and
vector retrieval. The prototype uses services including OpenAI,
Pinecone, Tavily, YouTube Data API, TMDB and OMDb. The exact personal
data sent to each vendor, the configured storage region, vendor
retention, and whether European data-residency options are enabled are
not fully documented in the prototype. These points therefore require
verification before production deployment.

The system does **not** make decisions with legal or similarly
significant effects on viewers, commenters, or contestants. It generates
entertainment content: recaps, summaries, participant information, and
aggregated fan reactions. There is no human review before a recap is
shown to the viewer; instead, the system uses automated retrieval
constraints and a spoiler-check step.

**Conclusion:** personal data is involved. The main GDPR exposure comes
from repurposing publicly available third-party content---especially
YouTube comments---and passing or storing that material across an AI/RAG
vendor stack.

------------------------------------------------------------------------

# Phase 1 --- Personal Data Inventory

  -----------------------------------------------------------------------------------------------------
  Data category        Source                     Purpose(s)        Retention period    Crosses EEA
                                                                                        border?
  -------------------- -------------------------- ----------------- ------------------- ---------------
  Viewer request and   Directly from viewer       Generate a        Not formally        **TBD** ---
  viewing progress                                relevant,         defined in          depends on
  (edition, season,                               spoiler-bounded   prototype           API/vendor
  episode; potentially                            recap                                 configuration
  free-text request)                                                                    

  Contestant names and TMDB, OMDb, episode        Identify          Not formally        **TBD**
  public               metadata, public web       participants and  defined; may enter  
  biographical/show    sources                    provide factual   retrieval/index     
  information                                     recap context     pipeline            

  Public web text      Tavily-discovered/public   Research and      Not formally        **TBD**
  about identifiable   sources                    factual grounding defined             
  contestants/people                                                                    

  YouTube comment text YouTube Data API           Generate          Not formally        **TBD**
                                                  aggregated "fan   defined; may be     
                                                  reactions" and    processed/indexed   
                                                  audience themes                       

  YouTube              YouTube Data API           Not necessary for Not formally        **TBD**
  username/channel                                the core          defined             
  identifier or other                             fan-reaction                          
  comment metadata, if                            feature                               
  retrieved                                                                             

  Embeddings / vector  Generated from source      Semantic          Not formally        **TBD**
  representations      material and               retrieval for     defined             
  derived from         stored/retrieved through   recap generation                      
  retrieved content    vector infrastructure                                            

  Generated recap      Generated by the system    Deliver           Not formally        **TBD**
  containing                                      entertainment     defined             
  information about                               recap to viewer                       
  contestants and                                                                       
  summarised audience                                                                   
  reactions                                                                             
  -----------------------------------------------------------------------------------------------------

## Purpose-limitation flag

The clearest issue is **YouTube comments**. Commenters originally posted
their comments to participate on YouTube, not specifically to have them
collected by an independent AI product, embedded/indexed, and
synthesised into a separate entertainment service.

Public availability does not by itself remove GDPR obligations. Before
production use, the controller should document whether this secondary
use is compatible with the original context or establish an appropriate
lawful basis and provide the required transparency.

The current product also appears not to need commenter usernames or
channel identifiers to produce an aggregated fan-reaction feature. Those
fields should therefore be excluded as early as technically possible.

------------------------------------------------------------------------

# Phase 2 --- Role Map

Because this is an individual prototype rather than a deployed client
system, the role map below describes the likely production arrangement.

  -------------------------------------------------------------------------------
  Entity            Likely GDPR role        Processing activity DPA / transfer
                                                                status
  ----------------- ----------------------- ------------------- -----------------
  Future operator   **Controller**          Determines why and  Must establish
  of *Previously                            how viewer inputs   controller
  On*                                       and third-party     documentation,
                                            public content are  privacy notice,
                                            processed to create retention
                                            recaps              schedule, ROPA
                                                                and vendor
                                                                contracts

  Louise /          **Processor if building Builds and operates **TBD --- legal
  development team  solely on a client's    the                 review** based on
                    documented              prototype/system    production
                    instructions;                               relationship
                    controller if                               
                    independently deciding                      
                    product                                     
                    purposes/essential                          
                    means**                                     

  OpenAI API        Likely **processor**    Model inference     Production
                    for customer data where and/or embeddings   operator should
                    contracted under                            execute/verify
                    applicable API business                     DPA and transfer
                    terms/DPA                                   configuration.
                                                                OpenAI's current
                                                                DPA provides
                                                                SCC/adequacy
                                                                mechanisms for
                                                                relevant EEA
                                                                transfers;
                                                                European API data
                                                                residency is
                                                                available to
                                                                eligible
                                                                customers

  Pinecone          Likely **processor** if Vector storage and  **TBD** ---
                    storing vectors/content semantic retrieval  verify DPA,
                    on controller                               region,
                    instructions                                subprocessors,
                                                                retention and
                                                                deletion controls

  Tavily            Likely                  Search and          **TBD** ---
                    **processor/vendor**,   extraction          verify
                    depending on exact                          contract/DPA,
                    service and data flow                       logging,
                                                                retention,
                                                                subprocessors and
                                                                transfer
                                                                mechanism

  Google / YouTube  Generally an            Supplies public     **TBD --- legal
                    **independent           comments/metadata   review**; also
                    controller** for the    via API             verify YouTube
                    YouTube service; exact                      API terms and
                    relationship for                            permitted
                    API-derived data                            storage/use
                    requires review                             

  TMDB / OMDb and   Usually independent     Supply              Verify applicable
  source websites   source/service          entertainment       API terms and
                    operators rather than   metadata/public     whether personal
                    processors acting       source information  data is sent
                    solely on this                              onward
                    product's instructions                      
  -------------------------------------------------------------------------------

### International transfers

The prototype does not document enough configuration to conclude that
all processing remains in the EEA. Therefore the correct audit status is
**TBD** rather than "yes" or "no."

For OpenAI specifically, its current DPA states that EEA/Swiss data
transferred outside the EEA/Switzerland is protected through SCCs or an
applicable adequacy decision. OpenAI also offers European API data
residency to eligible customers. A production audit would still need to
verify the actual account/project configuration rather than assuming the
option is enabled.

------------------------------------------------------------------------

# Phase 3 --- Lawful Basis Assessment

  --------------------------------------------------------------------------------------
  Purpose               Proposed lawful   One-line justification       Legal review?
                        basis                                          
  --------------------- ----------------- ---------------------------- -----------------
  Process               **Contract ---    The service cannot generate  **Yes** ---
  viewer-selected       Art. 6(1)(b)**,   the requested                confirm
  show/season/episode   where processing  spoiler-bounded recap        applicability to
  to answer the         is objectively    without knowing what content actual product
  viewer's request      necessary to      the viewer asked for         relationship and
                        provide the                                    free-text
                        requested recap                                telemetry
                        service                                        

  Process public        **Legitimate      The operator has a           **Yes --- LIA
  contestant/show       interests ---     legitimate interest in       required**
  information for       Art. 6(1)(f)**    producing an informative     
  factual recap                           entertainment recap from     
                                          relevant public information, 
                                          subject to necessity and     
                                          balancing                    

  Process public web    **Legitimate      Retrieval of relevant public **Yes --- LIA
  articles/posts for    interests ---     material supports accuracy   required**
  grounding             Art. 6(1)(f)**    and grounding, but           
                                          collection must be limited   
                                          to what is necessary         

  Process YouTube       **TBD --- likely  Authentic audience reaction  **Yes --- legal
  comments to summarise legitimate        is a legitimate product      review required**
  fan reaction          interests if LIA  purpose, but secondary use   
                        succeeds**        of identifiable public       
                                          comments creates a           
                                          meaningful                   
                                          privacy/purpose-limitation   
                                          issue                        

  Process commenter     **No clear        The fan-reaction feature can **Yes ---
  usernames/channel IDs necessity         likely operate without       preferred
                        identified**      retaining identifiers        remediation is
                                                                       not to
                                                                       process/store
                                                                       them**

  Generate/store        Follows the       Embeddings are a technical   **Yes**
  embeddings derived    lawful basis of   means, not a new lawful      
  from personal data    the underlying    basis, and may remain        
                        processing        personal data where          
                        purpose; separate linkability/identification   
                        necessity         risk persists                
                        assessment                                     
                        required                                       
  --------------------------------------------------------------------------------------

## Legitimate Interests Assessment --- public web and contestant information

### 1. Purpose test --- is the interest legitimate?

**Likely yes.** The concrete interest is to provide viewers with
accurate, useful, source-grounded entertainment recaps.

### 2. Necessity test --- is the processing necessary?

**Partially.** Processing relevant public information is useful for the
service, but the system should retrieve only the content needed for the
selected season/episode and should avoid unnecessary identifiers or
unrelated personal information.

### 3. Balancing test --- do the individual's interests override?

For professional/public show information about contestants, the balance
may favour the product where the information is already deliberately
public and the use is proportionate. However, this cannot be assumed for
every source or every piece of information.

**Result: plausible legitimate interest, but document a formal LIA
before production.**

## Legitimate Interests Assessment --- YouTube fan reactions

### 1. Purpose test

**Likely yes.** Summarising authentic audience reaction is a legitimate
product objective.

### 2. Necessity test

**Only if minimised.** The product needs comment content to identify
themes, but it does not appear to need commenter identity. A less
intrusive architecture can strip usernames/channel IDs before LLM or
vector processing and use short-lived comment text.

### 3. Balancing test

**Uncertain.** Commenters may reasonably expect public visibility on
YouTube, but may not expect their contribution to be copied, embedded,
stored and repurposed in an unrelated AI product. Scale, retention,
quoting, identifiability and the nature of the comments materially
affect the balance.

**Result: TBD --- legal review.** If legitimate interests is retained as
the basis, complete and document the LIA before production.

------------------------------------------------------------------------

# Phase 4 --- Risk and Rights Analysis

## Special-category data --- Article 9

The system is **not designed to collect or infer special-category
data**, but public comments and web sources could contain references to
health, sexuality, political or religious views, ethnicity or other
Article 9 information about commenters or contestants. The current
architecture does not appear to require those attributes for the
fan-reaction or recap purpose.

The production design should therefore filter or avoid extracting
special-category information unless genuinely necessary. If the product
intentionally begins using such data, an Article 6 lawful basis alone
would not be sufficient: a valid Article 9 condition would also be
required. **Current conclusion: incidental presence is possible;
intentional processing should be excluded and flagged for legal
review.**

## Automated decision-making --- Article 22

**Article 22 is not triggered on the current intended use.** The system
generates entertainment content and does not make a decision producing
legal or similarly significant effects on viewers, commenters or
contestants.

The automated spoiler checker can change whether a draft is regenerated,
but that is a content-quality workflow rather than a consequential
decision about a person.

## DPIA trigger

Applying the lab's EDPB criteria:

-   **Evaluation/scoring of people:** not the intended purpose, although
    summarising sentiment about contestants can involve evaluative
    statements.
-   **Automated decision-making with significant effects:** no.
-   **Systematic monitoring:** not of the viewer; repeated collection of
    public comments should still be reviewed if scaled.
-   **Sensitive/highly personal data:** potentially incidental in
    free-text public content, not intentionally targeted.
-   **Large-scale processing:** prototype: no; production scale:
    **TBD**.
-   **Matching/combining datasets:** **yes** --- the system combines
    metadata, web sources and YouTube material.
-   **Vulnerable data subjects:** not intentionally targeted; minors
    could theoretically appear in public data, so **TBD** at scale.
-   **Innovative technology:** **yes** --- autonomous
    research/RAG/generative AI workflow.
-   **Processing that prevents rights/service/contract:** no.

At prototype scale, a mandatory DPIA is **not clearly established**.
However, two criteria---innovative technology and combining
datasets---are plausibly present, and production scale could add further
criteria. Because EDPB guidance says processing meeting two criteria
will in most cases warrant a DPIA assessment, the prudent recommendation
is to perform a **DPIA screening before production** and conduct a full
DPIA if the scaled design is likely to create high risk.

## Data-subject rights friction

**Access (Art. 15): Partial/Gap.** The prototype does not maintain a
documented mechanism for locating all material associated with a
particular commenter across source text, vectors and generated outputs.
Responding to an access request could therefore be difficult.

**Erasure (Art. 17): Gap.** If a YouTube comment is deleted at source,
the prototype does not document propagation of that deletion into cached
text, embeddings/vector storage or previously generated material.
Production needs traceable source IDs and deletion propagation or short
retention.

**Objection (Art. 21): Gap.** If legitimate interests is used for public
comments, individuals can have a right to object. There is currently no
documented intake and suppression mechanism to prevent re-ingestion
after a valid objection.

**Information/transparency (Arts. 13--14): Gap/TBD.** The hardest issue
is Article 14 because data is obtained from third-party public sources
rather than directly from commenters. Legal review should determine the
applicable transparency approach and whether any Article 14 exemption is
actually available; it should not be assumed.

------------------------------------------------------------------------

# Phase 5 --- Law Stacking Check

-   **AI Act:** First-pass classification is **limited risk /
    transparency**, not high-risk. The AI Act adds AI-specific
    transparency requirements for direct AI interaction/generative
    output that are distinct from GDPR's personal-data transparency
    duties.
-   **ePrivacy:** The core backend architecture does not inherently
    require cookies or tracking pixels. If the production web app uses
    non-essential analytics, advertising cookies, local device
    identifiers, or similar tracking, ePrivacy consent requirements must
    be assessed before deployment. **Current status: TBD based on
    frontend analytics configuration.**
-   **Data Act:** **N/A on the current design.** The product does not
    rely on connected-product/IoT data. Cloud service contractual
    switching provisions could become relevant at organisational level,
    but they are not central to this prototype's data flow.

------------------------------------------------------------------------

# Phase 6 --- Compliance Memo

**To:** Data Protection Officer / Legal Counsel\
**From:** Louise Plessis, AI Product Consultant\
**Subject:** First-pass GDPR assessment --- *Previously On: Love Is
Blind*

### Bottom line: PROCEED WITH CONDITIONS

The prototype can continue as a product concept, but I would not move
the current data pipeline directly into production because the lawful
basis, minimisation, retention, vendor-transfer configuration and
data-subject-rights workflow for public YouTube comments are not yet
documented.

The core viewer experience is comparatively low risk: users provide a
show edition, season and episode cutoff and receive an entertainment
recap. The material GDPR exposure comes from the research layer. The
system collects public content written by or about identifiable people,
uses YouTube comments to create fan-reaction summaries, may transform
source material into embeddings, and sends data through third-party
AI/search/storage services. Public availability does not remove this
processing from GDPR.

I recommend three actions, in this order.

**1. Redesign the fan-reaction pipeline around data minimisation.** Do
not retain commenter usernames/channel identifiers unless a documented
need emerges. Strip identifiers before model/vector processing where
technically possible, restrict retrieval to comments required for the
current request, define a short retention period, and retain source
references sufficient to propagate deletion or suppression.

**2. Establish the legal and vendor basis before production.** Complete
an LIA for public-source and YouTube-comment processing, with the
YouTube use marked **TBD --- legal review** until the balancing test and
API terms are confirmed. Map every processor/subprocessor, execute or
verify DPAs, document the actual hosting regions, and confirm the
transfer mechanism for any EEA data processed outside the EEA. OpenAI
offers a DPA and European API data-residency options, but the production
configuration must be verified rather than assumed.

**3. Build accountability and rights handling into the architecture.**
Create a privacy notice, retention schedule, ROPA, DPIA screening, and
workflows for access, erasure and objection. Source IDs should make it
possible to locate and delete derived vectors/content when required.

Residual risks remain even after these controls: public free text can
contain unexpected sensitive information; lawful-basis balancing for
third-party comments is context-dependent; and vendor/subprocessor or
transfer configurations may change.

This memo is a **first-pass product compliance assessment only**. It is
not a legal opinion, DPIA, conformity assessment, or certification.
Legal counsel/DPO review is required before relying on it for production
compliance decisions.

------------------------------------------------------------------------

# Accountability Test

**Could I demonstrate GDPR compliance to a regulator using only the
project's current documentation?**

**No.** The prototype demonstrates the product architecture, but it does
not yet contain the governance evidence needed to demonstrate GDPR
accountability.

  -----------------------------------------------------------------------
  Documentation / evidence            Current status
  ----------------------------------- -----------------------------------
  Personal data inventory             **Created in this audit**

  Controller/processor role map       **Created in this audit; production
                                      roles need confirmation**

  Record of Processing Activities     **Missing**
  (ROPA)                              

  Privacy notice covering viewer and  **Missing**
  third-party-source processing       

  Formal LIA for public-source        **Missing**
  processing                          

  Formal LIA / legal determination    **Missing**
  for YouTube comments                

  DPIA screening                      **Created at first-pass level here;
                                      formal screening missing**

  Full DPIA                           **Not currently established as
                                      mandatory; reassess before
                                      production**

  DPA register for processors         **Missing / not documented in
                                      repo**

  International transfer assessment   **Missing / configuration not
  and SCC/adequacy record             documented**

  Retention schedule                  **Missing**

  Automated deletion / anonymisation  **Missing**
  evidence                            

  Data-subject access / erasure /     **Missing**
  objection procedure                 

  Incident-response / breach          **Missing**
  procedure                           

  Security/access-control             **Missing**
  documentation                       
  -----------------------------------------------------------------------

## Legal-review preparation: YouTube comments

Before asking counsel to decide the lawful basis and Article 14
approach, I would prepare:

1.  The exact YouTube API fields retrieved.
2.  Whether usernames/channel IDs are currently sent to OpenAI or stored
    in Pinecone.
3.  Average and maximum number of comments processed per recap.
4.  Whether comments are quoted verbatim or only aggregated.
5.  Retention duration for raw comments, embeddings and generated
    outputs.
6.  How deleted YouTube comments are removed from local/vector storage.
7.  Whether a commenter can be identified from stored vectors or
    metadata.
8.  Expected production geography and user volume.
9.  The current YouTube API terms applicable to storage and reuse.
10. A proposed minimised architecture with identifiers removed before
    downstream AI processing.

------------------------------------------------------------------------

# Reinforce --- Design Decision I Would Change

The clearest design decision I would change in hindsight is the
treatment of YouTube comments.

I initially approached the feature as a product-quality question: **how
can the system capture authentic fan reactions rather than generating
generic commentary?** That led naturally to retrieving real comments and
feeding them into the research/RAG pipeline.

From a privacy-by-design perspective, I would reverse the order of that
reasoning. I would first define the minimum information required to
answer the product question. The feature needs the *substance of
audience reactions*, not the identity of individual commenters.

A production version should therefore remove usernames/channel
identifiers before downstream model or vector processing, use comments
transiently where possible, aggregate themes rather than reproduce
identifiable comments, and preserve only the source/deletion metadata
required for governance. This would reduce GDPR exposure without
reducing the user value of the feature.

------------------------------------------------------------------------

# Stretch --- Data Protection by Design Checklist

**Highest-risk processing activity:** collection and AI processing of
public YouTube comments for fan-reaction summaries.

  ------------------------------------------------------------------------
  Design principle         Current state           Pass / Fail / Unknown
  ------------------------ ----------------------- -----------------------
  Data minimisation: only  Comment content is      **Fail**
  minimum necessary data   relevant, but the       
  collected                prototype does not      
                           document stripping      
                           usernames/channel       
                           identifiers before      
                           downstream processing   

  Purpose binding: data    Product purpose is      **Fail**
  technically restricted   fan-reaction synthesis, 
  to stated purpose        but no technical        
                           purpose-control or      
                           documented reuse        
                           boundary exists         

  Access controls: access  Vendor/API access       **Unknown**
  limited to those who     exists, but repository  
  need it                  documentation does not  
                           establish production    
                           RBAC/access policy      

  Retention enforcement:   No documented automated **Fail**
  automated                retention/deletion      
  deletion/anonymisation   policy for raw comments 
                           or derived vectors      

  Subject-rights workflow: No documented lookup,   **Fail**
  access/erasure within    deletion-propagation or 
  one month                objection/suppression   
                           workflow                

  Incident response:       No GDPR                 **Fail**
  breach detection and     incident-response       
  72-hour notification     procedure is documented 
  process documented       in the prototype        
  ------------------------------------------------------------------------

### Changes required

Before production, the fan-reaction pipeline should strip unnecessary
identifiers at ingestion, define a short retention window, maintain
traceable source IDs for deletion, implement deletion across raw/vector
stores, create an objection/suppression mechanism, restrict operational
access, and document an incident-response process. Vendor contracts and
actual storage/processing regions should be verified alongside these
technical controls.

------------------------------------------------------------------------

# References used for this first-pass assessment

-   Regulation (EU) 2016/679 (GDPR), particularly Articles 5, 6, 9,
    13--14, 15, 17, 21, 22, 28, 30, 32--35 and 44--49.
-   EDPB / WP29 Guidelines on Data Protection Impact Assessment (WP248
    rev.01).
-   EDPB guidance on DPIA criteria and accountability.
-   OpenAI Data Processing Addendum and API data-residency
    documentation, checked August 2026.
