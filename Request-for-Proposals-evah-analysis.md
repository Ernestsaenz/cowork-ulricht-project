# Request-for-Proposals-EVAH: Comprehensive Biomedical Research & Funding Analysis

> **Version 2 — Updated with full integration of `EVAH RFP FAQ_0.pdf` (92 questions, 20 pages, released March 2026 by J-PAL/APHRC).** FAQ content is cited throughout as `(FAQ Q#)` and integrated within each analytical section in order.

---

## I. Folder Overview

This folder contains a **complete RFP package, a draft concept note, and the official FAQ** for the Evidence for AI in Health (EVAH) initiative — a USD 60 million global funding mechanism launched by the **Wellcome Trust, Gates Foundation, and Novo Nordisk Foundation**, managed by J-PAL and APHRC. The RFP opened February 20, 2026, with applications due **April 1, 2026**. The FAQ document (March 2026, 92 questions) represents the official interpretive guidance issued after the March 6 question deadline, and materially clarifies — and in several cases relaxes — requirements that appeared more stringent in the core RFP documents.

Alongside the funder guidance, the folder includes a **concept note proposing to evaluate AICOMTA in Myanmar** (Pathway A: early deployment, up to USD 1M, 3–12 months). The concept note is a February 2026 draft that explicitly identifies "Confirm Myanmar-based lead institution" as a next step.

**Apparent purpose:** Active proposal development. The funder materials (including the newly present FAQ) provide comprehensive guidance; the concept note represents the applicant team's early-stage response.

**Stage of work:** Pre-submission planning, not a finalized application. The FAQ materially changes the strategic picture: several blockers previously identified are less severe, while the adaptation-funding constraint emerges as a new concern.

---

## II. File Inventory and Categorization

| File Name | Type | Purpose | Notes |
|-----------|------|---------|-------|
| `Evidence for AI in Health (EVAH) RFP \| J-PAL.pdf` | Core RFP document | Main RFP announcement: timeline, pathways, eligibility, instructions | 5 pages |
| `RFP Overview - Evidence for AI in Health_0.pdf` | Detailed RFP guidance | Background, eligibility, priorities, exclusions, detailed pathway descriptions | 11 pages |
| `Application Guidelines - Evidence for AI in Health RFP_0.pdf` | Application instructions | 27 evaluation design questions, budget guidelines, checklist | 19 pages |
| `Evidence for AI in Health (EVAH) initiative \| J-PAL.pdf` | Initiative overview | Broad initiative description, co-chairs, key facts | 5 pages |
| `Announcing: Evidence for AI in Health RFP.pdf` | Dissemination | Email announcement to Grand Challenges community | 2 pages |
| `EVAH Budget Template.xlsx` | Budget tool | Structured Excel: Start Here, Initiative Budget, Total Project Budget | 3 worksheets |
| **`EVAH RFP FAQ_0.pdf`** | **Official FAQ / interpretive guidance** | **92 questions across 10 thematic sections; released after March 6 question deadline** | **20 pages — critical document** |
| `EVAH Concept Note for Myanmar.JD.docx` | **Applicant concept note** | Draft proposal to evaluate AICOMTA in Myanmar under Pathway A | Feb 2026 draft |

### II.A. FAQ Document: Structure and Analytical Summary

The FAQ (`EVAH RFP FAQ_0.pdf`) is the **single most important guidance document in the folder for a team preparing a submission**. It resolves ambiguities across all major application areas. Its 10 sections are:

| Section | Q# Range | Subject Matter | Key Implications for Myanmar/AICOMTA |
|---------|----------|----------------|--------------------------------------|
| 1. Eligibility & Partnerships | Q1–20 | Who can apply; consortium structure; partnership documentation | Several previously assumed blockers are relaxed — but the regional lead requirement is strictly confirmed |
| 2. Tool Eligibility & Readiness | Q21–29 | CDST definition; LLM wrappers; deployment readiness | AICOMTA's LLM-wrapper architecture is explicitly eligible; Spanish validation is transferable |
| 3. Pathway Selection | Q30–36 | A vs. B logic; transitions; multi-pathway submissions | Pathway A → B sequential strategy is explicitly encouraged |
| 4. Evaluation Design & Methods | Q37–43 | Methods; rigor definition; power; outcomes | Mixed-methods fine; before-after alone insufficient; Pathway A sample size must be justified |
| 5. Budget & Supported Costs | Q44–53 | What's fundable; subawards; software; indirect costs | Software adaptation is **limited** — may not cover the full Myanmar localization phase |
| 6. Geographic & Setting Questions | Q54–60 | PHC definition; disease scope; site specification | Faith-based, private, and disease-specific programs all eligible |
| 7. Data Governance & Sharing | Q61–66 | Open access; IP; proprietary models; commercialization | IP retention permitted; open-sourcing not required; commercialization allowed |
| 8. Equity, Ethics & Responsible AI | Q67–75 | Ethics timing; consent; bias; human-in-the-loop; safety | Ethics approval NOT required at application stage; algorithmic bias assessment encouraged |
| 9. Submission, Review & Award | Q76–83 | Portal; late submissions; reviewer comments; award process | No late submissions; projects cannot start before grant agreement AND ethics approval |
| 10. Proposal Evaluation & Selection | Q84–92 | Scoring; rejection reasons; scoring within pathway | Five common rejection reasons explicitly stated; emphasis on decision-relevant evidence |

### Content Gaps (Updated)

