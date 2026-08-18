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
information and public online material, including episode and cast
metadata, web sources, and YouTube comments used to represent fan
reactions. It then retrieves and synthesises relevant information into a
generated recap while trying to exclude events from episodes beyond the
viewer's selected cutoff.

The viewer inputs used for the core recap are mainly **edition, season,
episode number, and the request itself**. These are not necessarily
personal data in isolation. However, the system also processes public
content written by or about identifiable people. YouTube comments may
include usernames or channel identifiers, comment text, opinions, and
other information voluntarily disclosed by commenters. Web sources and
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
services used for search, metadata, model inference or embeddings, and
vector retrieval. The prototype uses services including OpenAI,
Pinecone, Tavily, YouTube Data API, TMDB, and OMDb. The exact personal
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

**Conclusion:** Personal data is involved. The main GDPR exposure comes
from repurposing publicly available third-party content---especially
YouTube comments---and passing or storing that material across an AI/RAG
vendor stack.

------------------------------------------------------------------------

# Phase 1 --- Personal Data Inventory

  ----------------------------------------------------------------------------------------------------
  Data category       Source                     Purpose(s)        Retention period    Crosses EEA
                                                                                       border?
  ------------------- -------------------------- ----------------- ------------------- ---------------
  Viewer request and  Directly from viewer       Generate a        Not formally        **TBD** ---
  viewing progress:                              relevant,         defined in          depends on
  edition, season,                               spoiler-bounded   prototype           API/vendor
  episode,                                       recap                                 configuration
  potentially                                                                          
  free-text request                                                                    

  Contestant names    TMDB, OMDb, episode        Identify          Not formally        **TBD**
  and public          metadata, public web       participants and  defined; may enter  
  biographical/show   sources                    provide factual   retrieval/index     
  information                                    recap context     pipeline            

  Public web text     Tavily-discovered/public   Research and      Not formally        **TBD**
  about identifiable  sources                    factual grounding defined             
  contestants or                                                                       
  other people                                                                         

  YouTube comment     YouTube Data API           Generate          Not formally        **TBD**
  text                                           aggregated fan    defined; may be     
                                                 reactions and     processed/indexed   
                                                 audience themes                       

  YouTube             YouTube Data API           No necessary      Not formally        **TBD**
  username/channel                               purpose           defined             
  identifier or other                            identified for                        
  comment metadata,                              the core                              
  if retrieved                                   fan-reaction                          
                                                 feature                               

  Embeddings/vector   Generated from source      Semantic          Not formally        **TBD**
  representations     material and               retrieval for     defined             
  derived from        stored/retrieved through   recap generation                      
  retrieved content   vector infrastructure                                            

  Generated recap     Generated by the system    Deliver           Not formally        **TBD**
  containing                                     entertainment     defined             
  information about                              recap to viewer                       
  contestants and                                                                      
  summarised audience                                                                  
  reactions                                                                            
  ----------------------------------------------------------------------------------------------------

## Purpose-limitation flag

The clearest issue is **YouTube comments**. Commenters originally post
comments to participate on YouTube, not specifically to have them
collected by an independent AI product, potentially embedded or indexed,
and synthesised into a separate entertainment service.

Public availability does not by itself remove GDPR obligations. Before
production use, the controller should document whether this secondary
use is compatible with the original context or establish an appropriate
lawful basis and provide the required transparency.

The product also appears not to need commenter usernames or channel
identifiers to produce aggregated fan reactions. Those fields should
therefore be excluded as early as technically possible.

------------------------------------------------------------------------

# Phase 2 --- Role Map

