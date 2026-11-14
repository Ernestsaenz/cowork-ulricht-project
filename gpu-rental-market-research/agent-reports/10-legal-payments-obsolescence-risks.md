# Agent 10: Legal, Payment, Regulatory and Technical-Obsolescence Risks

**Business under study:** buying used servers and GPUs in Colombia, Venezuela or Ecuador, assembling small clusters, and renting them on peer-to-peer and decentralized GPU marketplaces (Vast.ai, SaladCloud, RunPod, TensorDock, Clore.ai, io.net, Akash).
**Research date:** 2026-11-14 (all sources accessed on this date unless noted).
**Disclaimer:** This is desk research, not legal, tax or sanctions advice. Rules change often, and several items below come from secondary sources. Before committing capital, confirm each one with a licensed Colombian, Ecuadorian or Venezuelan tax/customs advisor, and, if any US person or entity is involved, with US sanctions counsel.

**Evidence labels used throughout**

| Label | Meaning |
|---|---|
| **[C]** | Confirmed from a primary or official source (regulator, platform ToS or docs, vendor release notes) read during this research |
| **[S]** | Secondary source (law firm, press, trade publication, forum); plausible but not primary |
| **[E]** | Estimate or inference by this agent |
| **[K]** | Background knowledge not re-verified in this session. The shared web-search budget ran out partway through, so a few items could not be re-checked; each is marked |

---

## 1. Executive summary

- **Venezuela should not host the clusters.** No single factor rules it out, but five risks stack up:
  - **Mining ban.** On 7 May 2026 the Ministry of Electric Energy reaffirmed an "absolute" nationwide ban on crypto mining, enforced by CORPOELEC consumption monitoring, raids and seizures, with a USD 1,000 tip reward in Carabobo [S]. To an inspector, a GPU rental farm looks the same as a GPU mining farm.
  - **Power.** The grid is under formal rationing. Demand hit a record ~15.6 GW in August 2026 against a ~3 GW deficit, and 62.8% of households report daily outages [S]. Outages of that frequency make Vast's >90% reliability bar for verification unrealistic [C/E].
  - **Payouts.** Wise does not operate in Venezuela at all [C]. Stripe has no Venezuela payout route [C]. PayPal lists Venezuela without local-currency withdrawal [C]. In practice this leaves crypto, with token, freeze and enforcement risk.
  - **Sanctions.** OFAC eased many sectors in 2026, but the Government of Venezuela, including state-owned banks and utilities, is still blocked under EO 13884 [C]. Any US person or US LLC in the chain needs GL 35 even to pay CORPOELEC, and must file reports for USD payments [C].
  - **Platform terms.** Clore.ai's ToS excludes anyone in a country "subject to a U.S., EU, or UN embargo **or sanctions regime**". Venezuela is subject to such regimes, so Clore hosting there is arguably excluded [C/E].
- **Colombia and Ecuador are workable on payments.** Vast.ai pays only through Wise or PayPal (no bank, ACH or SWIFT), weekly with a USD 20 minimum [C]. PayPal supports send, receive and withdraw for both countries; Colombia is "cross-border only" [C]. Stripe Global Payouts lists Colombia (COP, private preview) and Ecuador (USD) as recipient countries, and Stripe's stablecoin payouts (US platforms, individuals only) cover both [C]. Stripe Connect cross-border payouts to connected accounts, however, cover only the US, UK, EEA, Canada and Switzerland [C], so Stripe-paying platforms such as TensorDock may not support LATAM hosts [E].
- **Colombia tax.**
  - The corporate rate is 35% in 2026 [S]. A free-trade-zone (zona franca) user pays 20% on export income if it files an internationalization plan [S].
  - Hosting and cloud computing are **excluded from IVA** (art. 476 num. 21 ET; DIAN Concepto 13328 of 1 Oct 2025 and Oficio 13566 of 3 Aug 2026) [C]. "Excluded" means no IVA is charged but input IVA on the hardware is not refundable, unlike an "exempt" export of services under art. 481(c) [E].
  - Export-of-services proceeds do **not** have to be channeled through the formal FX market [S].
  - DIAN Resolution 000240 (24 Dec 2025) brings in OECD CARF crypto reporting from tax year 2026 [S].
- **Ecuador tax and FX.** The economy is dollarized, so there is no FX risk. IVA is 15%, with 0% on qualifying exported services [S]. The **ISD (currency-outflow tax) is 5% in 2026**, with 2.5% only for listed productive tariff lines (Decreto 272) [S]. Export proceeds that are not repatriated can trigger a **presumptive ISD** (art. 156 LRET; about 180 days per an academic source) [S]. Leaving earnings in PayPal, Wise or USDT abroad therefore has a cost.
- **Importing used IT equipment is restricted.**
  - **Colombia:** used machinery and equipment need a **prior import license** from MinCIT's Import Committee [S, from the 2025 official Invest in Colombia guide]. Venezuela-to-Colombia hardware arbitrage would hit this wall.
  - **Ecuador:** the COMEX 009-2022 list bans used clothing, used vehicle parts, used tyres, used vehicles and used or refurbished phones sent by courier [C]. I could not confirm whether used computers (HS 8471/8473) are banned or merely restricted.
- **Technical obsolescence is the biggest threat to an "old hardware" thesis, and it has arrived:**
  - CUDA 13.0 removed compiler and library support for Maxwell, Pascal and Volta [C].
  - **R580 is the last driver branch** for those GPUs; as a Long Term Support Branch it reaches **EOL in June 2028** [C].
  - **PyTorch 2.15 (28 Oct 2026) ships only CUDA 13.2 and 13.4 wheels and needs Turing (sm_75) or newer.** PyTorch 2.14 is the last release with Pascal or Volta wheels [C].
  - **vLLM ≥ 0.20 (April 2026) dropped V100**; the current docs require compute capability 7.5+ [C/S].
  - TensorRT-LLM officially supports only Ampere and newer [C]. FlashAttention-2 needs Ampere or newer [C].
- **Platform hardware floors exclude most "old" kit:**
  - **Salad:** RTX 3060 to RTX 5090 only [C].
  - **RunPod:** Community Cloud is closed to new hosts. Secure Cloud partners need **Ampere or newer** and pass due diligence [S].
  - **Vast verification:** more than 7 GB VRAM per GPU, **more than 2.85 GiB/s PCIe bandwidth per GPU** (rules out x1 mining risers), RAM ≥ 95% of total VRAM, 2 physical cores per GPU, CPU with AVX, **500/500 Mbps wired, public IPv4 with no CGNAT**, Ubuntu Server 22.04+, reliability above 90% [C].
- **Bottom line on hardware [E].** For a 3+ year rental life in 2026, buy **Ampere or newer** (RTX 3090 or 3060 12GB, A4000/A5000/A6000, A10/A40/A100) or Ada. Turing (T4, RTX 2080 Ti, Quadro RTX 8000) is a 2–3 year bet. Pascal and Volta (P40, P100, V100) have roughly 0–18 months of declining, niche demand and a hard driver cliff in June 2028. Old Xeon E5 v1/v2 hosts lack AVX2 (x86-64-v3), so they cannot run RHEL 10 or Ubuntu cloud images built for v3, but they still meet Vast's AVX minimum.

---

## 2. Detailed findings

### A. Payments and sanctions

#### A1. Venezuela: OFAC status in 2026