- **FAQ now present** — the original analysis flag that "No FAQ responses" were available is resolved
- **Budget template not yet filled out** — confirmed by FAQ (Q44) as intentionally high-level at this stage; detailed budget will be requested at due diligence if selected
- **No review scoring rubrics** beyond embedded Application Guidelines guidance and FAQ Section 10
- **No completed applications** — only concept note/draft

---

## III. Scientific and Biomedical Content Analysis

### III.A. What the RFP Requires

**Focus:** AI-enabled clinical decision support tools (CDSTs) that support frontline health workers in LMICs. Disease-agnostic but emphasizes cross-cutting primary health care (PHC) functions.

**CDST Definition (FAQ Q22):** An AI-enabled CDST must:
1. Support clinical decision-making (triage, diagnosis, referral, treatment guidance)
2. Be used by frontline health workers — *not patients directly* — in eligible countries
3. Be integrated into real-world care workflows, not a standalone application
4. Have moved beyond proof-of-concept with demonstrated performance in validation studies
5. Generate actionable guidance at the point of care

**What is NOT funded (FAQ Q21–22, Q25):** Patient-facing apps, standalone chatbots not integrated into provider workflows, management dashboards for policymakers, general AI model development, supply chain decision-making tools.

**LLM wrappers (FAQ Q29):** Explicitly acceptable — "Either is acceptable. Please describe clearly whether your solution is based on a wrapper of an existing LLM or not." This directly validates AICOMTA's Gemini 2.0 RAG architecture.

**Eligible geographies:** Sub-Saharan Africa, South Asia, Southeast Asia (LMICs within these regions). Multi-country evaluations are permitted (FAQ Q55).

**PHC setting definition (FAQ Q56):** "First-contact care delivered at community or outpatient level, such as community health worker programs, health centers, dispensaries, and outpatient primary care clinics." Key requirement: tool supports frontline decision-making within routine service delivery pathways. Importantly, ICU/acute ward/emergency medicine tools are NOT eligible unless clearly integrated with frontline PHC pathways (FAQ Q57). Private and faith-based facilities are eligible (FAQ Q58).

**Disease-specific programs (FAQ Q59):** Disease-specific programs such as maternal health, TB, HIV qualify *if the tool supports frontline clinical decision-making within routine PHC workflows* rather than functioning as a vertical research-only intervention.

**Two pathways (FAQ Q30–35):**
- **Pathway A (3–12 months, up to USD 1M):** Implementation readiness evidence — usability, adoption, workflow fit, operational feasibility, training needs. Appropriate when tool is not yet stable enough to measure reliable outcome impacts across sites.
- **Pathway B (12–24 months, up to USD 3M):** Decision-grade impact evidence — causal effects on clinical decisions, health outcomes, efficiency, equity. Requires maturity for rigorous impact evaluation at scale.
- Pathways are **mutually exclusive per project** — a project cannot transition from A to B during the same grant (FAQ Q32).
- An institution *can* submit separate applications for both pathways for different tools/countries (FAQ Q34).
- **If funded under Pathway A, the team can apply for Pathway B in a future round** — explicitly encouraged (FAQ Q35).

**Readiness definition (FAQ Q23):** "Ready for deployment at scale does not necessarily require national or multi-country deployment. Rather, it refers to tools that are sufficiently mature and stable within real-world care settings to support rigorous evaluation." Both pathways require prior validation evidence (pilot deployments, validation studies, usability testing, or documented real-world/simulated performance).

### III.B. Myanmar Concept Note: AICOMTA Evaluation

**AI Intervention:** AICOMTA (Compartir Talento) — a RAG-based conversational AI providing guideline-referenced, specialist-validated clinical responses. Built on Gemini 2.0, developed by IDARA/Instituto de Investigación Sanitaria Galicia Sur (Spain), led by Dr. Juan Turnes. Part of broader LiverAI technology stack.

**Architecture eligibility (FAQ Q29):** AICOMTA is a wrapper of an existing LLM (Gemini 2.0) with RAG. The FAQ explicitly confirms this architecture is eligible — the application must simply describe the solution clearly.

**Prior validation geography (FAQ Q27):** Prior AI tool validation does NOT need to be in the exact evaluation geography. "Applicants should document prior performance and contextual relevance and explain how the tool will be safely adapted and monitored locally. Proposals should include plans for performance and safety monitoring in the new context." This is a significant clarification — AICOMTA's Spanish validation data is **directly citable as evidence of readiness**, provided the application includes a contextual relevance justification and local safety monitoring plan.

**Tool ownership geography (FAQ Q26):** AICOMTA is owned by IDARA, a Spanish company. The FAQ confirms this is permissible — "Yes, provided the project meets all eligibility criteria (e.g., where the lead applicant is legally registered and operational) and complies with funders' access and data-sharing policies."

**Developer as consortium partner (FAQ Q13):** IDARA (the AI tool developer) does NOT need to be a formal consortium partner — the tool can be procured/authorized without IDARA joining the consortium. However, optional letters of support from technology partners are encouraged where possible.

**Clinical focus:** Gastroenterology, general internal medicine, endocrinology — targeting primary care and community health workers in rural Myanmar (70% rural population).

**Research questions:**
1. Can AICOMTA be effectively adapted (linguistically, clinically, culturally) for Myanmar frontline workers?
2. How do frontline workers perceive and adopt AICOMTA (usability, trust, workflow integration)?
3. What is the safety profile when non-specialists use AICOMTA for triage, diagnosis, referral?

**Study design:** Mixed-methods early-deployment evaluation:
- Phase 1 (3 months): Clinical content localization with expert validation
- Phase 2 (6 months): Pilot deployment at 3–5 primary care/community health centers via national telemedicine infrastructure
- Phase 3 (3 months): Analysis and reporting
- **Quantitative:** System Usability Scale, adoption rates, clinician-adjudicated accuracy, safety monitoring
- **Qualitative:** Interviews on trust, workflow fit, barriers