The following is a first-pass role map for a potential production
version. GDPR roles depend on the **actual processing relationship**: in
particular, who determines the purposes and essential means of
processing.

  --------------------------------------------------------------------------------------
  Entity            GDPR role            Processing activity in  DPA / transfer status
                                         *Previously On*         
  ----------------- -------------------- ----------------------- -----------------------
  **Future operator **Controller**       Determines why viewer   Controller
  of *Previously                         inputs, public-source   documentation required;
  On***                                  information, and fan    Article 28 DPAs
                                         reactions are processed required with entities
                                         and determines the      that act as processors
                                         essential means of the  
                                         recap service           

  **Louise /        **Processor if       Develops, configures,   **TBD --- legal
  development       building/operating   and potentially         review** based on the
  team**            solely on a client's operates the            production relationship
                    documented           research/RAG pipeline   
                    instructions;                                
                    controller where                             
                    independently                                
                    determining purposes                         
                    and essential                                
                    means**                                      

  **OpenAI API**    **Likely             Processes selected      **TBD --- verify**
                    processor**,         retrieved material for  applicable DPA,
                    assuming API         model inference and/or  data-residency
                    processing is        embeddings              configuration,
                    performed on the                             subprocessors,
                    operator's                                   retention, and transfer
                    instructions under                           mechanism before
                    the applicable                               production
                    contractual terms                            

  **Pinecone**      **Likely             Stores and retrieves    **TBD --- verify** DPA,
                    processor**,         embeddings/vectorised   hosting region,
                    assuming vector      source material used by subprocessors,
                    infrastructure       the RAG pipeline        retention/deletion
                    processes data on                            settings, and transfer
                    the controller's                             mechanism
                    instructions                                 

  **Tavily**        **Likely processor   Searches and retrieves  **TBD --- verify**
                    where personal data  public web information  exact payloads,
                    in queries/content   used by the research    contractual role, DPA
                    is processed on the  agent                   where applicable,
                    operator's behalf;                           retention,
                    exact role requires                          subprocessors, and
                    confirmation**                               transfer mechanism

  **Google /        **Independent        Makes public comments   **No
  YouTube**         controller /         and associated metadata controller--processor
                    third-party data     available through the   DPA assumed for this
                    source for the       YouTube Data API;       source relationship.**
                    relevant YouTube     *Previously On*         Verify YouTube API
                    service data; not    independently selects   terms, permitted
                    assumed to be a      and repurposes some of  storage/reuse, and any
                    processor for        that data for           relevant transfer
                    *Previously On***    fan-reaction analysis   implications

  **TMDB**          **Independent        Supplies cast,          Not treated as a
                    third-party data     programme, and episode  processor by default;
                    source/service       metadata used as        verify API terms and
                    provider; exact GDPR factual context         whether personal data
                    role depends on the                          is transmitted beyond
                    actual data                                  requests for public
                    exchange**                                   metadata

  **OMDb**          **Independent        Supplies programme and  Not treated as a
                    third-party data     episode metadata used   processor by default;
                    source/service       as factual context      verify API terms and
                    provider; exact GDPR                         actual data exchanged
                    role depends on the                          
                    actual data                                  
                    exchange**                                   

  **Public source   **Independent        Public material is      No Article 28 DPA
  websites**        controllers of their retrieved and used as   merely because the
                    own websites/content research context        system retrieves public
                    and third-party data                         content; *Previously
                    sources; not                                 On* remains responsible
                    processors acting on                         for its own downstream
                    behalf of                                    collection and reuse
                    *Previously On***                            
  --------------------------------------------------------------------------------------

## Role-mapping rationale

The future operator of *Previously On* is the **controller** because it
determines the purposes of processing---providing spoiler-aware recaps
and fan-reaction summaries---and the essential means used to achieve
them.

A development team working solely on that operator's documented
instructions may act as a **processor**. If the development team
independently decides the product's purposes or essential processing
means, it may instead be a controller for those activities. The
production arrangement would therefore need legal confirmation.

OpenAI and Pinecone are treated as likely **processors only where they
process personal data on the operator's instructions**. By contrast,
YouTube, TMDB, OMDb, and public websites are primarily **third-party
data sources rather than processors acting on behalf of *Previously
On***. Their own GDPR roles, contractual terms, and the legality of the
downstream reuse still need to be assessed separately.

## International transfers