| Item | Finding | Label / source |
|---|---|---|
| Nature of program | Not a comprehensive embargo. Dealings with the country or people of Venezuela are not prohibited **unless blocked persons or other prohibited conduct are involved**. The Government of Venezuela (GOV), including BCV, PdVSA, entities it owns ≥50% or controls, and people acting for it, is blocked whether or not it appears on the SDN list. | [C] OFAC FAQ 680 (last updated 9 Jan 2023) |
| Executive orders listed | EO 14373 (9 Jan 2026, "Safeguarding Venezuelan Oil Revenue"), 13884, 13857, 13850, 13835, 13827, 13808, 13692 | [C] OFAC Venezuela program page |
| 2026 easing | Sector general licenses for oil and petrochemicals (GL 46E, 47B, 48D, 49B, 50C, 52C), minerals (51D, 54C, 55A), financial services with certain state banks (GL 57, 14 Apr 2026), telecom (GL 24A, 61A, 62), earthquake relief (60A, to 21 Apr 2027). Most recent action: GL 5AA, 4 Nov 2026. Several officials delisted in Oct 2026. | [C] OFAC page; [S] law-firm summaries |
| GL 35 (still in force) | Lets US persons "pay taxes, fees, and import duties to, and purchase or receive permits, licenses, registrations, certifications, and **public utility services** from" the GOV when ordinarily incident to day-to-day operations. **US persons paying the GOV in USD must file semi-annual reports** with OFAC and State. | [C] GL 35 text (5 Nov 2019) |
| GL 61A (27 Aug 2026) | Authorizes supplying goods and services for telecom ("data, telephone, internet connectivity…") in Venezuela, including dealings with CANTV and CONATEL. Report to State within 10 days and every 90 days after. Excludes payments in GOV-issued digital tokens and any China, Russia, Iran, North Korea or Cuba persons. | [C] GL 61A text |
| Practical implications | A US person or US LLC operating in Venezuela must: (a) rely on GL 35 for the CORPOELEC electricity bill (state utility, so GOV) and report USD payments; (b) avoid receiving or sending funds through state-owned banks (Banco de Venezuela, Banco del Tesoro, Banco Digital de los Trabajadores) unless GL 57 covers it (not reviewed in detail); (c) screen counterparties for GOV links. | [E] from FAQ 680 and GL 35 |
| EU sanctions (relevant to a Spanish person or company) | Not re-researched. The EU regime targets listed individuals and arms or internal-repression equipment; it is not a general business ban. | [K] |
| US export controls on GPUs (EAR) | High-end accelerators classified 3A090/4A090 (e.g., A100/H100 class; RTX 4090 is thought to exceed the threshold) need a BIS license for D:5 (arms-embargoed) destinations, which are thought to include Venezuela. Older cards (V100, P40, RTX 3090) appear to fall below the performance thresholds. The foreign-direct-product rule can reach reexports from Colombia or Ecuador. **Verify before moving any modern GPU into Venezuela.** | [K] (search budget exhausted; needs verification) |

#### A2. Marketplace terms: sanctions and payouts

| Platform | Sanctions / country clause | Host payout rails | Venezuela | Colombia / Ecuador | Label / source |
|---|---|---|---|---|---|
| **Vast.ai** | ToS (version 1 Sep 2026): no users in Cuba, Iran, North Korea, Syria, or the Crimea, Donetsk, Luhansk, Kherson or Zaporizhzhia regions, "or any other region subject to comprehensive U.S. embargo". **Venezuela not named.** | **Wise and PayPal** (an older doc also lists Stripe). No direct bank, ACH, wire or SWIFT. USD 20 minimum. Invoices weekly on Friday, paid the next Friday. Host must have a verified, B2B-capable payout account. | Wise does not work in Venezuela, so PayPal is the only listed rail [E] | PayPal yes. Wise not on its unsupported list. | [C] vast.ai/terms; docs.vast.ai/host/payment |
| **RunPod** | ToS bars use by Prohibited Parties, Embargoed Countries, persons controlled by residents of them, **"or the Government of Venezuela"**. | Third-party sites say Stripe Connect, weekly (unverified) | Private Venezuelans not barred by this clause, but see onboarding | **Community Cloud closed to new hosts (2026). Secure Cloud partners need Ampere+ GPUs and due diligence.** | [S] ConductAtlas capture of RunPod ToS (Sep 2026); [S] RunPod docs/blog snippet (published 20 Apr 2026, updated 6 Oct 2026) |
| **TensorDock** | Supplier Hosting Agreement (26 Mar 2024). Uptime-SLA penalties for the host. 10% commission if a host solicits customers off-platform. | **Stripe**: Stripe verifies host identity, and a 1099 is issued above USD 600 a year | Not possible (no Stripe in Venezuela) | Depends on whether TensorDock uses Stripe Global Payouts; plain Connect cross-border does not reach Colombia or Ecuador [E] | [S] TensorDock docs/FAQ snippets |
| **SaladCloud (Chefs)** | Chefs terms (28 Sep 2026): no residents of countries under **comprehensive** US sanctions. One account per person. Running Salad on computers "you do not own or control" needs written permission. Commercial use restricted. | Reward points redeemed on the Salad Storefront: **PayPal transfer**, prepaid cards, gift cards | Not excluded by the terms; PayPal is limited | Yes, via PayPal | [C] salad.com/terms/chefs |
| **SaladCloud hardware** | "NVIDIA RTX-class consumer GPUs, from the RTX 3060 through the RTX 5090" | n/a | n/a | n/a | [C] salad.com FAQ |
| **Clore.ai** | ToS (March 2026): user must not be in, or a national or resident of, "any country subject to a U.S., EU, or UN embargo **or sanctions regime**". KYC/AML at Clore's discretion. | **Crypto: CLORE, BTC, USDT, USDC** | **Arguably excluded**: Venezuela is subject to US and EU sanctions regimes [E] | Allowed | [C] docs.clore.ai/legal/terms-of-service |
| **io.net, Akash** | io.net ToS could not be retrieved. Akash is permissionless (AKT/USDC). | Crypto | Not verified | Not verified | Gap |

#### A3. Payment providers by country

| Provider | Venezuela | Colombia | Ecuador | Label / source |
|---|---|---|---|---|
| **Stripe Connect cross-border** (to connected accounts) | No | No: self-serve only among US, UK, EEA, CA, CH | No | [C] docs.stripe.com/connect/cross-border-payouts |
| **Stripe Global Payouts** (US/UK senders) | Not listed | **Listed: COP (private preview)**; added in the 25 Mar 2026 changelog | **Listed: USD** | [C] docs.stripe.com/global-payouts/…/recipient-countries |
| **Stripe stablecoin (USDC) payouts** | Not listed | **CO listed** | **EC listed** | [C] docs.stripe.com/crypto/crypto-payouts. Private preview; US platforms only; individuals and sole proprietors only, not companies |
| **PayPal** | Send, receive, withdraw; **no local-currency feature** | Send, receive, withdraw; "can only send and receive **cross-border** payments" | Send, receive, withdraw **in local currency (USD)** | [C] developer.paypal.com country-feature page |
| **Wise** | **Unsupported**: cannot log in, register or use a Wise card from Venezuela | Not on the unsupported list | Not on the unsupported list | [C] wise.com/help/articles/2978049 |
| **Payoneer** | Prepaid card reportedly no longer issued to new Venezuelan users (Aug 2025) | Not verified | Not verified | [S] Airtm blog (a competitor) |
| **Binance P2P (VES)** | Active. Binance re-added Banco de Venezuela, Banco del Tesoro and Banco Digital de los Trabajadores, all **state-owned**, as payment methods in April 2026. A bolívar-deposit pilot began 15 Oct 2026. About USD 5.9 bn of P2P volume Jun–Oct 2026 (Ecoanalítica). 3 "binanceros" reportedly arrested for arbitrage (Aug 2026). | n/a | n/a | [S] criptonoticias, diariobitcoin, finanzasdigital |

