# AICOMTA-Documentation: Comprehensive Biomedical Research & Funding Analysis

---

## I. Folder Overview

The AICOMTA-documentation folder contains four documents representing the complete research and implementation lifecycle of a Spanish clinical AI assistant project. **AICOMTA (Artificial Intelligence Sharing Talent)** is a retrieval-augmented generation (RAG)-based clinical decision support system designed for primary care physicians to improve coordination with hospital specialists in gastroenterology and endocrinology, developed at the Instituto de Investigación Sanitaria Galicia Sur (IDARA) within the Galician Health Service (SERGAS), led by Dr. Juan Turnes.

**Apparent purpose:** Research archive and funding portfolio for a clinically-governed AI implementation project with dual objectives: (1) validate feasibility and efficacy of AI-assisted clinical decision support in primary care, and (2) demonstrate AI-enabled retrieval of chronic hepatitis C patients lost to follow-up.

**Stage of work:** The folder spans from ethics-approved protocol (2023), through real-world implementation study (draft manuscript, 2024–2025), a peer-reviewed disease-specific outcome paper (published 2025 in *Gastroenterología y Hepatología*), and a grant/award expansion application (Zendal Prize). This indicates a **mature research initiative transitioning from validation to international scale-up**.

---

## II. File Inventory and Categorization

| File Name | Type | Content | Language | Stage |
|-----------|------|---------|----------|-------|
| `Protocolo CEIC COMTA.pdf` | Ethics & clinical protocol | Full CEIC protocol for COMTA project (2023); study design, methods, evaluation framework, informed consent, budget | Spanish | Ethics-approved study design |
| `Borrador paper_v1.0 AICOMTA .docx` | Manuscript draft | Main validation study: 6-month prospective observational mixed-methods study of AICOMTA; usability, satisfaction, response quality | English | Pre-publication draft (near-final) |
| `Memoria AICOMTA Francisco Guitián.pdf` | Published research article | Hepatitis C patient retrieval using AI; published in *Gastroenterología y Hepatología* 2025 | English/Spanish | Peer-reviewed publication |
| `Aicomta premios Zendal (1).pdf` | Grant/award application | Project description for Zendal Prize: objectives, team, Latin American expansion plan, international partnerships | Spanish | Grant-seeking/award application |

### Notable Gaps

- No standalone biosketch/CV files
- No detailed budget for expansion activities
- No letters of institutional support (though referenced)
- No letters of collaboration from international partners (Heidelberg, Colombia)
- No risk mitigation documentation
- No data management plan

---

## III. Scientific and Biomedical Content Analysis

### Disease Area and Clinical Context

The project addresses **healthcare fragmentation between primary care (PC) and hospital care (HC)** across two clinical domains: gastroenterology/hepatology and endocrinology. The documented clinical need is substantial — Porter et al. (2023, cited in `Borrador paper_v1.0`) estimate that PC physicians would need 26.7 hours per day to follow all clinical guidelines.

A secondary disease focus is **chronic hepatitis C (HCV)** elimination, with AI-based identification of patients lost to follow-up in a population of ~300,000 in the Pontevedra health area.

### Patient Populations

| Study | Population | Size |
|-------|-----------|------|
| AICOMTA validation (`Borrador paper_v1.0`) | Primary care physicians, 2 health centers | n=16 physicians; 328 clinical conversations |
| COMTA protocol (`Protocolo CEIC COMTA.pdf`) | PC physicians, 3 health centers | Target n=25 (50% of 46 available) |
| HCV retrieval (`Memoria AICOMTA`) | Residents of Pontevedra/O Salnés | 99 patients identified; 64 retrieved (64.6%) |

### Intervention and Technology

**AICOMTA System Architecture** (from `Borrador paper_v1.0`):

