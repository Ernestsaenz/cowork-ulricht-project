# Recent News Impact Analysis for EVAH Grant Application

**Date:** March 22, 2026
**Scope:** January–March 2026 developments affecting the Myanmar/Thailand AI clinical assistant project

---

## Executive Summary

Several major developments in the last three months significantly affect the EVAH application. Some are highly favorable (EVAH launch, growing evidence base for AI CDSTs in LMICs), while others present risks that must be acknowledged and addressed in the proposal (Gemini 2.0 Flash deprecation, USAID funding collapse, ongoing Myanmar instability). This analysis identifies **7 key areas** with actionable implications for the application.

---

## 1. EVAH Initiative Officially Launched (February 20, 2026)

**What happened:** The Gates Foundation, Wellcome Trust, and Novo Nordisk Foundation formally announced EVAH as a $60 million joint initiative at the AI Impact Summit in New Delhi. J-PAL and APHRC confirmed as delivery partners. The RFP opened the same day.

**Impact on project:** **HIGHLY FAVORABLE**
- Confirms the funding opportunity is real and well-resourced
- The high-profile launch signals strong funder commitment and political backing
- Media coverage positions EVAH as a flagship initiative, meaning successful grantees will have high visibility
- The $60M pool and two-pathway structure (A→B progression) confirms long-term funding potential beyond the initial grant

**Action for application:** Reference the initiative's stated goals directly. Align language with funder messaging about "locally-led evaluations" and "responsible AI adoption." Emphasize the Pathway A → Pathway B progression as a strength of the proposal's long-term vision.