#### A4. Venezuela workarounds and their risks

| Workaround | How it works | Key risks |
|---|---|---|
| Crypto-paying marketplaces (Clore, io.net, Akash) + USDT, then Binance P2P to VES | Host is paid in crypto and sells USDT peer-to-peer | Clore's ToS sanctions-regime clause [C]. Volatility of CLORE, IO and AKT tokens. **Tether froze about USD 182 m of USDT on Tron in coordination with US authorities (11 Jan 2026)** [S]. Arrests of P2P arbitrageurs (Aug 2026) [S]. P2P counterparties paying through state banks are a problem for any US person [E]. Venezuelan tax: IGTF of about 3% on foreign-currency and crypto payments [K]. |
| Book the payout to a foreign entity or relative while the hardware stays in Venezuela | Wise, PayPal or Stripe account held in Spain, the US or Colombia | Vast and other marketplaces show machine location from the IP address. Misstating location or ownership breaches ToS and risks forfeited earnings [E]. Creates a Venezuelan permanent establishment and tax exposure [E]. A US LLC is a US person: GL 35 applies and USD payments to CORPOELEC must be reported [C]. Banks de-risk Venezuela-linked flows; JPMorgan reportedly froze BlindPay and Kontigo accounts over Venezuela business [S, PYMNTS; unverified date]. |
| Run the cluster in Colombia, use Venezuela only to source hardware | Buy cheap in Venezuela, move to Colombia | **Colombia requires a prior import license for used machinery and equipment** [S]. Venezuelan export formalities [K]. EAR reexport licensing for high-end GPUs [K]. |

#### A5. Spanish or US entity as host, with hardware in LATAM (brief)

| Structure | Pros | Cons |
|---|---|---|
| **Spanish SL as host** | Wise, PayPal and Stripe all available. EU-banked. Credibility with platforms. Spain has tax treaties with Colombia, Ecuador and Venezuela [K]. | Servers in Colombia or Ecuador at the SL's disposal are likely a **permanent establishment** there (OECD Art. 5 commentary on servers) [K]. That means local corporate tax on attributable profit, local accounting and VAT registration, with a foreign tax credit in Spain. Spanish CFC rules may apply if a LATAM subsidiary earns mainly passive income. EU DAC8 crypto reporting since 1 Jan 2026 [K]. A Spanish SL cannot avoid local import, energy and mining rules. |
| **US LLC (foreign-owned)** | Easy Stripe and Wise access. No US tax if there is no US trade or business. | Form 5472 plus pro-forma 1120 each year (USD 25k penalty) [K]. **It is a US person for OFAC**, so every Venezuela dealing needs a GL 35 analysis and screening [C]. The same LATAM permanent-establishment issue applies. |
| **Local company (Colombian SAS / Ecuadorian SAS)** | Cleanest for local power contracts, imports, IVA treatment and insurance | Local tax: Colombia 35% (or 20% in a free-trade zone); Ecuador 25% [K] plus ISD. Payout rails are narrower: PayPal and Stripe Global Payouts for Colombia and Ecuador, Wise status for local business accounts not verified. |

### B. Regulation and tax

#### B1. Venezuela: crypto-mining ban and the "GPU farm looks like a mining farm" risk

| Date | Event | Label / source |
|---|---|---|
| Sep 2020 | Decree 4.196 (Official Gazette 41.969) regulates mining. Miners must register in the RIM (Registro Integral de Mineros) under SUNACRIP. | [S] criptonoticias |
| 2023–2024 | PDVSA-Cripto corruption case; SUNACRIP intervened and restructured | [S] |
| May 2024 | Ministry of Electric Energy orders all crypto mining farms disconnected from the grid. Seizures reported of about 11,000 miners (Carabobo, other states) and 100+ devices in Miranda after joint SUNACRIP, CORPOELEC and police inspections triggered by **high electricity consumption**. | [S] heise, forklog, criptonoticias, oilprice |
| 7 May 2026 | Ministry reaffirms an **"absolute prohibition"** of crypto mining nationwide: special supervision plan, sanctions "with the full weight of the law", confiscations, and a USD 1,000 reward for tips in Carabobo. Owning mining equipment is reportedly not illegal. | [S] criptonoticias (7 May 2026) |
| May 2026 | Press calls SUNACRIP "extinct" while demanding action on illegal farms that worsen Zulia blackouts | [S] La Patilla headline (page blocked, 403) |
| Jun 2026 | National Assembly passes, in first reading, a law opening the power sector to private concessions | [S] MercoPress |
| Aug–Oct 2026 | Formal rationing across most states (Caracas largely spared). Record demand of 15,625 MW (10 Aug 2026). ~3,000 MW deficit. **62.8% of households had daily outages in 2026** vs 37.1% in 2024 (ANOVA). El Niño drought risk. | [S] Rio Times, Reuters via The Star, Al Jazeera (6 Oct 2026), Bloomberg (8 May 2026) |

**Assessment [E].** No rule specifically targets AI or GPU data centers. But the enforcement method is to find unusual, constant electricity draw and then inspect, and to an inspector a GPU rack looks the same as a GPU mining rig. Equipment can be seized first and the dispute settled later. Rationing also means grid power is unavailable for hours a day outside Caracas. Running on diesel generators adds cost, and generators themselves draw attention. **High risk; treat as a deal-breaker for hosting in Venezuela.**

#### B2. Colombia: tax and FX for exported compute services

| Topic | Finding | Label / source |
|---|---|---|
| Corporate income tax | 35% for tax year 2026 | [S] Asuntos Legales, Pérez-Llorca 2026 free-trade-zone guide |
| Free-trade zone (zona franca) | 20% rate on **export** income for industrial users, provided an **internationalization plan** is filed with MinCIT (Ley 2277/2022). 35% on other income. | [S] Asuntos Legales (Aug 2026), El Tiempo, Pérez-Llorca 2026 guide |
| Individuals | Progressive rates up to 39% under the general schedule | [K] |
| IVA: cloud and hosting | **Excluded** under art. 476 num. 21 ET: "Suministro de páginas web, servidores (hosting), computación en la nube (cloud computing)". DIAN says each taxpayer must check its service against the five NIST/MinTIC essential characteristics (on-demand self-service, broad network access, resource pooling, rapid elasticity, measured service). | [C] DIAN Concepto 13328 (1 Oct 2025); [C] Oficio 13566 (3 Aug 2026, published 18 Aug 2026) |
| IVA: export of services | Art. 481(c) ET: services provided in Colombia and used exclusively abroad by non-residents without business in Colombia are **exempt, with refund right**. Requirements in art. 1.6.1.21.15 DUR 1625/2016 (amended by Decreto 456/2021): supporting contract or documents, RUT registration as service exporter. | [S] gerencie, accounter, DIAN oficio 15981/2026 |
| Exclusion vs exemption | If GPU rental counts as cloud computing it is **excluded**: no IVA to charge, but **no IVA refund** on the 19% IVA paid when buying hardware locally. Check whether art. 258-1 ET (IVA on productive fixed assets credited against income tax) can recover part of it. | [E]; art. 258-1 is [K] |
| Withholding | Foreign marketplaces do not withhold Colombian tax. A SAS has to apply special self-withholding of income tax. | [K] |
| FX regime | Export of services is a **free-market operation**, not subject to mandatory channeling (art. 41 Res. Externa 1/2018 lists goods trade, investment and debt as mandatory). Foreign bank accounts need no registration unless used for mandatory-channeling operations. | [S] Banco de la República pages |
| Bank-withdrawal tax (GMF) | 0.4% on bank withdrawals | [K] |
| Crypto | DIAN **Resolución 000240 (24 Dec 2025)** adopts OECD CARF: crypto service providers report users from tax year 2026, first report due end-May 2027, penalties up to 1% of transaction value. The FX regime does not recognize crypto. | [S] Holland & Knight (5 Jan 2026), Valora Analitik, Portafolio |