**Before-after studies (FAQ Q39):** The concept note's current design lacks an explicit comparison group. The FAQ states that simple pre-post comparisons without a counterfactual "generally do not provide sufficiently rigorous evidence." For Pathway A, a comparison strategy is still needed — matched controls, interrupted time series, or quasi-experimental approaches are acceptable alternatives to a full RCT.

**Intermediate outcomes (FAQ Q41):** For Pathway A, if direct health outcomes are infeasible within the study timeframe, "validated intermediate outcomes (e.g., diagnostic accuracy, guideline adherence)" are acceptable. This directly supports AICOMTA's clinician-adjudicated accuracy outcome.

**Consortium:**
- Myanmar-based lead institution (TBD — **critical gap** — see Section IV)
- Myanmar national telemedicine provider (infrastructure partner)
- IDARA/Dr. Juan Turnes (Spain) — AICOMTA development and adaptation
- University Hospital Mannheim/Heidelberg University — evaluation design, data governance
- Hospital Partnership Alliance (HPA), PINTAI working group

### Strengths

- **Mature AI technology** with real-world validation data from Spain (4.06/5 acceptance; 328 clinical conversations; expert panel evaluation) — eligible as Pathway A readiness evidence even though not from Myanmar (FAQ Q27)
- **LLM wrapper architecture explicitly eligible** (FAQ Q29)
- **Spanish tool ownership no barrier** to Myanmar evaluation (FAQ Q26)
- Clear, testable research questions aligned with Pathway A objectives
- Integration into existing telemedicine infrastructure (scalability potential)
- Focus on non-specialist frontline workers (equity/access angle)
- Mixed-methods approach matching EVAH methodological expectations (FAQ Q37, Q43)
- Safety monitoring explicit (FAQ Q73 confirms this is expected)

### Weaknesses

- **Lead applicant not confirmed** — application is non-compliant without named Myanmar organization/PI (strictly confirmed by FAQ Q1–2)
- **No explicit comparison group** — mixed-methods design lacks counterfactual strategy (FAQ Q39 flags this as insufficient for even Pathway A)
- **Narrow disease scope** — gastroenterology and endocrinology may seem niche for primary care in Myanmar; epidemiological justification needed
- **Limited health system context** — concept lacks detail on Myanmar PHC structure
- **3-month adaptation timeline may be optimistic** — and may hit the software adaptation funding constraint (FAQ Q50)
- **Safety oversight model not detailed** — FAQ Q72–73 make this an explicit requirement
- **Study sites not specified** — FAQ Q60 states sites should be specified at application; additions after project begins generally require funder approval

---

## IV. Funding and Grant-Application Analysis

### IV.A. Funder Profile

| Funder | Role | Key Policy Requirements |
|--------|------|------------------------|
| Wellcome Trust | Co-funder; final decision | Clinical trials policy, Global and Open Access policies |
| Gates Foundation | Co-funder; final decision | Global and Open Access policies; commercialization potential |
| Novo Nordisk Foundation | Co-funder; final decision | IP policy; Data Ethics and AI Policy |

**Implementation partners:** J-PAL (methodology) and APHRC (African context). Final funding decisions are made by the three funders according to their internal approval processes (FAQ Q80). Grants will be managed by the Wellcome Trust, Gates Foundation, and Novo Nordisk Foundation (FAQ Q83).

### IV.B. Eligibility Clarifications from FAQ

The FAQ substantially clarifies eligibility requirements, resolving ambiguities in the core RFP. Most importantly for the Myanmar concept:

**"Based in the region" — strict four-condition definition (FAQ Q2):**
1. Legally registered entity in SSA, South Asia, or Southeast Asia
2. Organization is operationally active in the region (conducting programmatic activities there)
3. PI or Project Lead is based in the region
4. Core project activities — including evaluation and deployment — are led or co-led by regional organizations, with at least 80% of funds flowing to regional entities

> *Having staff or collaborators in the region alone is NOT sufficient if legal registration and project leadership requirements are not met.* (FAQ Q2b)

This is **the single most critical eligibility gate** for the Myanmar concept note. The Heidelberg/Mannheim team (Germany) and IDARA (Spain) cannot be the lead applicant — a Myanmar-registered, operationally-active organization with a Myanmar-based PI is required.

**PI employment (FAQ Q15–16):** The PI or Project Lead does NOT need to be employed by the lead applicant organization; lead applicants may partner with external research organizations or PIs not employed by them. The lead applicant also does NOT need to be an academic researcher or employed at a research institution.

**Evaluation geography (FAQ Q17):** The proposed evaluation does not need to take place in the same country where the lead applicant is registered, provided the lead applicant is also legally operating in additional countries in the region.

**Private AI companies as lead (FAQ Q3):** Private AI companies and for-profit entities ARE eligible to serve as lead applicants, provided they are legally registered and operational in an eligible region, with PI/Project Lead based there. The proposal must also include a clinical implementation partner and evaluation expertise, and focus on evidence generation rather than product development.

**Ministry of Health as lead (FAQ Q5):** A Ministry of Health IS eligible to serve as lead applicant, provided they meet all standard eligibility requirements.

**Multiple proposals (FAQ Q6):** Organizations may submit multiple proposals for different countries or tools. However, a PI or Project Lead within an organization may submit **only ONE application as lead**. This has direct implications: if Dr. Ulrich Kuch (Heidelberg) serves as PI on the EKFS application, he cannot also serve as lead PI on the EVAH application. Role assignments across the two Myanmar-facing proposals must be carefully managed.