The prototype does not document enough configuration to conclude that
all processing remains in the EEA. The audit therefore records
international-transfer status as **TBD** rather than assuming either
EU-only or international processing.

Before production, the operator should document the actual hosting
location and transfer mechanism for every processor receiving personal
data. Where data leaves the EEA, the applicable mechanism---such as an
adequacy decision or Standard Contractual Clauses---must be identified
and documented.

------------------------------------------------------------------------

# Phase 3 --- Lawful Basis Assessment

  ---------------------------------------------------------------------------------------
  Purpose               Proposed lawful   One-line justification        Flag for legal
                        basis                                           review?
  --------------------- ----------------- ----------------------------- -----------------
  Process               **Contract ---    The system cannot generate    **Yes** ---
  viewer-selected       Art. 6(1)(b)**,   the requested spoiler-bounded confirm against
  show/season/episode   where objectively recap without knowing which   the actual
  to answer the         necessary to      content the viewer requested  product
  viewer's request      provide the                                     relationship and
                        requested service                               any additional
                                                                        telemetry

  Process public        **Legitimate      The operator has a legitimate **Yes --- LIA
  contestant/show       interests ---     interest in producing an      required**
  information for       Art. 6(1)(f)**    informative entertainment     
  factual recap                           recap from relevant public    
                                          information, subject to       
                                          necessity and balancing       

  Process public web    **Legitimate      Retrieval of relevant public  **Yes --- LIA
  material for          interests ---     material supports accuracy    required**
  grounding             Art. 6(1)(f)**    and grounding, but collection 
                                          should be limited to what is  
                                          necessary                     

  Process YouTube       **TBD ---         Authentic audience reaction   **Yes --- legal
  comments to summarise potentially       is a legitimate product       review required**
  fan reaction          legitimate        purpose, but secondary use of 
                        interests if the  identifiable public comments  
                        LIA succeeds**    creates privacy and           
                                          purpose-limitation concerns   

  Process commenter     **No clear        The fan-reaction feature can  **Yes ---
  usernames/channel     necessity         likely operate without        preferred
  identifiers           identified**      retaining commenter identity  remediation is
                                                                        not to
                                                                        process/store
                                                                        them**

  Generate/store        Follows the       Embeddings are a technical    **Yes**
  embeddings derived    lawful basis of   means, not a separate lawful  
  from personal data    the underlying    basis, and may remain         
                        processing        personal data depending on    
                        purpose; separate identifiability/linkability   
                        necessity                                       
                        assessment                                      
                        required                                        
  ---------------------------------------------------------------------------------------

## Legitimate Interests Assessment --- Public web and contestant information

### 1. Purpose test

**Likely yes.** The concrete interest is to provide viewers with
accurate, useful, source-grounded entertainment recaps.

### 2. Necessity test

**Partially.** Processing relevant public information supports the
service, but the system should retrieve only information necessary for
the selected season/episode and avoid unrelated or unnecessary personal
data.

### 3. Balancing test

For deliberately public professional/show information about contestants,
the balance may favour the product where the use is proportionate and
within reasonable expectations. This should not be assumed for every
source or every piece of information.

**Result:** Plausible legitimate interest, but a formal LIA should be
documented before production.

## Legitimate Interests Assessment --- YouTube fan reactions

### 1. Purpose test

**Likely yes.** Summarising authentic audience reaction is a legitimate
product objective.

### 2. Necessity test

**Only if minimised.** The product needs comment content to identify
themes but does not appear to need commenter identity. A less intrusive
architecture can remove usernames/channel identifiers before LLM or
vector processing and minimise retention of raw comments.

### 3. Balancing test

**Uncertain.** Commenters may reasonably expect public visibility on
YouTube, but may not expect their contributions to be collected,
embedded, stored, and repurposed by a separate AI product. Scale,
retention, quoting, identifiability, and the nature of the comments
materially affect the balance.

**Result: TBD --- legal review.** If legitimate interests is relied
upon, complete and document the LIA before production.

