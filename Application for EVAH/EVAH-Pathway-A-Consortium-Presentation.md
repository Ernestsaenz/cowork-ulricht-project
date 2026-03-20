# EVAH Pathway A — Consortium Strategy Presentation
### Improving Clinical Decision Support and Telemedicine for Underserved Populations in the Thailand–Myanmar Corridor

*Internal consortium working document — March 2026*
*Not for submission to funders*

---

## Slide 1: Why We Are Here

**Visual/Layout notes:** Clean title slide. Map showing Thailand–Myanmar border region with pins at Bangkok (Mahidol), Myanmar (Telekyanmar coverage area), Spain (IDARA), and Germany (Goethe University Frankfurt). EVAH logo + funder logos (Wellcome Trust, Gates Foundation, Novo Nordisk Foundation) at bottom.

**Speaker notes / Context:**

This presentation lays out our strategy for the EVAH Pathway A application — a USD 1,000,000 grant over 3–12 months, managed by J-PAL and APHRC. The deadline is **April 1, 2026**.

The central question we must answer for the funders: *Can an AI-enabled clinical decision support tool, already validated in Spain, be safely adapted and effectively deployed for frontline health workers serving underserved populations in the Thailand–Myanmar corridor?*

Our answer is yes — and we have the consortium, the technology, and the operational platform to prove it.

**Key framing decision:** Mahidol University (Thailand) is the lead applicant. The narrative is led by a Thai academic institution seeking to improve healthcare access for three populations: Myanmar refugees/migrants in Thailand, Myanmar citizens served by Telekyanmar telemedicine, and Thai border communities. This is a patient-centered, equity-driven story.

---

## Slide 2: The Problem — Healthcare Access in the Thailand–Myanmar Corridor

**Visual/Layout notes:** Split layout. Left side: key statistics in large type with icons. Right side: brief contextual paragraph. Use warm, human-centered imagery (not clinical/sterile).

**Speaker notes / Context:**

The populations we serve face a convergence of crises. Myanmar's post-2021 coup collapse of formal health services left millions dependent on fragmented alternatives. At the Thai border, refugee and migrant communities face barriers to local health systems. Key data points:

- **Myanmar:** 70% rural population; formal health services collapsed post-coup; active armed conflict in ethnic states (Karen, Kachin, Karenni)
- **Hepatitis B treatment** costs 78.6% of Myanmar's annual minimum wage — effectively inaccessible (Hsu et al., 2024, *Hepatology International*)
- **Hepatitis C genotype 6** is highly prevalent in northern Myanmar, with genotype 3 dominant in southern Thailand — regional variation with treatment implications (Pybus et al., 2015)
- **Parasitic infections:** 67% helminthic infection prevalence among Thailand-Myanmar border refugees at baseline; 37% Blastocystis prevalence in border villages (Yoshikawa et al., 2015; Popruk et al., 2011)
- **10% hepatitis B prevalence** among US-bound refugees screened from Thai-Myanmar border camps (Mitchell et al., 2018)
- **Telekyanmar** already serves ~1,500–2,000 patients/month with ~360 volunteer clinicians but has only **1 gastroenterologist contributing 2 hours/week** — the specialist bottleneck is severe

The gastroenterology/hepatology focus is not arbitrary. Liver disease and GI infections are among the highest-burden conditions in these populations, and the near-total absence of specialist access makes AI-assisted decision support especially high-impact here.

---

## Slide 3: Our Solution — The Consortium

**Visual/Layout notes:** Hub-and-spoke diagram. Mahidol University (Thailand) at center as lead applicant. Spokes to: Telekyanmar (Myanmar — operational partner), IDARA (Spain — AI technology), German Partners (Germany — evaluation & certification). Budget percentages shown along each spoke. Color-coded: LMIC partners in green (≥80%), European partners in blue (≤20%).

**Speaker notes / Context:**