**Three core consortium functions required (FAQ Q8):** All proposals must include partners that collectively cover:
1. Clinical implementation (service-delivery organization where tool will be deployed)
2. Evaluation expertise (institution capable of rigorous health systems or impact evaluation)
3. Project management/implementation capacity (coordination and delivery)

The Myanmar concept covers functions 2 (Heidelberg) and 3 (telemedicine provider) explicitly, but function 1 (clinical implementation partner) is insufficiently documented.

**Clinical implementation partner letter required (FAQ Q8c):** "The lead applicant is responsible for assembling the consortium at the time of application. Applicants must have an identified clinical implementation partner in place when submitting the proposal. A letter of support from the clinical implementation partner is required, unless the lead applicant itself serves as the clinical implementation partner." This is a **hard submission requirement**.

**Technology developer as consortium partner (FAQ Q9, Q13):** The technology developer (IDARA/Spain) CAN be part of the evaluation team but must demonstrate independent evaluation capacity alongside it. Alternatively, the tool can be procured without IDARA joining the consortium formally — optional letters of support from technology partners are encouraged. Either arrangement is viable for AICOMTA.

**Evaluator and implementer as same organization (FAQ Q10):** Permissible provided the proposal demonstrates credible evaluation capacity, manages conflicts of interest, and uses objective methods (independent oversight, transparent methods, or separate evaluation personnel).

**Formal data sharing agreement (FAQ Q12):** NOT required at application stage. Applicants must describe how they will meet Global and Open Access expectations and willingness to share findings. Formal agreements are put in place post-selection.

**Country-specific regulatory compliance (FAQ Q20):** Applicants must comply with all local legal requirements. In Myanmar's context, this includes any digital health device regulations that may apply to AICOMTA deployment. The application should address this even if no specific regulatory approval is required before submission.

### IV.C. Budget Clarifications from FAQ

The FAQ significantly clarifies what is and is not fundable — with one major implication for the Myanmar concept's adaptation-heavy Phase 1.

| Budget Item | Eligible? | FAQ Reference | Implication for Myanmar Concept |
|------------|----------|---------------|--------------------------------|
| Software adaptation (localization, configuration) | **Limited** — only if necessary to enable evaluation | Q50 | Phase 1 "clinical content localization" may be partially fundable IF framed as enabling evaluation, not product development |
| Core product development, model training, major feature expansion | **No** | Q50 | Must not frame AICOMTA expansion into new disease areas as fundable |
| Licensing fees for AI tool | **Yes** — if necessary for evaluation period | Q52 | Gemini API/AICOMTA licensing costs for pilot deployment are eligible |
| Cloud hosting / API usage fees | **Yes** — when required to run tool | Q53 | Gemini 2.0 API costs during evaluation period are eligible |
| Commercialization preparation | **No** | Q49 | Market expansion, product rollout costs are excluded |
| Subawards to partners | **Yes** — with 80% regional fund flow | Q45 | Spanish and German team fees count toward the 20% non-regional cap |
| Partner costs within lead budget | **Yes** | Q46 | IDARA and Heidelberg costs can be included in Myanmar lead's budget |
| Indirect costs | **Max 20% of direct costs** at application stage | Q51 | Per RFP; will be finalized at funder level post-selection |
| Commercialization prep costs | **No** | Q49 | Cannot use funds for market expansion or software rollout |

**Critical budget constraint for Myanmar concept:** Phase 1 (3-month adaptation) is the most at-risk budget category. The FAQ is explicit (Q50): "In general, software and product development will **not** be funded. Limited software adaptation *may* be supported *only* if it is necessary to enable the evaluation (for example, configuration, integration, localization, or minor modifications required for deployment in the study setting)." The Myanmar content localization, language adaptation, and knowledge base expansion must be framed as **evaluation-enabling configuration**, not as AICOMTA product development. If reviewers judge it as the latter, Phase 1 costs may be ruled ineligible.

**Budget template (FAQ Q44):** The template is intentionally high-level at application stage. Detailed budget per individual funder guidelines will be requested post-selection. "Funds are intended for evaluation and necessary implementation to support that evaluation." Reviewers will assess whether budget is commensurate with scope and value-for-money.

**80% regional fund flow (FAQ Q45, Q48):** At least 80% of funds must flow to SSA, South Asia, or Southeast Asia-based entities. Non-regional vendor/partner fees (IDARA in Spain; Heidelberg in Germany) count toward the 20% cap. The budget narrative must clearly indicate which organization incurs each cost.

### IV.D. Data Governance and IP — Significantly Clarified by FAQ

Several concerns raised in the initial analysis are materially resolved by the FAQ:

**IP retention (FAQ Q65):** "Yes. Organizations may retain ownership of their technology. However, applicants must demonstrate that the outcomes of the research can inform public health decision-making and that access to the benefits of the research will not be unreasonably restricted." IDARA/AICOMTA retaining IP is not a blocker for EVAH eligibility.

**Open-sourcing NOT required (FAQ Q64):** "No. Global Access policies focus on access to evidence and public health benefit, not mandatory release of proprietary source code." This entirely removes the previously flagged concern about AICOMTA's proprietary nature conflicting with funder requirements.

**Proprietary models eligible (FAQ Q63):** Proprietary AI models can be evaluated. "Participation in EVAH does not require open-sourcing the model."