#### B3. Ecuador: tax and FX

| Topic | Finding | Label / source |
|---|---|---|
| Corporate income tax | 25% general rate. A simplified regime (RIMPE) exists for small businesses, but its fit for this business is unverified. | [K] |
| IVA | 15% since April 2024 | [S] Kintsugi 2026 guide |
| IVA on exported services | 0% (art. 56 num. 14 LRTI). Service exporters can request IVA refunds (SRI procedure on gob.ec). | [S] Consulta tributaria (CCQ 2025); [C] gob.ec SRI procedure exists |
| ISD (currency-outflow tax) | **5% in 2026.** Decreto 272 (30 Dec 2025): 2.5% for tariff lines listed by ministerial agreement (productive sectors), 0% for pharma, all subject to a fiscal cap. Whether servers or GPUs (8471/8473) are listed is unverified. | [S] Primicias, NMS Law (4 Jan 2026) |
| ISD presumption on exports | Art. 156 LRET presumes ISD was incurred when export proceeds are **not brought into Ecuador**; an academic source cites 180 days. The regulation sets specific rules for goods and service exports. | [S] EY alerts, academic thesis; exact current text not retrieved |
| ISD refund for service exporters | Art. 162 LRET plus Tax Policy Committee resolutions (e.g., CPT-RES-2026-001) | [S] NMS Law (12 Apr 2026) |
| FX | Dollarized: no conversion risk, but the ISD charges 5% on money leaving the country | [C/K] |

#### B4. Importing used IT equipment

| Country | Rule | Label / source |
|---|---|---|
| **Colombia** | About 97% of tariff lines need no import license, but **used machinery and equipment need a prior import license** from MinCIT's Import Committee. The legal basis is Decreto 925 of 2013 (art. 14 lists license cases, with Annex 1 subheadings); the Committee checks national production before approving. Registration on VUCE is mandatory. Remanufactured goods get more favorable treatment under the US–Colombia trade agreement. | [S] Invest in Colombia legal guide (2025); [C] trade.gov Colombia guide (published 9 Mar 2026); [S] MinCIT Circular 018/2020; [S] USTR 2014 NTE report |
| **Ecuador** | COMEX Resolution 009-2022 (30 May 2022, plus reforms) sets the **prohibited** list: used clothing and footwear, used vehicle parts, used tyres, used vehicles and motorcycles, and **used or refurbished cell phones via courier**. **Used computers (8471) not confirmed as prohibited**; an INEN-1 conformity certificate may apply. Ecuapass registration required. | [C] trade.gov Ecuador guide (published 2 Sep 2025); [S] elyex; **gap: Annex II not read** |
| **Venezuela** | IVA exoneration on imports of capital goods and IT/telecom goods reportedly withdrawn (Dec 2024). Tariff exemptions withdrawn for 1,200+ goods (Sep 2026). Standard IVA 16%. No used-IT-specific rule found. | [S] PwC Venezuela notes, NTN24; gap |
| **HS codes** | 8471.50 / 8471.41 / 8471.49 (complete servers and processing units), 8471.80 (other units, sometimes used for accelerator modules), 8471.70 (storage), **8473.30 (parts and accessories of 8471 machines, the usual heading for GPUs and graphics cards)**. Classification of GPUs varies by customs authority; get a binding ruling or broker opinion. | [E/K] |

**Implication [E].** Import barriers on used goods help explain how local used markets can be mispriced. They also block the easy fix of importing cheap used US or EU enterprise gear, and they block moving Venezuelan hardware into Colombia. Ecuador's 5% ISD adds to the cost of any hardware bought from foreign sellers.

### C. Technical obsolescence

#### C1. NVIDIA toolkit and driver

| Item | Finding | Label / source |
|---|---|---|
| CUDA 12.9 notice | Maxwell, Pascal and Volta are "feature-complete"; offline compilation and library support to be removed in the next major release | [C] NVIDIA CUDA Features Archive |
| **CUDA 13.0** (Aug 2025 [K]) | **Removed** offline compilation and library support for compute capability < 7.5 (Maxwell 5.x, Pascal 6.x, Volta 7.0/7.2). CUDA 12.x can still build for them. Current toolkit line is 13.4.x. | [C] NVIDIA CUDA Features Archive (13.2–13.4 docs) |
| Last driver branch | **R580** for Maxwell, Pascal and Volta. Last CUDA toolkit for them is 12.x. | [C] NVIDIA "CUDA Toolkit, Driver and Architecture Matrix" |
| R580 support end | **R580 is a Long Term Support Branch with EOL June 2028.** Later branches: R595 (production branch, EOL March 2027), R620 (LTSB, EOL September 2029). After June 2028 there are no security fixes for Pascal or Volta datacenter cards. | [C] NVIDIA "Supported Drivers and CUDA Toolkit Versions" |
| GeForce side | NVIDIA's UNIX deprecation notice: "The release 580 series will be the last to support GPUs based on the Maxwell, Pascal, and Volta architectures." Some reports say GeForce security updates continue to about Oct 2028. | [S] Tom's Hardware, Neowin; the 2028 GeForce date is [K] |
| Turing | No deprecation announced as of Nov 2026. The press calls it the "next candidate". | [S] |
| Vast driver floor | Turing and newer: 595.91.07 (on the 595 branch) or **610.57.04**. Below 7.5 (Maxwell, Pascal, Volta): **580.178.04**, so these hosts are stuck on R580 with a CUDA 12.x ceiling for renters' containers. | [C] docs.vast.ai/host/upgrade-nvidia-driver |

#### C2. Frameworks renters actually use (Nov 2026)