------------------------------------------------------------------------

# Phase 4 --- Risk and Rights Analysis

## Special-category data --- Article 9

The system is **not designed to collect or infer special-category
data**, but public comments and web sources could incidentally contain
information about health, sexuality, political or religious views,
ethnicity, or other Article 9 categories relating to commenters or
contestants.

The current product purpose does not require those attributes. A
production design should therefore avoid intentionally extracting or
using them and minimise incidental collection where possible. If the
product later intentionally processes special-category data, an Article
6 lawful basis would not be sufficient on its own; a valid Article 9
condition would also be required.

**Current conclusion:** Incidental presence is possible; intentional
processing is outside the intended scope and should trigger legal
review.

## Automated decision-making --- Article 22

**Article 22 is not triggered by the current intended use.** The system
generates entertainment content and does not make decisions producing
legal or similarly significant effects on viewers, commenters, or
contestants.

The automated spoiler checker can decide whether a draft is regenerated,
but this is a content-quality decision rather than a significant
decision about a person.

## DPIA trigger

Applying the EDPB criteria used in the lab:

-   **Evaluation/scoring of people:** not the intended purpose, although
    fan-reaction summaries can contain evaluative statements about
    contestants.
-   **Automated decision-making with significant effects:** no.
-   **Systematic monitoring:** not of the viewer; repeated collection of
    public comments should nevertheless be reassessed if scaled
    substantially.
-   **Sensitive/highly personal data:** potentially incidental in public
    free text, not intentionally targeted.
-   **Large-scale processing:** prototype: no; production: **TBD**.
-   **Matching/combining datasets:** **yes** --- the system combines
    metadata, web sources, and YouTube material.
-   **Data concerning vulnerable people:** not intentionally targeted;
    possible incidental inclusion means production scale should be
    reviewed.
-   **Innovative technology:** **yes** --- autonomous
    research/RAG/generative AI workflow.
-   **Processing preventing rights/service/contract:** no.

At prototype scale, a mandatory DPIA is **not clearly established**.
However, innovative technology and dataset combination are plausibly
present, and production scale could add further criteria. The
recommended action is therefore to conduct a **formal DPIA screening
before production** and perform a full DPIA if the final processing is
likely to result in high risk.

## Data-subject rights friction

### Access --- Article 15: Partial / Gap

The prototype does not document a mechanism for locating all material
associated with a particular person across source text, vectors, and
generated outputs. Responding efficiently to an access request could
therefore be difficult.

**Required improvement:** Maintain sufficient source/provenance
information to identify where relevant personal data has been processed
without unnecessarily retaining additional identifiers.

### Erasure --- Article 17: Gap

If a YouTube comment is deleted at source, the prototype does not
document propagation of that deletion into cached text,
embeddings/vector storage, or other retained copies.

**Required improvement:** Define retention and deletion rules and
maintain source references that allow deletion to propagate through
relevant stores.

### Objection --- Article 21: Gap

If legitimate interests is used for processing public comments,
individuals may have a right to object. There is currently no documented
process for receiving an objection and preventing the same data from
being re-ingested.

**Required improvement:** Create an objection/suppression workflow
appropriate to the production architecture.

### Information --- Articles 13--14: Gap / TBD

The difficult issue is Article 14 because personal data may be obtained
from public third-party sources rather than directly from the person.

**Required improvement:** Legal review should determine the appropriate
Article 14 transparency approach and whether any exemption applies. An
exemption should not be assumed simply because the information is
public.

------------------------------------------------------------------------

# Phase 5 --- Law Stacking Check

-   **AI Act cross-check:** First-pass classification is **limited risk
    / transparency**, not high-risk. The AI Act adds AI-specific
    transparency requirements for direct AI interaction and generated
    content that are distinct from GDPR's personal-data transparency
    duties.
-   **ePrivacy check:** The core backend architecture does not
    inherently require cookies or tracking pixels. If the production web
    app uses non-essential analytics, advertising cookies, local device
    identifiers, or similar tracking, the relevant ePrivacy consent
    requirements must be assessed. **Current status: TBD based on
    production frontend configuration.**