**Sources:**
- [Gates Foundation press release](https://www.gatesfoundation.org/ideas/media-center/press-releases/2026/02/ai-impact-health)
- [J-PAL EVAH RFP page](https://www.povertyactionlab.org/initiative/evidence-ai-health-evah-rfp)
- [Wellcome EVAH announcement](https://wellcome.org/insights/articles/evah-new-initiative-generate-evidence-ai-health)
- [Community Jameel announcement](https://www.communityjameel.org/news/community-jameel-congratulates-j-pal-and-partners-on-the-launch-of-a-usd-60m-initiative-to-evaluate-ai-in-health)

---

## 2. Gemini 2.0 Flash Deprecation — CRITICAL TECHNICAL RISK

**What happened:** Google announced that **Gemini 2.0 Flash will be shut down on June 1, 2026**. As of March 6, 2026, the model is only available to existing customers. Google recommends migration to Gemini 2.5 Flash-Lite or the newer Gemini 3.x series.

**Impact on project:** **HIGH RISK — REQUIRES IMMEDIATE ATTENTION**
- AICOMTA's RAG architecture uses Gemini 2.0 Flash as its backbone LLM
- The June 1 shutdown falls **within the first months of any funded project** (earliest start ~July 2026 if awarded promptly)
- Migration to a newer model (Gemini 2.5 or 3.x) is required before or during the project
- This affects cost projections, performance benchmarks, and the technical narrative in the proposal

**Action for application:**
1. **Do NOT present Gemini 2.0 Flash as the production model** — it will be deprecated before the project begins
2. Frame the proposal around a **model-agnostic RAG architecture** that can accommodate newer Gemini versions
3. Include model migration as part of the Phase 1 adaptation work
4. Consider whether Gemini 2.5 Flash-Lite or Gemini 3.1 Flash offers better cost/performance for the Myanmar context
5. This could actually be turned into a **strength**: demonstrate that the architecture is designed for LLM upgradability, which is important for long-term sustainability

**Sources:**
- [Google Gemini API Changelog](https://ai.google.dev/gemini-api/docs/changelog)
- [Gemini 2.0 Flash documentation](https://docs.google.com/vertex-ai/generative-ai/docs/models/gemini/2-0-flash)

---

## 3. Myanmar Political Situation: Sham Elections & Continued Instability

**What happened (Jan–Mar 2026):**
- Military-controlled elections completed in three phases (Dec 28, 2025 – Jan 25, 2026); USDP (junta proxy) won
- Parliament reconvened for first time in 6 years; Min Aung Hlaing expected to transition from commander-in-chief to President
- NUG declared 25 UEC members "terrorists"; resistance groups disrupted elections (79 ACLED-recorded events)
- Inter-resistance tensions: MNDAA-TNLA fighting in Kutkai (mid-March), resolved via ceasefire
- 19 smaller resistance groups formed the **Spring Revolution Alliance**
- A new cybersecurity law (January 2026) further restricts online content and expands surveillance

**Impact on project:** **SIGNIFICANT — MIXED**
- The political situation remains deeply unstable but **is not fundamentally different** from what funders already expect for Myanmar
- The NUG remains operational, which is important since the application must be submitted from an NUG-affiliated entity (Telekyanmar)
- Inter-resistance tensions (MNDAA-TNLA) did not directly affect Telekyanmar's operational areas but signal fragility
- The new cybersecurity law could affect telemedicine operations and data privacy
- The sham elections have not led to any legitimization of the junta internationally

**Action for application:**
- Acknowledge the complex operating environment but frame it as **exactly why this project is needed** — conflict-affected populations have the greatest need for accessible healthcare
- Emphasize Telekyanmar's **proven track record** of operating through 5 years of post-coup chaos
- Address the cybersecurity law in the data governance section
- Note that EVAH explicitly targets LMICs and conflict settings — Myanmar fits the profile

**Sources:**
- [UN News: Myanmar crisis deepens](https://news.un.org/en/story/2026/01/1166866)
- [Human Rights Watch: Myanmar 2026](https://www.hrw.org/world-report/2026/country-chapters/myanmar)
- [Mizzima: NUG on MNDAA-TNLA ceasefire](https://eng.mizzima.com/2026/03/20/32376)
- [BorderLens: Parliament returns](https://www.borderlens.com/2026/03/16/parliament-returns-six-years-after-coup-as-min-aung-hlaing-prepares-presidential-shift/)
- [ACLED: Myanmar elections analysis](https://acleddata.com/report/myanmars-military-elections-will-not-lead-peace-or-improvement-political-crisis)

---

## 4. USAID Funding Collapse — Opportunity and Risk

**What happened:** USAID obligations to Myanmar were cut by **68% between FY2024 and FY2025**, with deeper cuts expected in FY2026. The US had been Myanmar's largest humanitarian donor (25–40% of humanitarian funding). Key impacts:
- 7 of 9 hospitals serving 80,000 refugees near the Thailand-Myanmar border have **closed**
- HIV, TB, and malaria programs severely disrupted
- Global Fund allocations to Myanmar ($173M for 2024–2026) potentially at risk
- UK has also announced ODA cuts (£4.5B in 2026–27)

**Impact on project:** **DOUBLE-EDGED**
- **Risk:** The overall humanitarian and health funding environment for Myanmar is deteriorating, which could affect complementary services the project depends on
- **Opportunity:** The USAID withdrawal creates a massive gap in Myanmar health services that **European and multilateral funders are now motivated to fill** — this is exactly the positioning for Wellcome/Gates/Novo Nordisk
- **Opportunity:** Telekyanmar's diaspora-led, low-cost telemedicine model becomes even more essential when traditional aid channels collapse

**Action for application:**
- Frame the USAID withdrawal as creating an **urgent need** for alternative, sustainable health delivery models
- Position AI-assisted telemedicine as a **force multiplier** that can partially compensate for reduced health worker availability
- Emphasize the **cost-effectiveness** of the telemedicine + AI model vs. traditional clinic-based care
- Note that the European funders behind EVAH are specifically stepping in where US funding has retreated

**Sources:**
- [ReliefWeb: Myanmar implications of US funding freeze](https://reliefweb.int/report/myanmar/myanmar-implications-us-funding-freeze-and-cuts-humanitarian-response-and-health-needs-21-march-2025)
- [Think Global Health: USAID and global health](https://www.thinkglobalhealth.org/article/one-year-post-usaid-global-health-funding-stuck-in-limbo)
- [Atlas Institute: Long-term ramifications of US aid cuts in Myanmar](https://atlasinstitute.org/the-long-term-ramifications-of-us-aid-cuts-in-myanmar-the-social-political-and-humanitarian-consequences-of-washingtons-retrenchment/)
- [Think Global Health: Earthquake and health system collapse](https://www.thinkglobalhealth.org/article/earthquake-pushes-myanmars-health-system-verge-collapse)

---

## 5. March 2025 Earthquake: Lasting Health System Damage

**What happened:** On March 28, 2025, a **7.7-magnitude earthquake** struck central Myanmar (Mandalay, Sagaing, Naypyidaw). Impact:
- 4,430+ fatalities, 6,200+ injuries
- 5 health facilities completely destroyed, 61 partially damaged, 3 hospitals collapsed
- CDC and Public Health Laboratory in Naypyidaw/Mandalay damaged
- 17.2 million people in affected areas
- UN launched $275M addendum to humanitarian response plan

**Impact on project:** **SIGNIFICANT — STRENGTHENS THE CASE**
- The earthquake destroyed physical health infrastructure that **will take years to rebuild**
- Telemedicine becomes even more critical when clinics no longer exist
- The affected areas (Mandalay, Sagaing) overlap with Telekyanmar's service areas
- Disease outbreak risks (cholera, measles) increase demand for clinical decision support

**Action for application:**
- Reference the earthquake as a compounding factor that has further degraded health infrastructure
- Position telemedicine + AI as **resilient health delivery** — not dependent on physical infrastructure
- Note that the earthquake response demonstrated the limits of traditional health service delivery in Myanmar

**Sources:**
- [WHO earthquake response](https://www.who.int/southeastasia/outbreaks-and-emergencies/myanmar-earthquake-response-2025)
- [Think Global Health: Health system collapse](https://www.thinkglobalhealth.org/article/earthquake-pushes-myanmars-health-system-verge-collapse)
- [WEF: Hidden risks revealed](https://www.weforum.org/stories/2025/09/myanmar-earthquake-reveal-hidden-risks/)

---

## 6. Growing Evidence Base for AI CDSTs in LMICs

**What happened (recent publications):**
- **Nature Health (2026):** Study of LLM-based CDST across 16 Kenyan clinics found hallucinations in only 3.4% of encounters and 99% alignment with local guidelines, but **7.8% actively harmful recommendations** — a key safety concern
- **Penda Health study:** Clinicians with AI access made 16% fewer diagnostic errors and 13% fewer treatment errors
- **Frontiers in Digital Health (2026):** Scoping review noted persistent challenges with infrastructure, data quality, and governance in LMICs
- **Gates/OpenAI Horizon1000:** New initiative to deploy AI in 1,000 clinics across Africa starting in Rwanda

**Impact on project:** **FAVORABLE — BUT DEMANDS RIGOR**
- The Kenya safety finding (7.8% harmful recommendations) will be on reviewers' minds — the proposal must address safety monitoring head-on
- The growing evidence validates the approach but raises the bar for evaluation methodology
- Competing initiatives (Horizon1000) show the field is crowding — differentiation matters

**Action for application:**
- Cite the Kenya study to show awareness of safety risks and describe how AICOMTA's specialist-validated knowledge base mitigates this
- Highlight AICOMTA's existing validation data (4.2/5 quality, 87.5% adoption intent) as evidence of readiness
- Differentiate from generic LLM deployments by emphasizing the **RAG architecture with curated medical knowledge base** vs. raw LLM outputs
- Address the 7.8% harmful recommendation rate explicitly and describe safety monitoring protocols

**Sources:**
- [Nature Health: Safety of LLM-based CDST in African primary healthcare](https://www.nature.com/articles/s44360-026-00082-5)
- [Frontiers: Deploying Medical AI in Low-Resource Settings](https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2026.1743634/abstract)
- [WEF: AI bridging healthcare gaps](https://www.weforum.org/stories/2026/02/how-ai-can-help-bridge-healthcare-gaps-worldwide/)

---

## 7. Thailand Academic Partner Landscape

**What happened:**
- **Mae Fah Luang University (Chiang Rai)** is actively expanding cross-border health research with Myanmar, including a Jan 2026 study on Myanmar migrant health-seeking behavior and collaboration with Thailand's Ministry of Foreign Affairs on border health
- **Chulalongkorn University** co-hosted stakeholder meetings on Thailand-Myanmar border health with the National Health Foundation
- **Prince of Songkla University** and **Chiang Mai University** remain active in Southeast Asian global health research

**Impact on project:** **INFORMATIVE FOR PARTNER SELECTION**
- Mae Fah Luang University has the most active Myanmar cross-border health portfolio and is geographically positioned near the border
- Chulalongkorn has institutional prestige and active Myanmar health engagement
- The proposal's Thailand university partner (TBD) should be selected with awareness of these dynamics

**Action for application:**
- If the Thai partner is not yet confirmed, **Mae Fah Luang University** appears to have the strongest operational alignment (border health expertise, Myanmar migrant research, TICA collaboration)
- Chulalongkorn offers prestige and broader institutional resources
- Whichever partner is chosen, reference their Myanmar-related work to strengthen the consortium narrative

**Sources:**
- [Mae Fah Luang: Thai-Myanmar border health cooperation](https://en.mfu.ac.th/en-news/en-news-detail/detail/News/31132.html)
- [NHF: Thailand-Myanmar border health](https://thainhf.org/en/thailand-myanmar-border-health/)
- [PMC: Myanmar migrant health-seeking behavior in Chiang Rai](https://pmc.ncbi.nlm.nih.gov/articles/PMC12892736/)

---

## 8. Myanmar Internet & Digital Infrastructure

**Key data points:**
- 39.8 million internet users (72.5% penetration) as of late 2025
- 62.5 million cellular connections (114% of population)
- Median fixed download speed: 26.9 Mbps
- Affordable mobile data: ~$0.48/GB
- **BUT:** November 2025 submarine cable disruption caused nationwide Wi-Fi outages; continued VPN blocking; new cybersecurity law expands surveillance
- Starlink usage surging (3,000+ smuggled dishes) as the only source of unrestricted internet

**Impact on project:** **MIXED**
- High mobile penetration supports chat-based telemedicine delivery
- Internet disruptions and surveillance are real operational risks
- The cybersecurity law could theoretically affect health data transmission

**Action for application:**
- Design the system for **low-bandwidth, chat-based interaction** (already planned per March 13 meeting)
- Address internet disruption resilience (offline capabilities, asynchronous consultation models)
- Include data encryption and privacy protections in the technical architecture, referencing the regulatory environment

**Sources:**
- [DataReportal: Digital 2026 Myanmar](https://datareportal.com/reports/digital-2026-myanmar)
- [Myanmar Internet Project: Digital oppression quarterly](https://www.myanmarinternet.info/post/quarterly_nov_2025_jan_2026-1)

---

## Summary: Risk/Opportunity Matrix

| Factor | Impact | Risk Level | Opportunity Level |
|--------|--------|------------|-------------------|
| EVAH launch & $60M commitment | Validates funding opportunity | Low | **High** |
| Gemini 2.0 Flash deprecation (June 1) | Requires model migration | **High** | Medium (show adaptability) |
| Myanmar sham elections & instability | Operating environment unchanged | Medium | Medium (justifies need) |
| USAID funding collapse | Health service gaps widen | Medium | **High** (fills vacuum) |
| March 2025 earthquake aftermath | Infrastructure destroyed | Medium | **High** (telemedicine essential) |
| Kenya CDST safety study (7.8% harmful) | Raises safety expectations | Medium | Medium (AICOMTA's RAG approach mitigates) |
| Thai university partnerships active | Informs partner selection | Low | Medium |
| Myanmar internet disruptions | Operational risk | Medium | Low |
| WHO/EU AI regulation trends | Compliance requirements | Low | Low (framework already favorable) |

---

## Top 3 Urgent Actions for the Application

1. **Address Gemini 2.0 Flash deprecation** — reframe the technical narrative around model-agnostic architecture and include migration plan. This is the single most critical technical update needed in the proposal.

2. **Leverage the USAID gap narrative** — position the project as part of the European philanthropic response to the US withdrawal from global health. This aligns perfectly with the funder identities (Wellcome, Gates, Novo Nordisk).

3. **Cite the Kenya safety study** — proactively address the 7.8% harmful recommendation finding and explain how AICOMTA's specialist-validated RAG knowledge base provides an additional safety layer that generic LLM deployments lack.