| Partner | Country | Role | Approx. Budget Share |
|---------|---------|------|---------------------|
| **Mahidol University** | Thailand | Lead applicant; project management; coordination; subcontracting workflow development | Absorbs coordination costs + manages LMIC budget |
| **Telekyanmar** | Myanmar | Operational beneficiary; telemedicine delivery; ~360 volunteer clinicians, ~365 active providers, 5 clinics | Direct operational budget |
| **IDARA (IIS Galicia Sur)** | Spain | AI technology provider; AICOMTA system development, adaptation, and training delivery | ~USD 150K (salaries) from ≤20% European allocation |
| **German Partners (Ulrich Kuch, Jimmy Daza — Goethe University Frankfurt)** | Germany | Scientific evaluation; result certification; publications | ~USD 50K from ≤20% European allocation |

**EVAH budget rule:** ≥80% of the USD 1M must flow to LMIC partners (Thailand + Myanmar). ≤20% (≤USD 200K) to European partners. All allocations shown are indicative and subject to adjustment during budget finalization.

**Why Mahidol?** Most internationally recognized Thai university in health research; track record in international cooperation and grant management; located in Bangkok with access to border health networks. [TBD: Confirm Mahidol's formal agreement to serve as lead applicant]

---

## Slide 4: What EVAH Wants — And How We Fit

**Visual/Layout notes:** Two-column layout. Left: "EVAH Pathway A Requirements" (from the RFP). Right: "Our Proposal" (how we meet each one). Checkmarks for met requirements, yellow flags for items requiring attention.

**Speaker notes / Context:**

| EVAH Requirement | Our Position | Status |
|-----------------|-------------|--------|
| AI-enabled Clinical Decision Support Tool (CDST) | AICOMTA: RAG-based system on Gemini 2.0 Flash; specialist-validated knowledge base | ✅ Eligible (FAQ Q22, Q29 — LLM wrappers explicitly accepted) |
| Prior validation evidence | Spanish validation: 4.2/5 expert quality, 87.5% adoption intent, 328 real clinical conversations | ✅ Transferable (FAQ Q27 — cross-geography validation accepted) |
| LMIC-based lead applicant | Mahidol University, Thailand | ✅ Eligible |
| Frontline health worker use | Telekyanmar volunteer doctors + border health workers | ✅ Aligned |
| Primary health care setting | Community clinics, telemedicine consultations | ✅ Eligible (FAQ Q56, Q58) |
| Comparison group required | Need quasi-experimental design (not just before-after) | ⚠️ Must design stepped-wedge or matched control approach (FAQ Q39) |
| Ethics plan (not approval) | Must describe ethics plan; approval NOT required before submission | ✅ Feasible (FAQ Q67–Q75) |
| IP stays with applicant | Funder gets non-exclusive license; IDARA retains AICOMTA IP | ✅ Compatible (FAQ Q61–Q66) |
| Pathway A → B progression | Explicitly encouraged by EVAH | ✅ Strategic opportunity (FAQ Q35) |

**Critical compliance note:** Our Pathway A study design must include a comparison strategy. A stepped-wedge cluster design (rolling out the AI tool to clinics sequentially) or a matched-controls approach between AI-assisted and non-AI-assisted clinics are both viable. We should discuss which fits our operational reality better.

---

## Slide 5: The Evidence Base — Why This Should Work

**Visual/Layout notes:** Three evidence pillars shown as columns. Left: "AICOMTA Validated" (Spain data). Center: "LLM Evidence Growing" (published literature). Right: "LMIC Gap = Opportunity" (the evidence gap we fill). Key statistics highlighted in callout boxes.

**Speaker notes / Context:**

**Pillar 1 — AICOMTA is already validated in real-world clinical use:**
- 328 genuine clinical conversations over 6 months (Nov 2024–Apr 2025)
- Expert panel quality rating: **4.2/5** (blinded, 13 independent evaluators)
- Scientific accuracy: **4.4/5**
- Physician trust: **87.5%** would integrate into routine practice
- Published HCV retrieval outcomes: 64.6% patient retrieval → 87.1% sustained virological response
- Compliance with CHART (Chatbot Assessment Reporting Tool) declaration

**Pillar 2 — Growing evidence that LLM-based tools improve clinical decisions:**
- RAG-based systems show ~10% accuracy improvement over standalone LLMs (Neha et al., 2025; Yang et al., 2025)
- GPT-4 includes correct diagnosis in ~68% of complex cases (Ríos-Hoyo et al., 2024)
- AMIA consensus: AI works best as decision aid augmenting clinical judgment (Labkoff et al., 2024)
- Training and workflow integration are the two most critical success factors (Lambert et al., 2023, 194 citations)

**Pillar 3 — The LMIC evidence gap is our strategic position:**
- Only ~10 evaluations of AI in real-world LMIC health contexts found in comprehensive scoping review (Ciecierski-Holmes et al., 2022, *NPJ Digital Medicine*, 155 citations)
- No published evidence on RAG-based clinical assistants deployed in Myanmar or Thailand border populations
- EVAH exists precisely to fill this gap — our proposal is exactly what they're funding

---

## Slide 6: Work Package 1 — AI Clinical Support Assistant (~35% of budget)

**Visual/Layout notes:** Workflow diagram showing: AICOMTA system (center) → connected to Telekyanmar platform (left) and Training Course (right). Below: timeline bar showing Phase 1 (Adaptation, months 1–4), Phase 2 (Deployment + Training, months 4–10), Phase 3 (Analysis, months 10–12). Budget callout: ~USD 350,000.

**Speaker notes / Context:**

**WP1 delivers the core AI intervention and its evaluation.**

**Component A — AICOMTA Deployment (~USD 300K)**
- Adapt AICOMTA's RAG knowledge base for the Thailand–Myanmar context: local clinical guidelines, regional disease patterns (hepatitis B/C, liver disease, GI parasitic infections), multilingual support
- Integrate into existing Telekyanmar chat-based telemedicine workflow (not building a new EMR — confirmed in March 13 meeting)
- Serves both in-situ physicians in Myanmar AND volunteer doctors assisting remotely
- Technical costs (tokens, servers, deployment) managed from LMIC budget through the Thai lead partner (~USD 150K)
- IDARA team salaries for adaptation and technical support (~USD 150K from European allocation)

**Component B — 20-Hour Structured Training Course (~USD 50K)**
- Target: 50–150 Telekyanmar healthcare professionals
- 1-week intensive course with reusable materials
- Translated into multiple local languages (Burmese, Karen, Kachin, Karenni)
- Includes: avatar/mascot, usage videos, recorded sessions, full digital learning environment
- Pre/post assessment and certification — this creates the before/after evaluation data

**Why this enables rigorous evaluation:**
The training course is not just capacity building — it's a natural evaluation structure. Pre-course clinical decision quality vs. post-course quality (with AI tool) creates measurable outcomes. Combined with a stepped-wedge rollout to different clinic sites, this gives us Pathway A–quality evidence of implementation readiness and early efficacy signals for the Pathway B application.

**Budget note:** ~USD 350,000 total. All figures subject to change during budget finalization.

---

## Slide 7: Work Package 2 — Telemedicine Digitalization & Workflow Optimization (~40% of budget)

**Visual/Layout notes:** Before/after comparison. Left ("Now"): Facebook chat icon, paper medical records, 5 clinics. Right ("After"): Structured triage system, digitized records stored in Thailand, nationwide connectivity, AI-integrated workflow. Budget callout: ~USD 400,000.

**Speaker notes / Context:**

**WP2 is the qualitative leap for Telekyanmar — from Facebook chat to structured clinical service.**

**The transformation:**
- **From** asynchronous Facebook Messenger consultations **to** structured triage with clinical guidelines, video-conference capability where connectivity permits, and AI-integrated workflow
- **From** paper medical records **to** digitized clinical records stored on servers in Thailand (not Myanmar — for data security in conflict context)
- **From** 5 clinics **to** expanded connectivity nationwide
- **From** manual scheduling and follow-up **to** AI-assisted operational workflow (scheduling, record management, process optimization)

**Key infrastructure investments (all lightweight — no buildings):**
- Servers located in Thailand for stability and data protection
- Devices (tablets, affordable computers) for healthcare workers inside Myanmar
- Connectivity expansion from current 5-clinic footprint
- Digital marketing (~USD 30K in Meta/Google Ads) for service outreach to target populations
- Civil liability and equipment insurance for conflict zones (justifiable as indirect costs, up to 20% of direct costs per EVAH rules)

**Critical sustainability principle:** Everything implemented must function after the funding year ends at minimal or self-financed cost. This is not about building dependency — it's about digitizing what already exists and making it more efficient. No physician salaries are paid from this budget line. Telekyanmar's 360 volunteer clinicians continue to volunteer; we're improving the tools they work with.

**Reusable elements from EKFS proposal:** Operational data (190,000+ consultations, 86% patient/provider satisfaction), budget structure logic, Myanmar healthcare context analysis, logframe approach. We adapt rather than reinvent.

**Budget note:** ~USD 400,000 total. All figures subject to change during budget finalization.

---

## Slide 8: Work Package 3 — Coordination, Management & Evaluation (~25% of budget)

**Visual/Layout notes:** Governance org chart showing Mahidol (top, project lead) → three lines down to: Telekyanmar (Myanmar operations), IDARA (AI technology), German Partners (evaluation). Cross-cutting bar at bottom: "Ethics | Data Governance | M&E Framework." Budget callout: ~USD 250,000.

**Speaker notes / Context:**

**WP3 is the glue — cross-country coordination across 4 time zones, ethics oversight, and evaluation design.**

**Thailand coordination (Mahidol University — lead):**
- Administrative project management and financial oversight
- Subcontracting development of workflows/processes for the new telemedicine system
- Ethics submission to Thai IRB (described in application, submitted after award — per FAQ Q67–Q75)
- Manages ≥80% LMIC budget allocation

**Myanmar operations (Telekyanmar):**
- Local administrative staff (low salaries, justifiable for 12 months)
- Medications and consumables (~USD 100K, adapted from EKFS budget structure)
- Travel and logistics within Myanmar
- Local coordination personnel

**German partners — scientific evaluation and certification (Ulrich Kuch, Jimmy Daza, Goethe University Frankfurt):**
- Design and oversee the evaluation methodology (quasi-experimental design with comparison group)
- Certify results for publication
- Ensure evaluation meets EVAH/J-PAL rigor standards for Pathway A → Pathway B progression
- Budget: ~USD 50K from the ≤20% European allocation

**Data governance:**
- Patient data digitized in Myanmar, stored on servers in Thailand
- GDPR-aware framework (IDARA as European data processor)
- Open-access publication commitment
- IP retained by IDARA; funder receives non-exclusive license (FAQ Q61–Q66)

**Monitoring & evaluation framework:**
- Baseline assessment before AI tool deployment
- Stepped-wedge or matched-controls design for comparison
- Quarterly consortium meetings (cross-timezone — Bangkok, Myanmar, Spain, Germany)
- Mid-point review at month 6

**Budget note:** ~USD 250,000 total (remaining after WP1 + WP2). All figures subject to change during budget finalization.

---

## Slide 9: Timeline and Evaluation Strategy

**Visual/Layout notes:** Gantt chart spanning 12 months. Three horizontal bars for WP1, WP2, WP3. Key milestones marked with diamonds. Evaluation design shown as overlay. Right side: pathway from "Pathway A Evidence" → arrow → "Pathway B Application (future round)."

**Speaker notes / Context:**

| Month | WP1: AI Clinical Support | WP2: Telemedicine Digitalization | WP3: Coordination |
|-------|-------------------------|--------------------------------|-------------------|
| 1–3 | Knowledge base adaptation; local guideline integration; multilingual content | Server setup in Thailand; device procurement; workflow design | Ethics submission; baseline data collection; governance setup |
| 4–6 | Training course development; pilot deployment at first clinic sites | Record digitization begins; connectivity expansion starts | Comparison group enrollment; M&E framework operational |
| 7–9 | Full training delivery (50–150 professionals); stepped-wedge rollout | Structured triage system live; AI workflow integration | Midpoint evaluation; data quality review |
| 10–12 | Post-training assessment; usage data analysis; safety review | System stabilization; sustainability handover planning | Final analysis; publication drafting; Pathway B concept development |

**Evaluation design — addressing the "comparison group" requirement:**

We propose a **stepped-wedge cluster design**: the AI tool is rolled out to clinic sites in a staggered sequence. Sites waiting for deployment serve as concurrent controls. This is operationally realistic (you can't deploy everywhere at once) and methodologically rigorous (each site contributes both control and intervention data).

**Pathway A outcomes (intermediate, per FAQ Q41):**
- Diagnostic accuracy (clinician-adjudicated, pre/post training)
- Guideline adherence rates
- System Usability Scale scores
- Adoption rates and usage patterns
- Safety events / adverse AI recommendations
- Provider trust and workflow integration (qualitative)

**The Pathway A → B bridge:** EVAH explicitly encourages Pathway A grantees to apply for Pathway B in future rounds (FAQ Q35). Our Pathway A generates the implementation evidence (adoption, safety, feasibility) needed to justify a larger Pathway B impact evaluation (USD 3M, 12–24 months) measuring health outcomes.

---

## Slide 10: What We Need to Decide — Next Steps

**Visual/Layout notes:** Clean action-item table with owner and deadline columns. Traffic-light status indicators (green/yellow/red). Prominent "April 1 deadline" countdown.

**Speaker notes / Context:**

We have **14 days to submission.** Here is what needs to happen:

| Action Item | Owner | Deadline | Status |
|------------|-------|----------|--------|
| Confirm Mahidol University as lead applicant (formal agreement) | [TBD: Thailand contact] | March 22 | 🔴 Critical — blocks everything |
| Confirm PI at Mahidol (can only lead ONE EVAH application — FAQ Q6) | [TBD: Thailand contact] | March 22 | 🔴 Critical |
| Finalize budget using EVAH template (.xlsx) — respect ≥80% LMIC rule | All partners | March 27 | 🟡 In progress |
| Write evaluation protocol (stepped-wedge design with comparison group) | German partners + IDARA | March 25 | 🟡 Needs start |
| Compile CVs/biosketches for all key personnel | All partners | March 25 | 🟡 Partially available (EKFS biosketches reusable) |
| Draft ethics plan (not full approval — describe IRB submission timeline) | Mahidol + Telekyanmar | March 27 | 🟡 Needs start |
| Prepare partner letters of support | All partners | March 27 | 🟡 KDHW letter exists from EKFS; need Mahidol, IDARA |
| Internal review of complete draft application | All partners | March 28 | ⬜ Pending |
| Submit via EVAH portal | Mahidol (lead applicant) | **April 1** | ⬜ Deadline — no late submissions accepted |

**Open questions for consortium discussion:**

1. **Mahidol confirmation:** Is this locked in? If not, what is our backup? (This is the single biggest blocker.)
2. **Evaluation design:** Stepped-wedge cluster or matched-controls? We need the German partners' recommendation.
3. **Disease scope:** Should we stay narrowly focused on gastroenterology/hepatology (our strongest evidence) or broaden to general primary care (more appealing to reviewers)? The epidemiological data supports a GI/hepatology focus for these populations, but we should discuss.
4. **WP2 scope:** How ambitious is the telemedicine digitalization in a 12-month Pathway A? Should we scope it down and save the full transformation for Pathway B?
5. **Sustainability narrative:** What happens on day 366? The funders will ask. Our answer should be: the AI system runs at minimal cost (tokens + server), the training materials are reusable, and the digitized records persist. But we need to quantify "minimal cost."

---

*Document prepared for internal consortium use. All budget figures are indicative and subject to change. Statistics sourced from project documentation and published literature as cited. Items marked [TBD] require partner input before finalization.*

*Next meeting: March 20, 2026 — 9:30 AM Myanmar time*