**Commercialization permitted (FAQ Q66):** "Applicants should describe how reasonable pricing, licensing, or distribution plans will support equitable access in low- and middle-income settings consistent with Global Access principles." IDARA's potential commercialization of AICOMTA is compatible with EVAH, provided an equitable access plan is articulated.

**Patient-level data (FAQ Q62):** Not required to be publicly shared. Patient privacy takes priority; EVAH does not require data to be hosted or transferred outside the country where the study is conducted.

**Global Access requirements (FAQ Q61):** Funded projects must: describe how findings will advance equitable access; share findings to contribute to broader learning and public health use; allow results to be synthesized with other EVAH studies; follow funder-specific data-sharing, publication, and IP requirements (determined post-selection by assigned funder).

### IV.E. Ethics and Responsible AI — Key Clarifications

**Ethics approval timing (FAQ Q67):** Ethics approval is **NOT required at the application stage**. Applicants must describe the anticipated ethical considerations and the process for obtaining approvals. IRB approvals are required before award contracting and any human subjects work. This removes what was previously listed as a submission blocker — the concept only needs to describe the IRB pathway, not obtain approval before applying.

**Human-in-the-loop requirement (FAQ Q72):** "Tools should support, not replace, clinical decision-making by frontline health workers. The evaluation should reflect real-world supervision and accountability structures within the health system." This is a design and narrative requirement — the concept must explicitly describe how AICOMTA supports (but does not supplant) the clinical judgment of Myanmar health workers.

**Safety monitoring (FAQ Q73):** "Applicants should describe procedures for identifying and managing potential harms, incorrect recommendations, or adverse events during the evaluation. Monitoring approaches should be proportionate to the level of risk posed by the intervention." This is an **explicit application requirement** that the concept note currently addresses only superficially.

**Algorithmic bias (FAQ Q70):** Applicants are "encouraged to examine performance across relevant population subgroups (e.g., gender, age, geography, or cadre) where feasible." The Myanmar concept should include a subgroup analysis plan even if it is exploratory.

**Patient notification of AI use (FAQ Q71):** Applicants should follow local ethics guidance and regulatory requirements. Where appropriate, patient-facing communication should support transparency.

**Independent oversight committees (FAQ Q75):** Not universally required; higher-risk studies may warrant additional oversight, which applicants should justify. Given that AICOMTA is being used by non-specialists for clinical decision-making, addressing oversight proactively is advisable.

**Community engagement (FAQ Q68):** Not mandatory as a standalone requirement but strongly encouraged. The concept should describe how frontline health workers, supervisors, patients, and local health authorities will be involved.

### IV.F. Review Criteria and Competitive Positioning

**Review process (FAQ Q84):** All submissions first undergo **administrative and eligibility screening** before full technical review. Only eligible proposals proceed. This makes eligibility compliance the absolute first gate — proposals missing required elements (lead applicant identification, clinical implementation partner letter) will be screened out before scientific review.

**Common rejection reasons (FAQ Q85) — explicitly stated:**
1. Misalignment with the objectives of the selected funding pathway or RFP scope
2. Insufficient rigor in the proposed evaluation design
3. Lack of a credible implementation setting or partnerships
4. Tool not meeting readiness requirements (e.g., still in development)
5. Limited relevance for real-world decision-making

**Scoring within pathway (FAQ Q86):** Applications are reviewed relative to expectations of their chosen pathway, not directly compared across pathways. Both pathways consider: overall relevance, feasibility, strength of partnerships, and potential contribution to evidence — with different emphasis.

**Innovation vs. scalability (FAQ Q89):** Primary emphasis is on "the proposal's potential to generate decision-relevant evidence for real-world health system use." Tools that are novel but lack a clear integration pathway or evaluation readiness will be less competitive. The Myanmar concept's use of existing telemedicine infrastructure directly addresses this.

**CDST vs. standard of care comparisons (FAQ Q92):** Scored on policy relevance, technical design, feasibility, partnership strength, and contribution to evidence — including "incremental learnings on how AI-enabled CDSTs perform relative to existing options." Studies advancing foundational principles (how training data, implementation strategies, or provider behavior influence CDST integration) may be considered "particularly innovative and valuable."

**Previously funded pilots (FAQ Q90):** Eligible if generating **new, rigorous evidence**. The AICOMTA Spain pilot can be cited as evidence of maturity; it cannot be repeated or merely replicated in Myanmar.

**Pathway A → B strategy (FAQ Q35):** Explicitly: "We expect this will be feasible and encouraged, pending final subsequent RFPs' thematic priorities." This validates the Myanmar concept's staged approach.

### IV.G. Submission Readiness Assessment (Revised)

**Current status: NOT READY FOR SUBMISSION — with important nuance**

Several previously identified blockers have been resolved by the FAQ. The remaining blockers are:

**Hard eligibility blockers (will cause administrative rejection, FAQ Q84):**
1. **No named lead applicant organization** legally registered and operational in Myanmar (FAQ Q1–2) — confirmed CRITICAL
2. **No PI/Project Lead identified** who is based in Myanmar (FAQ Q2) — confirmed CRITICAL
3. **No clinical implementation partner letter of support** — confirmed REQUIRED at submission (FAQ Q8c)

**Important gaps that weaken competitiveness but are NOT hard blockers:**
4. **Study sites not specified** — FAQ Q60 states sites should be specified at application; vague sites are a weakness
5. **No comparison group described** — simple usability-only design risks "insufficient evaluation rigor" rejection (FAQ Q39, Q85ii)
6. **Budget not itemized** — FAQ confirms template is high-level (Q44), but a reasonable budget estimate is still expected; value-for-money will be assessed
7. **Safety monitoring plan absent** — explicitly expected (FAQ Q73)
8. **Human-in-the-loop model not described** — required (FAQ Q72)