-   **Data Act check:** **N/A for the core use case.** The system does
    not use connected-product or IoT data.

------------------------------------------------------------------------

# Phase 6 --- Compliance Memo

**To:** Data Protection Officer / Legal Counsel\
**From:** Louise Plessis, AI Product Consultant\
**Subject:** First-pass GDPR assessment --- *Previously On: Love Is
Blind*

## Bottom line: PROCEED WITH CONDITIONS

The prototype can continue as a product concept, but I would not move
the current data pipeline directly into production because the lawful
basis, minimisation, retention, vendor relationships,
international-transfer configuration, and data-subject-rights workflow
for public YouTube comments are not yet documented.

The core viewer experience is comparatively low risk: viewers provide a
show edition, season, and episode cutoff and receive an entertainment
recap. The material GDPR exposure comes from the research layer. The
system collects public content written by or about identifiable people,
uses YouTube comments to create fan-reaction summaries, may transform
source material into embeddings, and processes data through third-party
AI, search, and storage services. Public availability does not remove
this processing from GDPR.

I recommend three actions, in this order.

**1. Redesign the fan-reaction pipeline around data minimisation.** Do
not retain commenter usernames or channel identifiers unless a
documented need emerges. Strip unnecessary identifiers before downstream
model/vector processing where technically possible, restrict retrieval
to comments required for the current purpose, define retention, and
maintain only the provenance needed for governance and deletion.

**2. Establish the legal and vendor basis before production.** Complete
an LIA for public-source processing, with the YouTube-comment use marked
**TBD --- legal review** until the balancing test and API terms are
confirmed. Map the exact GDPR role of each vendor, establish Article 28
DPAs where a vendor acts as processor, and document the actual hosting
regions and transfer mechanisms for personal data leaving the EEA.

**3. Build accountability and rights handling into the architecture.**
Create a privacy notice, retention schedule, ROPA, formal DPIA
screening, and workflows for access, erasure, and objection.
Source/provenance identifiers should make it possible to locate and
remove relevant retained data without collecting unnecessary identity
information.

Residual risks remain even after these controls: public free text can
contain unexpected sensitive information; the legitimate-interest
balancing test for third-party comments is context-dependent; and
vendor/subprocessor configurations may change over time.

This memo is a **first-pass product compliance assessment only**. It is
not a legal opinion, DPIA, certification, or final determination of
controller/processor roles. Legal counsel or DPO review is required
before relying on it for production compliance decisions.

------------------------------------------------------------------------

# Accountability Test

**Could I demonstrate compliance to a regulator using only the project's
current documentation?**

**No.** The prototype demonstrates the product architecture, but it does
not yet contain all governance evidence needed to demonstrate GDPR
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

  DPIA screening                      **First-pass analysis created here;
                                      formal screening missing**

  Full DPIA                           **Not currently established as
                                      mandatory; reassess before
                                      production**

  DPA register for actual processors  **Missing / not documented in
                                      repo**

  International-transfer assessment   **Missing / configuration not
  and SCC/adequacy record             documented**

  Retention schedule                  **Missing**

  Automated deletion/anonymisation    **Missing**
  evidence                            

  Data-subject                        **Missing**
  access/erasure/objection procedure  

  Incident-response/breach procedure  **Missing**

  Security/access-control             **Missing**
  documentation                       
  -----------------------------------------------------------------------

## Legal-review preparation --- YouTube comments

Before asking counsel to decide the lawful basis and Article 14
approach, I would prepare:

1.  The exact YouTube API fields retrieved.
2.  Whether usernames/channel IDs are sent to model or vector vendors.
3.  Average and maximum number of comments processed per recap.
4.  Whether comments are quoted verbatim or only aggregated.
5.  Retention duration for raw comments, embeddings, and generated
    outputs.