| Stack | Minimum NVIDIA arch / status | Label / source |
|---|---|---|
| **PyTorch 2.8** (2025) | CUDA 12.8/12.9 wheels drop Maxwell and Pascal; CUDA 12.6 wheel keeps them | [C/S] PyTorch dev-discuss #3128, release notes |
| **PyTorch 2.11** (23 Mar 2026) | Volta dropped from cu128. **PyPI default becomes cu130 (Turing+).** Pascal and Volta need the cu126 index. | [C] GitHub release notes; dev-discuss #3290 |
| **PyTorch 2.12** (13 May 2026) | cu126 "legacy" covers sm_50–sm_90 (download.pytorch.org only). cu130 stable and cu132 experimental cover sm_75–sm_120. | [C] dev-discuss #3337 (1 Apr 2026) |
| **PyTorch 2.14** (2 Sep 2026) | **Last release with any CUDA 12.x wheels**, so the last prebuilt support for Maxwell, Pascal and Volta | [C] dev-discuss #3432 (4 Sep 2026) |
| **PyTorch 2.15** (28 Oct 2026, latest) | Wheels: **cu132 (default) and cu134 only**. **Minimum GPU Turing sm_75. NVIDIA driver ≥ 580.** Pascal and Volta users told to pin 2.14 or build from source. | [C] GitHub v2.15.0 release notes |
| **vLLM** | v0.19.x docs: CC ≥ 7.0. **Latest docs: "compute capability 7.5 or higher (e.g., T4, RTX20xx, A100…)".** V100 install fails from **v0.20.0 (≈Apr 2026)**; fallback is ≤0.18.x. Default binaries built on CUDA 12.9; CUDA 13 images need R580+. | [C] docs.vllm.ai (latest, v0.19.1); [S] discuss.vllm.ai (30 Apr 2026) |
| **TensorRT-LLM** | Official: Blackwell, Hopper, Ada (sm89), Ampere (sm80/86). Volta and Turing not listed, so community support only. | [C] TRT-LLM support matrix (page dated 15 Sep 2025) |
| **FlashAttention** | FA2: Ampere, Ada, Hopper; Turing only through a separate "flash-attention-turing" repo. FA3: H100/H800 only. FA4: Hopper and Blackwell. | [C] Dao-AILab/flash-attention README |
| **SGLang** | NVIDIA's NGC SGLang containers (26.02, 26.05) target Hopper and Ampere. No official minimum CC found; FlashInfer is thought to need sm75+. | [C] NVIDIA SGLang release notes; minimum is a gap |
| **Precision features** | bf16 needs Ampere+ (Turing and Volta have fp16 only). FP8 needs Ada or Hopper+. FP4 needs Blackwell. Many 2025–2026 open models ship in bf16 or FP8. | [K] (consistent with the FA2 bf16 note) |

#### C3. Container and template requirements on marketplaces

| Item | Finding | Label / source |
|---|---|---|
| Vast verification image | CUDA **≥ 11.8** self-test (12.6+ on ARM64). Maxwell or newer. **More than 7 GB VRAM per GPU.** All GPUs in a machine must be the same model. | [C] docs.vast.ai/host/verification-stages |
| Host driver vs container CUDA | The host driver sets the maximum CUDA a container can use; renters filter offers by that. CUDA 13 images need R580+. On Pascal and Volta, CUDA 13 user-space libraries have **no kernels**, so PyTorch cu130+ wheels fail with "no kernel image" errors even on R580. | [C] PyTorch 2.15 notes, vLLM docs; [E] for renter behavior |
| Default `pip install torch` | Since 2.11 the PyPI default is CUDA 13.x, Turing+ only. A renter on a P40 or V100 who runs a stock template or plain `pip install` gets a broken environment unless pinned to cu126 and ≤2.14. | [C/E] |

#### C4. Old CPUs and operating systems

| Item | Finding | Label / source |
|---|---|---|
| RHEL 10 | **Minimum x86-64-v3** (AVX, AVX2, BMI1/2, FMA…). Fails with "Fatal glibc error: CPU does not support x86-64-v3" on pre-Haswell CPUs. | [C] Red Hat "Considerations in adopting RHEL 10 – Architectures"; [S] Broadcom KB |
| AlmaLinux 10 | v3 build, plus a separate community x86-64-v2 build | [S] AlmaLinux forums |
| Ubuntu 26.04 LTS | Desktop and server installs **keep the amd64 (v1) baseline**. An amd64v3 variant is optional. **Cloud images are amd64v3 by default** and won't boot on pre-v3 instances. | [C] Ubuntu cloud docs; [S] OMG! Ubuntu (Sep 2026), ServeTheHome |
| Vast host CPU minimum | x86_64 with **AVX**; 2 physical cores per GPU | [C] Vast verification stages |
| Xeon E5 v1/v2 (Sandy/Ivy Bridge) | AVX but **no AVX2**, so x86-64-v2 only. OK for Vast and Ubuntu 22.04/24.04 server. Cannot run RHEL 10 or v3-compiled binaries; containers or CPU code built for AVX2 crash with "illegal instruction". DDR3 and PCIe 3.0. | [E/K] |
| Xeon E5 v3/v4 (Haswell/Broadwell) | AVX2, so v3. **No AVX-512** (introduced with Skylake-SP) and **no AMX** (Sapphire Rapids+). PCIe 3.0 with 40 lanes per socket. Fine as GPU hosts. | [K] |
| PCIe floor | Vast requires **more than 2.85 GiB/s per GPU**. PCIe 3.0 x4 (~3.5 GiB/s effective) barely passes; **x1 mining risers (~0.8–0.9 GiB/s) fail**. | [C] Vast; [E] bandwidth arithmetic |
| RAM floor | System RAM ≥ 0.95 × total VRAM. Example: 8 × RTX 3090 (192 GB VRAM) needs ≥ 183 GB RAM. | [C] Vast |

#### C5. Generation table

Remaining-life figures are **[E] estimates** for this business: how many years a host can expect meaningful paid demand on P2P marketplaces, counted from Nov 2026.