**Resolved concerns (no longer blockers):**
- ~~IP conflict with AICOMTA proprietary model~~ → Not required to open-source (FAQ Q64–65)
- ~~Spanish-only validation inadequate~~ → Prior validation need not be in exact geography (FAQ Q27)
- ~~LLM wrapper architecture ineligible~~ → Explicitly eligible (FAQ Q29)
- ~~Ethics approval needed before submission~~ → Not required at application stage (FAQ Q67)
- ~~Budget needs full detail~~ → Template intentionally high-level; details required only at due diligence (FAQ Q44)
- ~~Data sharing agreement required~~ → Not required at application stage (FAQ Q12)

**New concern identified by FAQ:**
- **Phase 1 adaptation costs may be ineligible** if framed as product development rather than evaluation-enabling configuration (FAQ Q50) — requires careful narrative framing

**Deadline:** April 1, 2026

---

## V. Strategic Interpretation

### V.A. Project Goals

The Myanmar concept aims to generate **early-deployment evidence on whether AICOMTA can be successfully adapted and used by non-specialist frontline health workers in Southeast Asia**. Positive results would justify a Pathway B impact evaluation in a future EVAH round — a transition the FAQ explicitly calls "feasible and encouraged" (FAQ Q35).

### V.B. Maturity Assessment

| Dimension | Rating | Evidence |
|-----------|--------|---------|
| AI technology maturity | **High** | Spanish validation; 328 conversations; 4.06/5 acceptance; award-winning; LLM wrapper explicitly eligible |
| Myanmar implementation readiness | **Low-Moderate** | No prior deployment; partnership TBD; sites unspecified |
| Evaluation design rigor | **Low** | Questions clear but no comparison group, no sample size, no outcome measurement plan |
| Team's Myanmar experience | **Unclear** | Partnerships mentioned but not documented; German/Spanish teams' prior Myanmar work not evidenced |
| Consortium assembly | **Incomplete** | Three required functions not fully covered; clinical implementation partner unconfirmed |

### V.C. Funding Strategy Assessment

The Pathway A → B sequential strategy is well-reasoned and **explicitly validated by FAQ Q35**. The Myanmar concept's logic is coherent: deploy AICOMTA via existing telemedicine infrastructure, generate early-deployment evidence (Pathway A), and use that evidence to design and power a Pathway B impact evaluation in a future round.

However, the concept's competitiveness depends critically on:
1. Identifying a qualified Myanmar lead organization and PI before April 1
2. Securing a clinical implementation partner letter
3. Adding a comparison group or adequate counterfactual strategy to avoid "insufficient rigor" rejection

**PI conflict risk:** If Dr. Ulrich Kuch (Goethe/Heidelberg) is the PI on the EKFS application (EUR 500K), he cannot simultaneously serve as lead PI on the EVAH application (FAQ Q6). Roles across the two Myanmar-facing proposals must be explicitly differentiated.

### V.D. Barriers to Success (Revised)

**Operational/eligibility barriers:**
1. **Identifying a qualified Myanmar lead PI** with health systems research expertise and institutional affiliation in Myanmar — acute time constraint with <2 weeks to deadline
2. **Securing clinical implementation partner letter** from MOH, health facility network, or Myanmar NGO delivering primary care
3. **Specifying study sites** — FAQ Q60 states additions after project start generally require funder approval; sites should be committed at application

**Scientific/methodological barriers:**
4. **Comparison group design** — the current before-after design is insufficient per FAQ Q39; a comparison strategy (matched controls, ITS, or similar) must be incorporated without over-complicating a Pathway A scope
5. **Adaptation phase funding risk** — Phase 1 (clinical content localization) may not be fundable as written; must be reframed as evaluation-enabling configuration activity

**Technical/contextual barriers:**
6. **Adaptation complexity** — Myanmar disease epidemiology, clinical training norms, and diagnostic capacity differ substantially from Spain; localization requires Myanmar expert validation
7. **Infrastructure risk** — Myanmar telemedicine provider reliability, connectivity stability, and integration with clinical workflows is unknown
8. **Safety assurance** — non-specialist clinical decision-making with AI requires explicit oversight model per FAQ Q72–73

**Strategic barriers:**
9. **MOH alignment** — concept does not demonstrate Myanmar MOH endorsement or digital health strategy integration; without this, adoption post-evaluation is uncertain
10. **Portfolio competition** — EVAH will likely receive 100+ applications; the Myanmar concept competes against proposals with confirmed partnerships, established in-country teams, and more established disease areas

### V.E. Strongest Selling Points

1. **Mature technology** explicitly eligible: LLM wrapper validated, award-winning, with real-world acceptance data transferable across geographies per FAQ Q27
2. **IP and commercialization fully compatible**: no open-sourcing required; IDARA can retain AICOMTA IP (FAQ Q64–65); commercialization path compatible with EVAH
3. **Scalable delivery model** via existing telemedicine infrastructure — directly addresses FAQ Q89's requirement for credible integration pathway
4. **International team triangle** — Spanish developers + German evaluators + Myanmar implementers covering all three required consortium functions
5. **Staged strategy validated** — Pathway A → B trajectory explicitly supported by J-PAL FAQ Q35
6. **Equity focus** — rural Myanmar, community health workers, and ethnic minorities in conflict-affected states directly aligns with EVAH's equity priority
7. **Budget headroom** — Pathway A at <USD 1M is lean and value-for-money (FAQ Q44c: reviewers assess commensurateness with scope)

---

## VI. Folder-Specific Recommendations