6.  How deleted source comments are removed from retained data.
7.  Whether stored vectors or metadata remain linkable to an individual.
8.  Expected production geography and user volume.
9.  Applicable YouTube API terms governing storage and reuse.
10. A proposed minimised architecture with unnecessary identifiers
    removed before downstream AI processing.

------------------------------------------------------------------------

# Reinforce --- Design Decision I Would Change

The clearest design decision I would change in hindsight is the
treatment of YouTube comments.

I initially approached the feature as a product-quality question: **How
can the system capture authentic fan reactions rather than generating
generic commentary?** That naturally led to retrieving real comments and
feeding them into the research/RAG pipeline.

From a privacy-by-design perspective, I would reverse the order of that
reasoning. I would first define the minimum information required to
answer the product question. The feature needs the **substance of
audience reactions**, not the identity of individual commenters.

A production version should therefore remove usernames/channel
identifiers before downstream model or vector processing, use comments
transiently where possible, aggregate themes rather than reproduce
identifiable comments, and preserve only the source/deletion metadata
genuinely required for governance. This would reduce GDPR exposure
without reducing the user value of the feature.

------------------------------------------------------------------------

# Stretch --- Data Protection by Design Checklist

**Highest-risk processing activity:** Collection and AI processing of
public YouTube comments for fan-reaction summaries.

  -----------------------------------------------------------------------
  Design principle        Current state of the    Pass / Fail / Unknown
                          system                  
  ----------------------- ----------------------- -----------------------
  **Data minimisation:**  Comment content is      **Fail**
  only the minimum        relevant, but the       
  necessary data is       prototype does not      
  collected               document removal of     
                          usernames/channel       
                          identifiers before      
                          downstream processing   

  **Purpose binding:**    Product purpose is      **Fail**
  data is technically     fan-reaction synthesis, 
  restricted to the       but no technical        
  stated purpose          purpose-control or      
                          documented reuse        
                          boundary exists         

  **Access controls:**    Vendor/API access       **Unknown**
  access is limited to    exists, but the         
  those who need it       prototype does not      
                          document production     
                          RBAC/access policy      

  **Retention             No documented automated **Fail**
  enforcement:**          retention/deletion      
  automated deletion or   policy for raw comments 
  anonymisation is in     or derived vectors      
  place                                           

  **Subject rights        No documented lookup,   **Fail**
  workflow:** system can  deletion-propagation,   
  support access or       or                      
  erasure within the      objection/suppression   
  required timeframe      workflow                

  **Incident response:**  No GDPR                 **Fail**
  breach detection and    incident-response       
  72-hour notification    procedure is documented 
  process is documented   in the prototype        
  -----------------------------------------------------------------------

## Changes required

Before production, the fan-reaction pipeline should:

-   strip unnecessary identifiers at ingestion;
-   define and enforce a retention window;
-   maintain sufficient provenance to support deletion without retaining
    unnecessary identity data;
-   propagate deletion through relevant raw/vector stores;
-   implement an objection/suppression mechanism where required;
-   restrict operational access;
-   document an incident-response process; and
-   verify vendor contracts and actual storage/processing regions.

------------------------------------------------------------------------

# Final Assessment

**Recommendation: Proceed with conditions.**

The current Project 3 prototype does not present a clear Article 22
automated-decision issue and is not intentionally designed to process
special-category data. Its main GDPR challenge is instead the
**secondary processing of public personal data---particularly YouTube
comments---inside an AI/RAG architecture**.

The highest-priority production changes are therefore:

1.  **Minimise the fan-reaction data before it enters the AI pipeline.**
2.  **Establish and document the lawful basis and vendor roles.**
3.  **Define retention, deletion, objection, and transparency
    processes.**
4.  **Verify international-transfer mechanisms and processor DPAs.**
5.  **Complete formal DPIA screening before scaling the system.**

The audit also shows a broader product lesson: using public data does
not mean privacy considerations disappear. Designing the minimum
necessary data flow before implementing retrieval and storage would have
reduced both compliance burden and architectural complexity.
