# Meeting Summary: AI Implementation in Telemedicine for Myanmar Healthcare

---

## Meeting Overview

- **Date:** Friday, March 13, 2026, 9:35 AM
- **Duration:** Not precisely specified; estimated 60–90 minutes based on depth of discussion
- **Context:** Multi-stakeholder planning call to discuss a joint grant proposal for deploying an AI-powered clinical assistant within Myanmar's telemedicine infrastructure, targeting a funding call with an **April 1st deadline**
- **Purpose:** Assess feasibility, define scope, align technical and operational capabilities, and begin structuring a grant proposal (up to $1M) for AI-assisted healthcare delivery in Myanmar

---

## Participants

| Name | Role | Affiliation |
|------|------|-------------|
| **Jimmy Daza** | Medical doctor, project coordinator/facilitator | Colombia-based; telemedicine experience in rural Latin America |
| **Dr. Juan Turnés (Tornes)** | Head of Gastroenterology & Pathology; AI research lead | Galicia, Spain |
| **Ernesto** | Technical/AI implementation specialist | Bestehealth (Spain-based) |
| **Dr. Laxas (Alexis)** | Founder & IT consultant, Telecyanmar | Myanmar (health informatics) |
| **Dr. Tarapi (Maa Therapy)** | Ministry of Health representative | Myanmar (NUG-affiliated) |
| **Dr. Ulrich (Koch)** | Academic partner, project liaison | Germany (Heidelberg/Frankfurt) |
| **Sandra** | Team member (joined from airport) | Spain-based |

**Key contributors:**
- **Jimmy** facilitated the meeting and guided proposal strategy
- **Dr. Turnés** provided deep technical insight on AI assistant architecture and validation
- **Dr. Laxas** detailed Telecyanmar's operational model and constraints
- **Dr. Tarapi** provided the Myanmar political/healthcare context and on-ground realities
- **Ernesto** addressed technical feasibility and timeline
- **Dr. Ulrich** offered strategic guidance and referenced prior proposal experience

---

## Main Topics Discussed

### 1. Myanmar Healthcare Crisis Context
- Post-2021 military coup: mass healthcare worker participation in civil disobedience movement
- Acute specialist shortage; providers operating in conflict zones under airstrike risk
- Healthcare delivered through telemedicine (Telecyanmar) and a medical diaspora Signal group providing 24/7 specialist consultation across time zones
- Township categorization system (3 tiers of stability) governs where interventions are feasible

### 2. Telecyanmar Platform Operations
- ~360 volunteers contributing 3–6 hours/week
- 10 primary care teams, 25 secondary/specialty teams
- Only one gastroenterologist (not a hepatologist), creating a critical gap
- 40–50 primary care doctors triage all new patients
- ~1,500–2,000 monthly patient consultations
- Entirely virtual: consultations via Facebook Messenger, prescriptions sent digitally
- Telemedicine support teams handle patient registration, simple medication questions, and escalation
- No AI system currently deployed; AI usage policy exists to prevent data leakage

### 3. Spanish AI Assistant Experience & Capabilities
- 2.5+ years building domain-specific AI assistants for healthcare
- Problem-first approach: identify clinical gaps, then build targeted AI tools
- RAG (Retrieval-Augmented Generation) architecture to minimize hallucinations
- Tools fed with **verified, locally relevant** clinical information—not generic LLM outputs
- Transparency features: references, source images, conversation tracking
- Validated in primary care settings in Spain
- Dr. Turnés authored the world's first WHO-recognized hepatitis C elimination plan (Galicia)
- Quality assessment framework: user feedback, accuracy tracking, conversation analysis

### 4. Technical Implementation Design
- **Initial phase:** Simple chat interface accessible via URL
- Information grounded in local clinical practice, drug availability, and workflows
- Multi-language support for Myanmar's diverse linguistic landscape
- Flexible deployment: local server hosting possible (e.g., Thailand) for data sovereignty
- No EMR integration required initially; paper-based records on-ground acknowledged
- **Development timeline:** ~3–4 months once source documentation is provided
- Two potential user groups:
  - Primary care physicians making specialist-level decisions
  - Telemedicine support staff/supervisors answering patient queries

### 5. Grant Proposal Strategy
- Targeting Gates Foundation, Wellness Foundation, and Novo Nordisk funding call
- Budget: up to **$1,000,000**; **80% to local Asian partners**, 20% to European partners
- One-year implementation period
- Application submitted **from Myanmar** (NUG-affiliated entity)
- Need to demonstrate patient impact numbers, healthcare professional reach, and operational feasibility
- Previous EKFS Foundation proposal (submitted last year, reached finalist stage) to be used as reference

### 6. Operational & Financial Logistics
- Telecyanmar: fully virtual, no physical office, NUG-registered NGO
- Funding flows through **Cambridge Global Health Partnerships (UK)** → **Spring Development Bank** (NUG online bank)
- Internal payments via KBZ Pay (mobile wallet, individual accounts to avoid military tracking)
- Supply chains for devices/medication: cross-border via Thailand, or via Yangon/India depending on conflict conditions
- Need to document these pathways for the proposal

### 7. Thailand Partnership Considerations
- Potential university partners: **Prince of Songkla University** (existing TB research collaboration), **Chiang Mai University**, **Chulalongkorn University**
- Political alignment is critical—some Thai institutions still engage with the military regime
- Thailand could serve as a base for training, coordination, and hardware supply
- Partner signatures needed for the proposal

---

## Goals & Objectives

**Short-term (proposal phase — next 2 weeks):**
- Finalize scope: number of facilities, healthcare professionals, and patients
- Secure Thailand-based academic partner commitments
- Draft and submit grant proposal by April 1st