- **Type:** Retrieval-Augmented Generation (RAG) system
- **Base model:** Google Gemini 2.0 Flash (no supervised fine-tuning)
- **Knowledge base:** Spanish clinical guidelines (AEG, AEEH), local SERGAS protocols
- **Embeddings:** multilingual-e5-large (1,024 dimensions)
- **Vector database:** Qdrant (HNSW algorithm)
- **Similarity threshold:** 0.65 cosine similarity; top-10 fragments
- **Generation parameters:** Temperature 0.3, Top-k 40, Top-p 0.9
- **Clinical governance:** Multidisciplinary panel validates all documents before ingestion
- **Distinctive features:** Verified medical authorship, explicit source citation, visual diagnostic algorithms integration

**HCV Retrieval Tool** (from `Memoria AICOMTA`): HEXIN (Herramientas para la Explotación de la Información) — big data and AI algorithms applied to the IANUS electronic health database to identify untreated HCV patients systematically.

### Study Design and Methods

**AICOMTA Real-World Study** (`Borrador paper_v1.0`): Prospective observational mixed-methods study (Nov 2024–Apr 2025). Expert panel of 13 independent evaluators (blinded) assessed 20% random sample of 328 conversations using a five-dimension rubric (scientific accuracy, clinical context, clarity, clinical utility, PC suitability). Compliance with CHART (Chatbot Assessment Reporting Tool) declaration.

**COMTA Protocol** (`Protocolo CEIC COMTA.pdf`): Before-and-after design with cross-sectional evaluations every 6 months (Sept 2023–Aug 2024). Administrative data from hospital systems, surveys, and focus groups (Atlas.ti analysis).

**HCV Retrieval** (`Memoria AICOMTA`): Retrospective identification (2007–2019 data) with prospective follow-up. AI algorithms screened 1,832 anti-HCV+ patients → reduced to 459 untreated → 99 confirmed lost to follow-up → 64 retrieved → 62 treated → 54 SVR (87.1%).

### Key Results

| Metric | Value | Source |
|--------|-------|--------|
| Physician usability score | 4.4/5 | `Borrador paper_v1.0` |
| Global satisfaction | 4.1/5 | `Borrador paper_v1.0` |
| Expert panel quality (overall) | 4.2/5 | `Borrador paper_v1.0` |
| Expert panel scientific accuracy | 4.4/5 | `Borrador paper_v1.0` |
| Trust in AICOMTA recommendations | 87.5% | `Borrador paper_v1.0` |
| Would integrate into routine practice | 87.5% | `Borrador paper_v1.0` |
| HCV patient retrieval rate | 64.6% (64/99) | `Memoria AICOMTA` |
| HCV treatment initiation | 96.88% (62/64) | `Memoria AICOMTA` |
| HCV sustained virological response | 87.1% (54/62) | `Memoria AICOMTA` |

### Strengths and Weaknesses

**Strengths:**

- Strong institutional backing (SERGAS, Galicia Sur Research Institute)
- Real-world validation with genuine clinical conversations (not simulated)
- Clinical governance model (specialist-validated content) is a key differentiator
- Published HCV retrieval results demonstrate concrete health impact
- High professional acceptance despite initial AI skepticism (baseline 3.4–3.5/5 → AICOMTA 4.1–4.5/5)
- Detailed technical transparency enabling reproducibility

**Weaknesses:**

- Small sample sizes (n=16 physicians; n=64 HCV patients)
- No patient-level clinical outcomes measured (only provider acceptance and tool quality)
- Short follow-up (6 months)
- Self-selection bias (voluntary physician participation)
- Endocrinology knowledge base underperforms (3.68/5 vs. 4.49/5 for PC)
- No comparative control group (vs. UpToDate, Clinical Key, etc.)
- Single-region studies (Pontevedra only)
- Organizational barriers identified but unresolved (only 18.8% had sufficient consultation time)

---

## IV. Funding and Grant-Application Analysis

### Current Funding Landscape

| Project | Funding Sources | Amount | Gap |
|---------|----------------|--------|-----|
| COMTA Protocol | AbbVie, Novo Nordisk (via Foundation) | €45,000 secured | ~€28,000 (38% unfunded) |
| AICOMTA validation | AstraZeneca, AbbVie, Novo Nordisk | Not specified | Unknown |
| HCV retrieval | Gilead Sciences FOCUS programme | Not specified | N/A |
| Zendal Prize | Applied | Not specified | Pending |