| Hardware generation (examples) | Still rentable in 2026? | Expected remaining rental life | Key reason |
|---|---|---|---|
| Kepler (K80, K40) | **No** | 0 | Last driver R470; below Vast's Maxwell floor; CUDA 11.x only |
| Maxwell (M40 24GB, GTX 980 Ti, Titan X) | Barely: Vast-verifiable, almost no demand | 0–1 yr | No CUDA 13; no PyTorch ≥2.15 wheels; vLLM unsupported; R580 EOL Jun 2028; very low perf per watt |
| Pascal (Tesla P40 24GB, P100 16GB, GTX 1080 Ti 11GB) | Niche only (llama.cpp/GGUF hobby inference, pinned legacy stacks) | **0–1.5 yr** | No tensor cores (P40); PyTorch wheels end at 2.14; vLLM ≥0.20 needs CC 7.5; not on Salad; RunPod needs Ampere+; driver cliff Jun 2028 |
| Volta (V100 16/32GB PCIe/SXM2, Titan V) | Yes, declining fast | **1–1.5 yr** (hard stop Jun 2028) | Dropped by vLLM 0.20 (Apr 2026) and PyTorch 2.15 (Oct 2026); no FA2, no bf16; 32 GB HBM2 still useful for pinned-stack training and fine-tuning |
| Turing (T4 16GB, RTX 2080 Ti 11GB, Quadro RTX 6000/8000 24/48GB, Titan RTX) | Yes | **2–3 yr** | Minimum for PyTorch 2.15, vLLM and CUDA 13; but no bf16, FA2 or FP8; "next" deprecation candidate; Salad requires RTX 3060+ |
| Turing low-VRAM (RTX 2060 6GB, 2070 8GB, GTX 16xx 4–6GB) | Marginal or no | 0–1 yr | ≤7 GB VRAM fails Vast verification (GTX 16xx, 2060 6GB); not on Salad |
| Ampere consumer (RTX 3060 12GB, 3080 10/12GB, **3090/3090 Ti 24GB**) | **Yes** (3090 is a mainstay) | **3–5 yr** | Full modern stack (bf16, FA2, TRT-LLM official); Salad-eligible; no FP8 |
| Ampere pro and datacenter (A4000/A5000/A6000, A10, A40, A100 40/80GB) | **Yes** | **3–5 yr** | Full support; RunPod Secure floor; A100 may need EAR licensing for Venezuela [K] |
| Ada (RTX 4060 Ti 16GB–4090, L4, L40S, RTX 6000 Ada) | **Yes** | **4–6 yr** | FP8; prioritized demand (8×4090 is on Vast's priority list) |
| Hopper / Blackwell (H100, RTX 5090, RTX PRO 6000, B200) | Yes, top demand | 5+ yr | Unlikely to be found cheap in the LATAM used market [E] |
| Old Xeon hosts (E5 v1/v2) | Yes as GPU hosts if AVX, PCIe lanes and RAM rules are met | 2–3 yr | x86-64-v2 only: RHEL 10 and v3 cloud images excluded; PCIe 3.0; DDR3 RAM needed at ≥95% of VRAM |
| Old Xeon hosts (E5 v3/v4) | Yes | 3–4 yr | x86-64-v3 OK; no AVX-512 or AMX (matters little for GPU rental) |

### D. Physical and operational risks (brief)

Mostly [K]/[E]; not re-verified because the search budget ran out.

| Risk | Venezuela | Colombia | Ecuador |
|---|---|---|---|
| Grid reliability | **Severe**: 2026 rationing, record deficit, 62.8% of households with daily cuts [S]. Makes Vast's >90% reliability hard to reach [E]. | Generally reliable in main cities; El Niño rationing risk [K] | **2024 drought rationing of up to ~14 h/day** (Sep–Dec 2024) [K]; hydro-dependent, so it can recur |
| Power quality, surges | Frequent surges on restoration; online UPS and AVR essential [E] | Moderate | High during outage cycles [E] |
| Theft, extortion | High; GPU racks are high-value and portable; the mining crackdown adds a state-seizure risk [E] | Medium–high outside secured facilities; colocation in a Tier III data center or free-trade-zone facility recommended [E] | Rising security problems since 2024 [K] |
| Insurance | Limited market; USD policies exist but claim payout is uncertain; seizure by the state is not insurable [E] | Mature market (all-risk electronic-equipment policies with surge cover usually available) [K] | Available through local insurers; check surge and blackout exclusions [K] |
| Connectivity (Vast: 500/500 Mbps, public IPv4, no CGNAT) | Hard outside a few providers [E] | Symmetric fiber and static IPs available on business plans in major cities [E] | Available in Quito and Guayaquil on business plans [E] |

---

## 3. Implications for the LATAM used-hardware rental business

1. **Exclude Venezuela as a hosting site.** The mining ban, grid rationing, broken payout rails, sanctions friction for any US-linked party, possible exclusion under Clore's ToS, and risk of seizure without recourse together make the expected value negative, however cheap the hardware. At most, Venezuela is a sourcing market, and moving the gear out runs into Colombia's prior-license rule for used equipment and possible EAR reexport limits [E].
2. **Colombia is the strongest base on paper**:
   - Wise and PayPal both work there. These are the only two rails Vast.ai pays through.
   - Exported services face no FX channeling obligation.
   - Hosting and cloud services are IVA-excluded, so there is no IVA invoicing burden but also no refund of IVA paid on hardware.
   - The 35% corporate rate falls to 20% inside a free-trade zone with an internationalization plan.
   - Budget for CARF crypto reporting if paid in crypto.
   - **Plan to buy hardware locally or import it new.** Importing used equipment needs a MinCIT prior license.
3. **Ecuador has no FX risk, but the ISD is a cost.** Hardware bought abroad costs an extra 5% ISD unless its tariff line is on the 2.5% list. Proceeds left abroad can trigger presumptive ISD. Model 5% leakage on both inflows and outflows unless an exporter refund is obtained. Ecuador's 2024 blackout history is a serious uptime risk for Vast reliability scoring.
4. **"Old" GPUs are the weakest part of the thesis.** In Nov 2026 the default renter toolchain (PyTorch 2.15 on CUDA 13.2, vLLM ≥0.20) no longer runs on Pascal or Volta, and NVIDIA ends driver security support for them in June 2028. Any purchase model should:
   - Price Pascal and Volta at scrap-plus value, with ≤18 months of declining utilization.
   - Treat Turing as a 2–3 year asset with known feature gaps (no bf16, FA2 or FP8).
   - Set **Ampere 24 GB (RTX 3090, A5000/A6000-class) as the minimum** for anything meant to earn for 3+ years.
5. **Ex-mining rigs need rework.** The 2018–2022 GPU mining wave left LATAM with RTX 30-series cards on x1 risers, small RAM and weak CPUs. On Vast they will fail the PCIe (>2.85 GiB/s per GPU), RAM (≥95% of VRAM) and CPU (2 cores per GPU) checks. Allow for new motherboards or servers (e.g., used dual-Xeon E5 v3/v4 4U chassis), RAM and SSD: plausibly USD 150–400 per GPU slot [E]. Mixed-model rigs must be split, since Vast needs the same model per machine.
6. **The network requirement may bind before hardware does.** Vast wants 500/500 Mbps wired and a public IPv4 address with no CGNAT. That points to a colocation or business fiber contract, not residential sites, which changes the cost model.
7. **Pick the payout rail per platform:**

   | Platform | Rails | Fit |
   |---|---|---|
   | Vast | Wise or PayPal | Fine for Colombia and Ecuador |
   | Salad | PayPal or gift cards | Consumer, personal-PC model; not built for multi-machine commercial hosting without written permission |
   | TensorDock | Stripe | Verify that a Colombian or Ecuadorian supplier can be onboarded |
   | RunPod | — | Closed to new community hosts |
   | Crypto platforms (Clore, io.net, Akash) | Crypto | Add token volatility and CARF/DAC8 reporting; Clore's ToS sanctions-regime clause matters if the operator or host has any Venezuelan link |

8. **Entity structure.** A Spanish SL as host makes payouts easier but does not remove local permanent-establishment, import, energy or IVA obligations where the servers sit. A local SAS, or the Spanish SL plus a local PE registration, is cleaner. Avoid a US LLC if any Venezuelan activity is contemplated, because it is a US person under OFAC.

---

## 4. Confidence and gaps

| Area | Confidence | Main gaps |
|---|---|---|
| OFAC Venezuela status (structure, GL 35, GL 61A) | **High** (primary texts read) | GL 57 (state-bank financial services) not read; EU regime not re-checked; EAR 3A090 applicability to Venezuela is background knowledge only |
| Marketplace terms and payouts | **Medium–high** for Vast, Salad, Clore (primary); **medium** for RunPod and TensorDock (secondary or snippets) | io.net and Akash terms not retrieved; Payoneer coverage unclear; Wise business-account availability for Colombian and Ecuadorian residents unverified; Vast's own payout-country restrictions not published |
| Venezuela mining crackdown and grid | **Medium** (consistent press, mostly secondary, one specialist outlet) | No Official Gazette text for the May 2026 communiqué; SUNACRIP's legal status unclear |
| Colombia tax and FX | **Medium–high** on IVA cloud exclusion (DIAN primary) and FX; **medium** on free-trade-zone details | Whether DIAN treats P2P GPU rental as "cloud computing"; interaction with art. 481 exemption; Régimen Simple (simplified regime) eligibility not researched |
| Ecuador tax and FX | **Medium** | Exact current art. 156 presumption text and deadline; whether 8471/8473 are on the 2.5% ISD list; income-tax and RIMPE details are background knowledge only |
| Used-goods import rules | **Medium** for Colombia; **low** for Ecuador and Venezuela | Ecuador COMEX 009-2022 Annex II not read; Venezuela rules unknown; GPU HS classification varies by country |
| NVIDIA, CUDA, PyTorch, vLLM, TRT-LLM, FA | **High** (vendor docs and release notes) | SGLang minimum compute capability; GeForce security-update end date (~Oct 2028) unverified |
| Physical, insurance | **Low** (background knowledge) | No insurer quotes; no crime statistics gathered |

**Process note.** The shared web-search budget ran out partway through this research. Items marked [K] could not be re-verified and should be checked before use. Re-running searches on: R580 GeForce security end date, Ecuador used-goods annex, io.net and Akash terms, Colombian Régimen Simple, Ecuador corporate rate and RIMPE, and EAR 3A090 for Venezuela would close most gaps.

---

## 5. Sources (all accessed 2026-11-14)

**Sanctions (US Treasury / OFAC)**
- OFAC Venezuela-related sanctions program page (EOs, GL list, recent actions incl. GL 5AA 4 Nov 2026): https://ofac.treasury.gov/sanctions-programs-and-country-information/venezuela-related-sanctions
- OFAC FAQ 680 (updated 9 Jan 2023): https://ofac.treasury.gov/faqs/680
- OFAC Venezuela GL 35 (5 Nov 2019): https://ofac.treasury.gov/media/25961/download?inline
- OFAC Venezuela GL 61A (27 Aug 2026): https://ofac.treasury.gov/media/936841/download?inline
- Agora LatAm, "OFAC Venezuela Sanctions: October 2026 Changes": https://www.agoralatam.com/insights/ofac-venezuela-sanctions-october-2026-update
- Mayer Brown on GL 46 (Jan 2026): https://www.mayerbrown.com/en/insights/publications/2026/01/ofac-issues-new-general-license-authorizing-established-us-companies-to-engage-in-trade-of-venezuelan-oil-and-related-activities
- Baker McKenzie on governing-law removal and telecom GLs: https://sanctionsnews.bakermckenzie.com/ofac-removes-the-us-governing-law-condition-from-the-venezuela-general-licenses-and-issues-new-authorizations-related-to-telecommunications-and-coal/

**Marketplace terms and docs**
- Vast.ai Terms of Use (version 1 Sep 2026): https://vast.ai/terms
- Vast.ai host payouts: https://docs.vast.ai/host/payment.md
- Vast.ai verification stages: https://docs.vast.ai/host/verification-stages.md
- Vast.ai NVIDIA driver minimums: https://docs.vast.ai/host/upgrade-nvidia-driver.md
- Vast.ai hosting overview: https://docs.vast.ai/documentation/host/hosting-overview
- RunPod ToS provision (ConductAtlas capture): https://conductatlas.com/platform/runpod/runpod-terms-of-service/provision/CA-P-052116/prohibited-party-and-embargoed-country-access-ban/
- RunPod blog, community cloud hosting update (pub. 20 Apr 2026, upd. 6 Oct 2026): https://www.runpod.io/blog/an-update-on-the-community-cloud-hosting-application-process
- TensorDock Supplier Hosting Agreement: https://docs.tensordock.com/legal-information/supplier-hosting-agreement
- Salad Chefs terms (28 Sep 2026): https://salad.com/terms/chefs ; Salad homepage FAQ: https://salad.com/
- Clore.ai Terms of Service (March 2026): https://docs.clore.ai/legal/terms-of-service

**Payment providers**
- Stripe Connect cross-border payouts: https://docs.stripe.com/connect/cross-border-payouts
- Stripe Global Payouts recipient countries: https://docs.stripe.com/global-payouts/send-money/recipient-countries
- Stripe changelog, Colombia added (25 Mar 2026): https://docs.stripe.com/changelog/dahlia/2026-03-25/cross-border-payouts-new-countries
- Stripe stablecoin payouts for Connect: https://docs.stripe.com/crypto/crypto-payouts
- PayPal Payouts country/feature support: https://developer.paypal.com/docs/payouts/standard/reference/country-feature/
- Wise, "Which countries can I use Wise in": https://wise.com/help/articles/2978049/which-countries-can-i-use-wise-in
- Airtm, Payoneer in Venezuela (Aug 2025): https://www.airtm.com/en/blog/economy/payoneer-in-venezuela
- Diario Bitcoin, Binance re-adds Banco de Venezuela to P2P: https://www.diariobitcoin.com/criptomonedas/binance-reincorpora-al-banco-de-venezuela-en-su-p2p-y-suma-nuevas-entidades-bancarias/
- Finanzas Digital, Binance P2P vs BCV (Ecoanalítica): https://finanzasdigital.com/mercado-p2p-binance-moviliza-83-por-ciento-divisas-bcv-ecoanalitica/
- CryptoActu, arrests of "binanceros": https://cryptoactu.com/venezuela-3-binanceros-arretes-arbitrage/

**Venezuela mining and grid**
- CriptoNoticias, absolute ban reaffirmed (7 May 2026): https://www.criptonoticias.com/comunidad/venezuela-mantiene-veto-absoluto-a-la-mineria-de-bitcoin-y-anuncia-medidas/
- Heise (May 2024): https://heise.de/-9724437 ; ForkLog seizures: https://forklog.com/en/venezuela-seizes-more-than-100-bitcoin-mining-devices/ ; Bitcoin.com 11,000 miners: https://news.bitcoin.com/venezuelan-authorities-announce-bitcoin-mining-ban-confiscate-over-11000-miners-to-face-the-nations-energy-crisis
- La Patilla (26 May 2026, headline only): https://lapatilla.com/2026/05/26/exigen-identificar-a-responsables-de-granjas-bitcoin-ilegales-que-agravan-los-apagones-en-zulia/
- Rio Times, rationing and demand records: https://www.riotimesonline.com/venezuela-power-rationing-round-industry-2026/ ; https://www.riotimesonline.com/venezuela-electricity-demand-eight-year-high-2026/
- Al Jazeera (6 Oct 2026): https://www.aljazeera.com/amp/news/longform/2026/10/6/we-are-desperate-venezuelas-power-cuts-fuel-growing-public-anger
- Bloomberg (8 May 2026): https://www.bloomberg.com/news/articles/2026-05-08/venezuela-s-faulty-power-grid-risks-derailing-economic-comeback
- MercoPress (4 Jun 2026): https://en.mercopress.com/2026/06/04/venezuela-moves-to-open-its-power-sector-to-private-investment-after-years-of-blackouts
- Reuters via The Star (13 Aug 2026): https://www.thestar.com.my/news/world/2026/08/13/beaten-venezuelans-brace-for-more-severe-power-water-cuts-as-el-nio-looms

**Colombia tax, FX, customs**
- DIAN Oficio/Concepto 13566 (3 Aug 2026): https://normograma.dian.gov.co/dian/compilacion/docs/oficio_dian_13566_2026.htm
- DIAN Oficio 13328 (1 Oct 2025): https://normograma.dian.gov.co/dian/compilacion/docs/oficio_dian_13328_2025.htm
- DIAN Oficio 15981 (2026), exports between related parties: https://normograma.dian.gov.co/dian/compilacion/docs/oficio_dian_15981_2026.htm
- Gerencie, IVA exemption on export of services: https://www.gerencie.com/exencion-del-iva-en-la-exportacion-de-servicios.html
- Asuntos Legales, free-trade-zone rate (Aug 2026): https://www.asuntoslegales.com.co/consultorio/como-quedo-la-tarifa-de-renta-para-usuarios-de-zonas-francas-3735567
- Pérez-Llorca, Guía de Zonas Francas 2026: https://www.perezllorca.com/wp-content/uploads/2026/04/Guia-de-Zonas-Francas-2026.pdf
- Banco de la República, cuentas de compensación: https://banrep.gov.co/politica-monetaria-cambiaria/regulacion-operaciones-cambiarias/generalidades-cuentas-compensacion
- Holland & Knight on DIAN crypto reporting (5 Jan 2026): https://www.hklaw.com/en/insights/publications/2026/01/la-dian-busca-regular-el-reporte-de-informacion-sobre-criptoactivos
- Valora Analitik on Res. 000240: https://www.valoraanalitik.com/criptoactivos-en-colombia/
- Invest in Colombia legal guide ch. 4 (2025): https://investincolombia.com.co/sites/default/files/2025-07/chap-4-foreign-trade-and-customs.pdf
- MinCIT Circular 018/2020 (Decreto 925/2013 license regime): https://normograma.invima.gov.co/compilacion/docs/circular_mincomercioit_0018_2020.htm
- trade.gov Colombia import requirements (published 9 Mar 2026): https://www.trade.gov/country-commercial-guides/colombia-import-requirements-and-documentation

**Ecuador tax, customs**
- NMS Law, Decreto 272 ISD 2026 (4 Jan 2026): https://nmslaw.com.ec/blog/2026/01/04/ecuador-tarifa-diferenciada-isd-2026/
- NMS Law, ISD refunds for exporters (12 Apr 2026): https://nmslaw.com.ec/blog/2026/04/12/condiciones-devolucion-isd-ecuador-exportadores-habituales/
- Primicias, ISD 2026: https://www.primicias.ec/economia/daniel-noboa-decreto272-tarifa-isd-impuesto-salida-divisas-vigencia2026-112835/
- SRI procedure, IVA refund for service exporters: https://www.gob.ec/sri/tramites/devolucion-impuesto-al-valor-agregado-iva-exportadores-servicios
- SRI procedure, ISD refund for service exporters: https://www.gob.ec/sri/tramites/devolucion-impuesto-salida-divisas-exportadores-servicios
- Kintsugi Ecuador VAT guide 2026: https://trykintsugi.com/sales-tax-guides/latam/ecuador
- trade.gov Ecuador prohibited/restricted imports (published 2 Sep 2025): https://www.trade.gov/country-commercial-guides/ecuador-prohibited-and-restricted-imports
- COMEX Res. 009-2022: https://www.gob.ec/regulaciones/resolucion-comex-no-009-2022

**Venezuela customs/tax**
- PwC Venezuela, IVA exoneration note (Jan 2026): https://www.pwc.com/ve/es/assets/documentos/stl/NAC-Exoneracion-IVA-Decreto-5207-Ene2026.pdf
- NTN24, tariff exemptions withdrawn (Sep 2026): https://www.ntn24.com/noticias-economia/regimen-venezolano-retira-exoneracion-de-aranceles-a-mas-de-1-200-bienes-importados-396840

**NVIDIA, CUDA, drivers**
- NVIDIA CUDA Features Archive: https://docs.nvidia.com/cuda/cuda-features-archive/index.html
- NVIDIA CUDA Toolkit/Driver/Architecture matrix: https://docs.nvidia.com/datacenter/tesla/drivers/cuda-toolkit-driver-and-architecture-matrix.html
- NVIDIA Supported Drivers and CUDA Toolkit Versions (R580 EOL Jun 2028): https://docs.nvidia.com/datacenter/tesla/drivers/supported-drivers-and-cuda-toolkit-versions.html
- NVIDIA driver lifecycle: https://docs.nvidia.com/datacenter/tesla/drivers/driver-lifecycle.html
- Tom's Hardware, R580 last for Maxwell/Pascal/Volta: https://www.tomshardware.com/pc-components/gpu-drivers/nvidia-to-axe-maxwell-pascal-and-volta-gpus-with-end-of-driver-support-580-series-drivers-will-be-the-last-to-support-gtx-900-and-1000-cards

**Frameworks**
- PyTorch releases (2.10–2.15 dates): https://github.com/pytorch/pytorch/releases ; v2.15.0: https://github.com/pytorch/pytorch/releases/tag/v2.15.0
- PyTorch dev-discuss #3432 (4 Sep 2026): https://dev-discuss.pytorch.org/t/notice-cuda-12-6-wheels-will-no-longer-be-published-from-pytorch-2-15-drops-maxwell-pascal-volta/3432
- PyTorch dev-discuss #3337 (1 Apr 2026): https://dev-discuss.pytorch.org/t/introducing-cuda-13-2-and-deprecating-cuda-12-8-release-2-12/3337
- PyTorch dev-discuss #3290 (2.11 Volta drop): https://dev-discuss.pytorch.org/t/dropping-volta-support-from-cuda-12-8-binaries-for-release-2-11/3290
- PyTorch dev-discuss #3128 (2.8 Maxwell/Pascal drop): https://dev-discuss.pytorch.org/t/cuda-toolkit-version-and-architecture-support-update-maxwell-and-pascal-architecture-support-removed-in-cuda-12-8-and-12-9-builds/3128
- vLLM GPU install (latest): https://docs.vllm.ai/en/latest/getting_started/installation/gpu/ ; v0.19.1: https://docs.vllm.ai/en/v0.19.1/getting_started/installation/gpu/
- vLLM forum, V100 on 0.20 (30 Apr 2026): https://discuss.vllm.ai/t/support-for-v100-sm-70-on-vllm-0-20/2605
- TensorRT-LLM support matrix: https://nvidia.github.io/TensorRT-LLM/reference/support-matrix.html
- FlashAttention README: https://github.com/Dao-AILab/flash-attention
- NVIDIA SGLang container release notes 26.05: https://docs.nvidia.com/deeplearning/frameworks/sglang-release-notes/rel-26-05.html

**CPUs / OS**
- Red Hat, RHEL 10 architectures: https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/considerations_in_adopting_rhel_10/architectures
- Red Hat developer blog on x86-64-v3 (Jan 2024): https://developers.redhat.com/articles/2024/01/02/exploring-x86-64-v3-red-hat-enterprise-linux-10
- Broadcom KB (RHEL 10 fails on pre-v3 CPUs): https://knowledge.broadcom.com/external/article/411056/rhel-10-installation-fails-with-fatal-gl.html
- Ubuntu cloud architecture variants: https://ubuntu.com/cloud/public-cloud/docs/all-clouds-explanation/architecture-variants/
- OMG! Ubuntu, amd64v3 ISOs (Sep 2026): https://omgubuntu.co.uk/2026/09/ubuntu-amd64v3-iso-downloads