**Medium-term (if funded — 1 year):**
- Deploy a RAG-based AI clinical assistant tailored to Myanmar's primary care context
- Train healthcare professionals on responsible AI use
- Validate tool accuracy and user satisfaction through structured quality assessment
- Generate evidence base for further funding

**Long-term:**
- Expand AI assistant to additional specialties and regions
- Potential EMR integration in later phases
- Build a scalable model for AI-assisted telemedicine in conflict/resource-limited settings

---

## Project Focus

- **Core idea:** A verified-information AI chat assistant supporting primary care physicians and telemedicine support staff in Myanmar, initially focused on gastroenterology/hepatology (hepatitis B/C, liver cirrhosis)
- **Scope:** Telecyanmar's online platform (~50 doctors, ~1,500–2,000 patients/month), potentially extending to on-ground facilities in liberated areas
- **Priorities:** Speed of deployment, clinical accuracy, local relevance, data privacy
- **Constraints:** No EMR on-ground, internet connectivity limitations in some townships, political complexity, drug import restrictions, virtual-only organizational structure
- **Assumptions:** Drug availability data and clinical guidelines can be sourced from local teams; local server hosting resolves data sovereignty concerns

---

## Key Decisions Made

| Decision | Reasoning |
|----------|-----------|
| Start with a **chat-based interface** (no EMR integration) | Lower barrier to entry; on-ground teams use paper records; EMR not needed for AI assistant functionality |
| Focus on **primary care physician support** as primary use case | Greatest benefit for less-experienced practitioners; aligns with existing patient flow |
| Include **telemedicine support staff/supervisor** use case | AI can replace or augment supervisor role for simple queries, reducing bottleneck |
| Target the **smaller grant track** (up to $1M) | Feasible scope; can generate evidence for future larger funding |
| Application to be submitted **from Myanmar** | Grant requirement for local lead |
| Use **previous EKFS proposal** as foundation | Saves time; financial estimates already exist; reached finalist stage |
| Next meeting set for **Thursday, March 20th, 9:30 AM Myanmar time** | Tight deadline requires weekly check-ins |

---

## Action Items

| Task | Responsible | Deadline |
|------|-------------|----------|
| Send Telecyanmar operational data (platform details, workflows, data systems) | Dr. Laxas (Alexis) | Within 1–2 days (~Mar 15) |
| Consult on-ground teams (Chin, Sagaing, etc.) for facility/patient/professional numbers | Dr. Laxas & Dr. Tarapi | By Thursday, Mar 19 |
| Identify and confirm Thailand university partner(s); obtain signatures | Dr. Tarapi & Dr. Laxas | By ~Mar 19–20 |
| Document supply chain and financial pathways for proposal | Telecyanmar team | Within 1–2 days |
| Circulate previous EKFS Foundation proposal and financial plan | Dr. Ulrich | ASAP |
| Review FAQ answers released by grant organizers (published Mar 13) | All | Immediately |
| Draft technical sections of the proposal | Ernesto, Dr. Turnés, Sandra | Ongoing through next week |
| Prepare training/education component description for proposal | Ernesto / Dr. Turnés | By Mar 20 meeting |
| Finalize proposal for April 1st submission | All | March 27–28 target for review |

---

## Discussion Insights

### Important Opinions & Perspectives
- **Dr. Turnés** emphasized that clinical practice guidelines from Europe are **not transferable**—local disease profiles, resources, and procedures must drive the AI's knowledge base
- **Ernesto** highlighted that **less-experienced practitioners benefit most** from AI support tools, citing stratified research findings; specialists benefit the least
- **Dr. Tarapi** stressed the importance of **political alignment** when selecting Thai partners—some institutions still engage with the military regime
- **Dr. Laxas** noted that the AI assistant could most valuably **replace the supervisor role** in the telemedicine support team workflow

### Risks & Challenges Identified
- **Tight deadline:** Only ~2.5 weeks to finalize a multi-partner, cross-border $1M proposal
- **Internet connectivity:** Not all townships can support digital tools; careful site selection needed
- **Drug availability:** Import restrictions mean medication availability is volatile and unpredictable
- **Banking complexity:** No traditional banking; reliance on NUG online banking and mobile wallets
- **Security concerns:** Military surveillance risk on financial flows and organizational activities
- **Partner alignment:** Thai academic institutions have mixed political positions on Myanmar's situation
- **Administrative capacity:** Telecyanmar lacks a physical office and traditional administrative infrastructure; may struggle as the administrative body for the grant

---

## How the Meeting Was Conducted

- **Structure:** Semi-structured; Jimmy facilitated, moving through introductions → context setting → technical discussion → operational logistics → next steps
- **Flow:** Each participant presented their domain expertise sequentially, followed by open Q&A
- **Communication style:** Professional but collegial; collaborative problem-solving tone with urgency driven by the deadline
- **Effectiveness:** Highly productive given the complexity—covered technical feasibility, operational constraints, financial logistics, and partnership considerations in a single session
- **Notable:** Participants joined from multiple time zones and locations (Spain, Germany, Myanmar, airport); some technical audio issues but managed effectively
- **Language:** Primarily English with occasional Spanish between Ernesto/Jimmy; multilingual comfort evident

---

## Next Steps

1. **Immediate (this week):**
   - Telecyanmar sends operational documentation and platform data
   - Dr. Ulrich shares EKFS proposal and financial plan
   - On-ground team consultations begin for participation commitments
   - All review the grant organizers' FAQ (released March 13)

2. **Next meeting: Thursday, March 20, 9:30 AM Myanmar time**
   - Review incoming data from Myanmar teams
   - Refine proposal scope and numbers
   - Address any outstanding questions

3. **Week of March 23–28:**
   - Finalize proposal text, budget, and partner signatures
   - Internal review by all parties

4. **April 1:** Grant submission deadline