**Total COMTA budget:** €76,644.75 (with 5% contingency). Personnel costs dominate at 80%.

### Funder Alignment

The project is well-positioned for multiple funding streams: EU Horizon Europe (digital health/AI pillar), Spanish RETOS R&D, ISCIII, WHO/Global Fund (HCV elimination), and continued pharmaceutical partnerships. The Zendal Prize application positions the project for Latin American expansion.

### Submission Readiness

**Not ready for major grant submission** in current state. Missing: biosketches, institutional support letters, international collaboration letters, data management plan, risk mitigation document, detailed Latin American expansion budget, sustainability plan.

**Near publication-ready:** Main AICOMTA validation manuscript (`Borrador paper_v1.0`) is near-final and should be prioritized for high-impact journal submission.

---

## V. Strategic Interpretation

### Project Vision

The project aims to establish AICOMTA as an **innovative, responsible, exportable model** ("modelo innovador, responsable y exportable" — `Aicomta premios Zendal`) for clinical AI governance in primary care, with scale-up to rural Latin America.

### Maturity Assessment

- **Technical maturity:** High — RAG system operational, 328 conversations logged
- **Clinical maturity:** Moderate — acceptance proven; clinical outcomes limited to HCV
- **Publication maturity:** Mixed — 1 peer-reviewed paper; main manuscript in draft
- **Funding maturity:** Moderate — pharma-funded pilots; seeking larger expansion grants

### Biggest Barriers

1. Time constraint paradox: high adoption intent (87.5%) but only 18.8% have sufficient consultation time
2. Endocrinology knowledge base insufficiency
3. Single-center/single-region evidence base
4. No patient-level outcome data
5. Latin American expansion lacks operational detail

### Strongest Selling Points

1. Clinical governance model (specialist-validated, transparent, traceable AI)
2. Real-world validation with high professional trust
3. Concrete HCV elimination impact (64.6% retrieval, higher than European comparators)
4. Health equity positioning for rural/remote populations
5. Reproducible technical architecture

---

## VI. Folder-Specific Recommendations

### Scientific Refinement

1. **Design a comparative effectiveness study** vs. standard clinical resources (UpToDate, Clinical Key)
2. **Conduct a longitudinal patient outcome study** linking AICOMTA use to diagnostic accuracy and health outcomes
3. **Resolve endocrinology underperformance** through expanded knowledge base with dynamic management guidelines
4. **Plan multi-center validation** across different Spanish autonomous communities before international expansion

### Narrative and Positioning

1. **Create a 2–3 page unified project summary** showing COMTA (coordination evaluation) → AICOMTA (clinical governance model) → HCV (proof-of-concept application) → Latin America (next phase)
2. **Clarify COMTA vs. AICOMTA naming** consistently across all documents
3. **Lead with clinical governance** as differentiation, not technical architecture

### Missing Documents (Priority Order)

1. Comprehensive team biosketches (Dr. Turnes, Pérez Cachafeiro, IDARA team)
2. Institutional letters of support (SERGAS, Galicia Sur Research Institute)
3. International collaboration letters (Heidelberg, Colombian partners)
4. Data management and sharing plan (GDPR-compliant)
5. Sustainability and dissemination plan
6. Risk mitigation document
7. Cost-effectiveness analysis

### Budgeting

1. Clarify whether the €28,000 COMTA funding gap was resolved
2. Develop detailed Latin American expansion budget (estimate 1.5–2× initial implementation cost)
3. Calculate cost per physician trained, cost per HCV patient retrieved, and system-level savings

### Translational Framing

1. Reposition as **"clinical governance model for AI in healthcare"** (exportable framework, not just a tool)
2. Frame HCV retrieval as **"AI-enabled disease elimination"** aligned with WHO 2030 targets
3. Emphasize health systems strengthening narrative (workflow integration, organizational change management)
4. Consider releasing de-identified conversation datasets for reproducibility

---

*Analysis completed March 2026. All claims tied to specific documents in the AICOMTA-documentation folder.*