### VI.A. Scientific Refinement

1. **Add a comparison group strategy to Phase 2.** The FAQ (Q39) is clear that before-after alone is insufficient. Options appropriate for Pathway A:
   - **Matched comparison facilities:** identify 3–5 control PHC centers not receiving AICOMTA; compare adoption outcomes
   - **Interrupted time series:** collect pre-deployment and post-deployment query/decision data; controlled ITS acceptable for implementation research
   - **Waitlist/stepped-wedge design:** deploy in phases; earlier-receiving facilities serve as counterfactual for later-receiving ones
   The choice should be explicitly justified in the evaluation design section citing FAQ Q37.

2. **Reframe Phase 1 as "evaluation-enabling configuration," not product development.** Per FAQ Q50, software adaptation is supported only if necessary to enable the evaluation (configuration, integration, localization, minor modifications). The Myanmar concept should explicitly state: "AICOMTA's core architecture and model are fully developed. Phase 1 activities are limited to evaluation-enabling configuration: translation of the user interface, localization of clinical decision algorithms for Myanmar clinical context, and validation of adapted outputs with Myanmar clinicians — all necessary preconditions for rigorous real-world evaluation."

3. **Specify named study sites at application.** FAQ Q60 states additions after project starts generally require funder approval. The concept should name at least 3 primary care facilities or community health centers (even if preliminary) with rationale for selection (catchment population, frontline worker cadres, connectivity infrastructure, MOH relationship).

4. **Detail the safety monitoring plan.** FAQ Q73 requires description of procedures for identifying and managing harms, incorrect recommendations, and adverse events. Propose: (a) weekly clinician review of AICOMTA recommendations during Phase 2; (b) serious adverse event reporting pathway; (c) safety threshold criteria for pausing deployment; (d) independent clinical safety reviewer role.

5. **Describe the human-in-the-loop model explicitly.** FAQ Q72 requires the evaluation to reflect real-world supervision and accountability structures. Specify: How do frontline workers access AICOMTA? What is the supervisory chain for clinical decisions? How is AICOMTA output presented as support, not directive? Is there a confirmation step before action is taken?

6. **Add a subgroup analysis plan for algorithmic bias.** FAQ Q70 encourages examination of performance across subgroups (gender, age, geography, cadre). The Myanmar concept should propose exploratory analysis of AICOMTA usability and accuracy across: physician vs. community health worker; urban vs. rural; male vs. female patients; Burmese-speaking vs. ethnic minority language users.

### VI.B. Narrative and Funder Alignment

1. **Write a Myanmar health system challenge narrative with data.** The concept note lacks epidemiological grounding for Myanmar. Required elements:
   - Number of primary care facilities; specialist-to-population ratio; specialist access barriers
   - Gastroenterology/endocrinology disease burden in Myanmar PHC (cite MOH data, WHO LMIC data)
   - Current diagnostic capacity limitations; referral failure rates
   - Myanmar MOH digital health strategy alignment (if a national digital health strategy exists, cite it)
   - Why telemedicine is a viable vehicle in Myanmar (infrastructure data: coverage, connectivity, prior adoption)

2. **Explicitly articulate the policy-use pathway.** FAQ Q89 emphasizes decision-relevant evidence. Add a section: "Evidence generated by this Pathway A evaluation will inform Myanmar MOH decisions on: (a) readiness for national telemedicine-integrated CDST deployment; (b) training requirements for frontline workers; (c) whether to commission a Pathway B impact evaluation in the next EVAH round."

3. **Address IP and commercialization proactively.** Given FAQ Q65–66 explicitly permit IP retention and commercialization, the concept can now state clearly: IDARA retains IP; the evaluation generates public-domain evidence; AICOMTA's commercialization plans include equitable pricing for Myanmar public health sector. This turns a previously flagged concern into a strength.

4. **Describe Global and Open Access compliance specifically.** Per FAQ Q61, applications must describe how findings will advance equitable access and be synthesized with other EVAH studies. Commit to: open-access publication of evaluation results; deposition of de-identified evaluation data in a public repository (where local regulations permit); willingness to contribute to EVAH cross-study synthesis.

5. **Address community engagement.** FAQ Q68 strongly encourages stakeholder engagement. Describe planned engagement with: frontline health workers (co-design of adaptation); supervisors and MOH staff (feedback loops); patient representatives (consent process, transparency about AI use).

### VI.C. Eligibility and Compliance Actions (Priority Order)

| Priority | Action | FAQ Reference | Status |
|----------|--------|---------------|--------|
| **CRITICAL** | Identify Myanmar-registered, operationally-active lead organization | Q1–2 | Not done |
| **CRITICAL** | Identify Myanmar-based PI or Project Lead | Q2 | Not done |
| **CRITICAL** | Obtain signed clinical implementation partner letter of support | Q8 | Not done |
| **High** | Specify named study sites (minimum 3) | Q60 | Not done |
| **High** | Add comparison group / counterfactual strategy to evaluation design | Q39 | Not done |
| **High** | Write safety monitoring plan | Q73 | Not done |
| **High** | Write human-in-the-loop description | Q72 | Not done |
| **Medium** | Reframe Phase 1 costs as evaluation-enabling configuration | Q50 | Not done |
| **Medium** | Prepare lead PI and co-PI CVs | Q8 | Not done |
| **Medium** | Write budget narrative with 80% regional fund flow justification | Q45, Q48 | Not done |
| **Lower** | Write algorithmic bias / equity subgroup analysis plan | Q70 | Not done |
| **Lower** | Describe Global and Open Access compliance commitment | Q61 | Not done |
| **Lower** | Describe community engagement plan | Q68 | Not done |
| **Resolved — no action needed** | Open-sourcing / IP conflict concern | Q64–65 | ~~Blocker~~ Resolved |
| **Resolved — no action needed** | Validation geography concern (Spanish data) | Q27 | ~~Blocker~~ Resolved |
| **Resolved — no action needed** | LLM wrapper eligibility | Q29 | ~~Blocker~~ Resolved |
| **Resolved — no action needed** | Ethics approval before submission | Q67 | ~~Blocker~~ Resolved |
| **Resolved — no action needed** | Full detailed budget at application stage | Q44 | ~~Blocker~~ Resolved |

### VI.D. Budget Guidance (Updated)

The budget template is intentionally high-level at application stage (FAQ Q44). The concept note need not provide line-item detail, but must provide a reasonable estimate that reviewers can assess for value-for-money.

| Category | Estimated Range | FAQ Eligibility | Key Consideration |
|----------|----------------|----------------|-------------------|
| Personnel — Myanmar lead | $300–400K (30–40%) | Eligible | PI (30%), co-PI (20%), evaluation manager (50%), data collectors |
| Personnel — International (Spain + Germany) | $100–150K (10–15%) | Eligible (counts toward 20% non-regional cap) | Keep below 20% cap; justify in budget narrative |
| Phase 1: Adaptation configuration | $60–100K | **Limited eligibility** (FAQ Q50) | Frame explicitly as evaluation-enabling localization, not product development |
| Telemedicine licensing / AICOMTA API / Gemini fees | $30–60K | **Eligible** (FAQ Q52–53) | Explicitly cite FAQ Q52–53 in budget narrative |
| Site costs / facility payments | $80–120K | Eligible | Frontline worker time, facility access, safety monitoring infrastructure |
| Travel (international team → Myanmar; Myanmar team → Spain/Germany) | $60–90K | Eligible | Adapt trips; limit international to essential visits |
| Data collection (qualitative tools, transcription, analysis software) | $60–80K | Eligible | Mixed-methods requires qualitative analysis capacity |
| Indirect costs (max 20% of direct) | $80–120K | Eligible up to 20% (FAQ Q51) | Will be finalized with assigned funder |
| **Total estimate** | **~$770K–$1,120K** | Near Pathway A ceiling | If over $1M, reduce Phase 1 scope or trim international personnel |

### VI.E. Reviewer Positioning (Updated with FAQ Insights)

The FAQ's Section 10 (Q84–92) gives explicit guidance on how proposals are scored. Frame the application accordingly:

1. **Open with the health system challenge and policy relevance** (FAQ Q89 emphasizes decision-relevant evidence above innovation). First 3 paragraphs should describe Myanmar's primary care access crisis, the specialist referral gap, and how AICOMTA evaluation evidence will inform MOH decisions.

2. **Demonstrate partnership credibility upfront** (FAQ Q85iii: "lack of credible implementation setting or partnerships" is the third most common rejection reason). The clinical partner letter and named study sites must be referenced in the application narrative itself, not just attached.

3. **Address evaluation readiness explicitly** (FAQ Q85iv: "tool not meeting readiness requirements" is a common rejection reason). Include a paragraph citing AICOMTA's Spanish validation results, expert panel acceptance scores, and award recognition. Reference FAQ Q27 to justify cross-geography applicability.

4. **Describe the comparison strategy early in the methods section** (FAQ Q85ii: "insufficient evaluation rigor" is the second most common rejection reason). State the counterfactual strategy upfront, then justify method choice.

5. **Make the Pathway A → B vision explicit** (FAQ Q35: explicitly encouraged). Add a "Future directions" or "Scale-up pathway" paragraph stating: positive Pathway A results will be used to design and power a Pathway B impact evaluation for submission to a future EVAH round.

6. **Frame AICOMTA's proprietary model as a strength, not a risk.** Cite FAQ Q63–65: proprietary tools are eligible; IP retention is permitted; the evaluation generates public-domain evidence regardless of model ownership. This positions IDARA as a mature commercial partner generating public good evidence, not a conflict-of-interest risk.

### VI.F. Timeline to Submission (Revised)

**Deadline: April 1, 2026. Estimated days remaining: ~14.**

| Week | Priority Actions |
|------|-----------------|
| **Week 1 (Days 1–7)** | Confirm Myanmar lead organization and PI; draft clinical implementation partner letter; identify 3 named study sites; restructure evaluation design to include comparison group |
| **Week 2 (Days 8–14)** | Complete budget narrative (at high level per FAQ Q44); write safety monitoring and human-in-the-loop sections; compile lead PI CV; write Myanmar health system context narrative; internal consortium review |
| **Day 14** | Final review, WizeHive portal submission (note: use alternate browser/incognito if issues; contacts: application_help@povertyactionlab.org; evah@povertyactionlab.org) |

**Assessment:** If the Myanmar lead organization is identified by Day 3–4, submission is achievable and the concept is competitive. AICOMTA's maturity, the FAQ-confirmed eligibility of Spanish validation data and LLM-wrapper architecture, and the explicitly validated Pathway A → B strategy are strong differentiators. The most dangerous remaining risk is evaluation rigor — a mixed-methods design without a comparison group will be vulnerable to rejection reason #2 (FAQ Q85ii).

---

*Analysis completed and updated March 2026 to incorporate `EVAH RFP FAQ_0.pdf` (92 questions, 20 pages). All claims evidence-based and tied to specific documents in the Request-for-Proposals-evah folder. FAQ citations in format (FAQ Q#) throughout.*
