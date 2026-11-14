# Agent 02: GPU Marketplaces With Host Programs Other Than Vast.ai (Centralized, Third-Party Supply)

**Scope:** RunPod (Community and Secure Cloud), TensorDock, Clore.ai, QuickPod, Octa.space, Cudo Compute, Hyperbolic, Prime Intellect, Shadeform, SF Compute, plus 2025–2026 entrants that accept third-party hosts (CloudRift, Packet.ai, GPUnex). Vast.ai, Salad and the DePIN networks (io.net, Akash and others) are covered by other agents.
**Research date:** 2026-11-14. Live marketplace data was pulled the same day from public APIs and pages: Clore.ai API, QuickPod public API, Octa CUBE marketplace page, the RunPod GraphQL `gpuTypes` query, and Shadeform's embedded instance catalogue.
**Labels:** **CONFIRMED** means a primary source (a platform doc, a live API or a ToS) that is dated or was pulled 2026-11-14. **SECONDARY** means press, aggregator or competitor content. **ESTIMATE/INFERENCE** means my own calculation or reasoning.

---

## 1. Executive summary

- **RunPod is closed to new hosts.** It stopped onboarding new Community Cloud hosts on **24 Feb 2026** (SECONDARY copy of the RunPod blog post). Its hosting docs now redirect to a security page (CONFIRMED). Secure Cloud partners need a **≥100 kW** deployment, NVIDIA Ampere or newer, T3/T4 facilities, two diverse ISP circuits and due diligence (SECONDARY snippet of the RunPod partner-requirements page). A small LATAM operator cannot get in. RunPod's live prices are still a useful benchmark: Community **4090 $0.34/h, 3090 $0.22/h, 5090 $0.69/h, A100 PCIe $1.19/h, H100 SXM $2.69/h, V100 $0.19–0.23/h** (CONFIRMED, RunPod API, 2026-11-14).
- **Most platforms on the list now require a datacenter and enterprise scale, and most will not take a small LATAM operator:**
  - **Cudo:** at least 5 bare-metal hosts, a renewable-powered N+1 datacenter, a /27 IPv4 block and 10 GbE.
  - **SF Compute:** 8×H100/H200/B200/B300 HGX nodes, Tier III, ≥400 Gbps InfiniBand.
  - **Hyperbolic:** negotiated deals with neoclouds and datacenters only. Its self-serve "Hyper-dOS" supplier path is no longer in its docs.
  - **Prime Intellect:** aggregates other clouds and has no host onboarding.
  - **Shadeform:** Tier 3/4 only. Its new **Flex VMs** self-enrolment (Oct 2026) needs only SSH plus a dedicated IPv4 address, but the Tier 3/4 rule still applies.
  - **TensorDock:** datacenter hosting required, 25% fee, Stripe-only payouts. Its public API returned **zero locations and zero hostnodes** on 2026-11-14, and competitors report it has been near-empty since late 2025.
- **Clore.ai is the only large marketplace still open to individuals with any hardware** (CONFIRMED, live API 2026-11-14):
  - 2,839 servers, **9,707 GPUs**, 897 host accounts; 42% of GPUs rented in the snapshot.
  - Utilization falls to **26%** once you remove one 2,192-GPU V100 fleet that is ~100% rented at about $0.05/GPU-h.
  - **Hosts keep 95% of the listed price on CLORE-paid rentals and 80% on BTC/USDT/USDC-paid rentals.**
  - Median listed prices per GPU-hour: **3090 $0.16 (rented median $0.13), 4090 $0.38 (rented $0.27), 5090 $0.54 (rented $0.50), 3080 $0.18 (rented $0.09)**.
  - Payouts are crypto only. There is no default KYC, and Venezuelan, Brazilian and Argentine hosts are already listed.
- **The CLORE token has collapsed:** **$0.0015, about $0.95M market cap** (CoinGecko, 2026-11-14). The "CLORE reward bonus" is therefore close to worthless. The whole marketplace emission is about 82,000 CLORE/day ≈ **$120/day shared by all hosts**. Set prices in USD; Clore supports USD autopricing and 96% of servers use it.
- **Octa.space (CUBE) is small but usable:**
  - About 148 nodes available, mostly consumer RTX cards, with nodes in Panama, Costa Rica and Argentina.
  - Prices are in USD; providers are **paid in USDC on Base per session, with a 20% platform fee** (ToS effective 30 Jul 2026; an older billing page says 15%).
  - Typical prices: **3090 $0.24/h, 4090 $0.32–0.38/h, 5090 $0.57/h**.
- **QuickPod is open to individuals and pays in fiat, but its demand is tiny:**
  - Hosts keep 80% (90% for early adopters) and are paid weekly by **PayPal, Stripe Connect or Wise**, with a **$5 minimum**.
  - Only **about 19 GPUs listed in total, about 15 occupied** (CONFIRMED, public API).
  - Prices: 3090 $0.18/h, A4000 $0.10/h, 5090 $0.50–0.55/h, V100 SXM2 $0.06–0.14/h.
- **Old datacenter GPUs are close to worthless on these markets:**
  - V100 SXM2: **$0.05/h on Clore**, $0.06–0.14 on QuickPod, $0.19–0.23 on RunPod Community, $0.25 on CloudRift. T4 on Clore: $0.019/h. P40: $0.10/h listed and unrented.
  - A 300 W V100 uses about $0.03–0.06/h of electricity at $0.10–0.20/kWh (ESTIMATE). On Clore it barely covers power.
- **Payouts to Colombia, Ecuador and Venezuela:**
  - Crypto platforms (Clore, Octa, GPUnex) work in all three, subject to sanctions clauses.
  - On Stripe, Ecuador can receive USD through **Global Payouts**; Colombia is COP in **private preview** only; Venezuela is **not supported** (CONFIRMED, Stripe docs).
  - Wise supports local COP payouts; Venezuela is not on Wise's list.

**Ranking for a small LATAM operator with used hardware:**
1. **Clore.ai**: largest open demand, any hardware, crypto payouts work in CO/EC/VE.
2. **Octa.space**: USD pricing and USDC payouts, open to individuals; small but real demand.
3. **CloudRift operator program**: 85% revenue share, consumer and enterprise GPUs including V100, no facility tier stated. Not yet verified for individuals or LATAM payouts.

QuickPod is a useful no-cost secondary listing. Shadeform Flex VMs becomes option #3 if the hardware is colocated in a Tier III facility.

---

## 2. Detailed findings

### 2.1 Who can host: eligibility and 2026 status

| Platform | Open to new hosts in 2026? | Individuals allowed? | Minimum size | Facility / tier | Network / uptime | Evidence |
|---|---|---|---|---|---|---|
| **RunPod Community Cloud** | **No**, closed 24 Feb 2026; existing hosts continue, no shutdown date | Was yes | n/a | n/a | n/a | RunPod blog (SECONDARY copy); hosting docs now redirect (CONFIRMED) |
| **RunPod Secure Cloud** | By application (partners@runpod.io) with due diligence | No, businesses only | **≥100 kW of GPU servers** | T3/T4; 2N power to rack; generator in ≤10 s | 2 diverse circuits; 100 Gbps uplinks; P95 jitter <3 ms; Ampere or newer | RunPod partner-requirements page (SECONDARY snippets, live page redirects) |
| **TensorDock** (Voltage Park since Mar 2025) | Application form still exists; marketplace looks dormant | Yes in principle, after strict vetting | None stated | "All new hardware… must be hosted in a data center" | 1 Gbps per location (up to 40 GPUs); static IP; 99.99% standard; 16 GB RAM, 8 vCPU and 1 TB NVMe per GPU; PCIe 3.0 x16 / 4.0 x8 | Host page (CONFIRMED, undated content); public API empty 2026-11-14 |
| **Clore.ai** | **Yes**, self-serve | **Yes** (HiveOS rigs, home PCs) | 1 GPU | None for container hosting. Bare Metal tier needs Tier 3, a legal entity, 64 threads and 128 GB RAM | ≥100/100 Mbps, <100 ms latency, dynamic IP allowed | Clore docs (CONFIRMED) |
| **Clore Partners** (resale to Vast.ai and other large renters) | Opt-in toggle | Yes | 1 rig | None | ≥100 Mbps; ≥16 threads, ≥32 GB RAM, ≥500 GB SSD, CUDA ≥12.2; 3070/3090/4090/5080/5090/A4000/A5000/A6000 only | Clore docs (CONFIRMED) |
| **Octa.space (CUBE)** | **Yes**, self-serve with an enrolment key | **Yes** | 1 node | None | Preferred: 8 cores, 32 GB RAM, 500 GB disk, RTX 30-series or newer; Ubuntu 26.04 preferred; reliability score; automated fraud checks | Octa docs and ToS 30 Jul 2026 (CONFIRMED) |
| **QuickPod** | **Yes**, self-serve | **Yes** | 1 GPU (CPU-only machines also allowed) | None | Ubuntu 22.04, open port range; reliability shown to renters | QuickPod docs (CONFIRMED) |
| **Cudo Compute** | Formally yes; focus is "data center vendors and service providers" | Effectively no | **≥5 identical bare-metal hosts** | Renewable-powered DC; N+1 power, cooling and network; 24/7 operations | 10 GbE public NIC + 1 GbE management; IPMI; **/27 public IPv4**; 802.1q VLANs; 16+ cores, 64 GB RAM, 2 TB SSD per host | Cudo docs (CONFIRMED, undated); company pivoted to enterprise clusters (homepage 2026) |
| **Hyperbolic** | By application; neoclouds, datacenters and GPU operators | No | Not stated; product line is H100/H200/B200 | Negotiated | Technical diligence and acceptance tests | hyperbolic.ai/suppliers (CONFIRMED 2026) |
| **Prime Intellect** | No host program found; aggregates clouds such as Runpod | No | n/a | n/a | n/a | Docs and FAQ (CONFIRMED) |
| **Shadeform Flex VMs** | **Yes**, self-enrolment by `curl` (launched Oct 2026), about 2-day review | Business questions asked; individuals unclear | Not stated | **FAQ: Tier 3/4 only** | SSH + dedicated IPv4; no BMC needed | shadeform.ai/flex-vms and FAQ (CONFIRMED) |
| **SF Compute** | By contract | No | Reference unit 256 GPUs; 8-GPU HGX nodes only | **Tier III**, N+1 generators | ≥400 Gbps RDMA per node, 2 ISPs, ≥2×100 Gbps uplink, 4 TB NAS per GPU | Cluster Requirements v1/v2 (CONFIRMED) |
| **CloudRift operator program** (new) | Yes, by contact form | Unclear; aimed at "operators" | None stated | None required; partner examples are Tier III / ISO 27001 | Bare-metal Linux or KVM agent | cloudrift.ai/for-operators (CONFIRMED, 2026) |
| **Packet.ai provider program** (new) | Yes, review in 2 business days | Aimed at colocation, Tier 2/3 and DC operators | "1 to thousands of GPUs" | N+1 power ideal | 1 Gbps+, 99%+ uptime, Ubuntu 22.04/24.04, 24–48 h burn-in; **datacenter-grade NVIDIA only** | packet.ai/for-providers (CONFIRMED, 2026) |
| **GPUnex** (new) | Yes, review in 1–3 days | **Yes**, a "Community tier" for individuals with home or office setups | 1 GPU | Community: none; Enterprise: Tier 3+ | Minimum 1 Gbps symmetric, 12 cores, 64 GB RAM, 1 TB SSD; 95% uptime recommended | gpunex.com knowledge base (CONFIRMED, 2026) |

### 2.2 Fees and pricing control

| Platform | Platform fee | Host keeps | Who sets the price |
|---|---|---|---|
| RunPod Community / Secure | Not published | Unknown | RunPod (Community prices are uniform per GPU type) |
| TensorDock | **25% revenue share** | **75%** | Host sets price; "Top Host" tag allows higher pricing. Downtime penalty: 5× (standard) or 10× (top host) the hourly rate per hour of downtime, credited to the customer |
| Clore.ai, on-demand | 10% base fee split 50/50 → **5% charged to host**, plus **15% extra if the renter pays in BTC/USDT/USDC** | **95%** (CLORE-paid) / **80%** (BTC/stablecoin-paid). Up to 97.5% by locking 2M+ CLORE (PoH) and MFP tiers | **Host** (USD autopricing; Price Coach guidance; cap $10,000/day) |
| Clore.ai, spot | 2.5% split → 1.25% to host, plus the same 15% non-CLORE fee | 98.75% / 83.75% | Host |
| Octa.space | **20%** (ToS effective 30 Jul 2026). The billing doc still says 15% | **80%** (85% per the older doc) | **Host** (USD per hour, plus disk and traffic prices) |
| QuickPod | **20%** flat; 10% for early adopters (host id <1000) | **80%** (90%) | **Host** (GPU, CPU, storage, duration) |
| Cudo | Not published | Unknown | **Host** sets per-vCPU, RAM, disk, GPU and IPv4 prices |
| Hyperbolic | Negotiated | Unknown | Negotiated |
| Shadeform Flex VMs | Not published | Unknown | Not stated |
| SF Compute (resale by tenants) | Fixed fee per node-hour + % of sale | Unknown | Order book |
| CloudRift | "85% rev-share" | **85%** (operator, per CloudRift's comparison table) | **Operator** sets SKUs, hourly rates and reserved terms |
| Packet.ai | "Majority of customer-billed revenue after platform fees" | Unknown; tier-based rate cards | Rate cards from Packet; supplier picks channels |
| GPUnex | "Majority" | Unknown | **Provider** (USDC per hour) |

### 2.3 Current customer prices per GPU-hour (USD) and implied host payout

Prices are customer-facing list prices pulled on 2026-11-14 unless noted. "Net" is the implied host payout per GPU-hour at the platform's published share (ESTIMATE). On Clore, the net is 80–95% of the listed price depending on the renter's payment currency.

| GPU | RunPod Community (closed) / Secure | Clore listed median (rented median) → host net | Octa (sample) → net 80% | QuickPod (range) → net 80% | CloudRift → net 85% | Shadeform (cheapest–median, 30+ clouds) | TensorDock (undated "from") → net 75% |
|---|---|---|---|---|---|---|---|
| RTX 3080 | 0.17 / – | 0.18 (0.09) → 0.07–0.08 | 0.20 → 0.16 | 0.03–0.24 → 0.02–0.19 | – | – | – |
| RTX 3090 | **0.22** / 0.50* | **0.16 (0.13)** → 0.10–0.12 | **0.24** (0.20–0.39) → 0.20 | **0.18–0.22** → 0.14–0.18 | – | – | (3090 listed, price n/a) |
| RTX 4090 | **0.34** / 0.89 | **0.38 (0.27)** → 0.21–0.25 | **0.32–0.38** → 0.26–0.30 | 0.10–0.55 (floor 0.27) → 0.22 | **0.45** → 0.38 | 0.40–0.60 | 0.35 → 0.26 |
| RTX 5090 | **0.69** / 1.39 | **0.54 (0.50)** → 0.40–0.48 | **0.57** → 0.46 | **0.50–0.55** (max 1.25) → 0.40–0.44 | **0.65** → 0.55 | 0.65–0.70 | – |
| RTX A4000 | 0.17 / 0.25 | 0.08 (0.08) → 0.07 | – | 0.10 → 0.08 | – | 0.15 | – |
| RTX A5000 | 0.16 / 0.27 | 0.24 (2 listings, unrented) | – | 0.17–0.30 | – | 0.44 | – |
| RTX A6000 | 0.33 / 0.69 | 2 listings (0.05 and 0.42) | – | 0.35–0.40 | – | 0.49–0.57 | (listed) |
| L40S | 0.79 / 1.09 | 1 listing 0.67 (rented) | – | 0.10 (single outlier) | **0.69** → 0.59 | 0.69–1.50 | – |
| A100 80GB | 1.19 (PCIe) / 2.09; SXM 1.39 / 2.19 | 1 listing 0.58 (PCIe); A100 40GB SXM 0.79–1.00 | – | – | – | 1.35–1.50 | ~1.80 (SXM4) → 1.35 |
| H100 | SXM **2.69** / 4.39; PCIe 1.99 / 2.89 | H100 NVL 0.94; H100 0.58 (1 each) | – | 2.50–2.80 | 1.70 (1-month term) | 1.66–2.73 | 2.25 (1.90–2.50 per SECONDARY Jul 2026) → 1.69 |
| V100 16/32GB | **0.19–0.23** / – | **0.05–0.055**, 2,204 rented → ~0.045–0.05 | – | 0.06–0.14 | **0.25–0.28** → 0.21–0.24 | 0.39–2.34 | – |
| T4 | – | **0.019** (32 GPUs, all rented, one Brazilian fleet) | – | 0.10 | – | – | – |
| P40 | – | 0.10 (1 listing, unrented) | – | 0.10 | – | – | – |
| CMP mining cards (30HX–170HX) | – | 0.03–0.30, 4–16% rented | 0.33 (170HX) | 0.05 (30HX) | – | – | – |

\*The RunPod Secure 3090 $0.50 value may be a default placeholder; several GPU types return 0.5 in fields that do not apply to them.

Notes:
- **Cudo supplier pricing guidance** (undated doc, CONFIRMED): average live prices of RTX 3080 $0.07, A4000 $0.29, A5000 $0.52, A6000 $0.78 per GPU-hour.
- **SF Compute** homepage illustration: reserved H100-class $3.00/GPU-h, resale realized $4.29/GPU-h (marketing example).

### 2.4 Clore.ai live marketplace in depth (CONFIRMED, `api.clore.ai/v1/marketplace`, 2026-11-14 ~11:00 UTC)

Prices are per server per day; I divided by GPU count and 24.

| GPU model | GPUs listed | GPUs rented | Rented share | Median list $/GPU-h | Median of rented $/GPU-h |
|---|---|---|---|---|---|
| Tesla V100 SXM2 32GB | 2,212 | 2,204 | 100% (one owner, US) | 0.055 | 0.055 |
| RTX 3070 | 1,076 | 76 | 7% | 0.167 | 0.058 |
| RTX 3080 | 568 | 97 | 17% | 0.179 | 0.086 |
| **RTX 5090** | 546 | 275 | **50%** | 0.542 | 0.500 |
| RTX 5070 Ti | 379 | 68 | 18% | 0.229 | 0.148 |
| **RTX 3090** | 331 | 130 | **39%** | 0.158 | 0.127 |
| RTX 5080 | 309 | 92 | 30% | 0.215 | 0.188 |
| **RTX 4090** | 289 | 52 | **18%** | 0.375 | 0.266 |
| RTX 3060 Ti | 214 | 118 | 55% | 0.053 | 0.049 |
| RTX 3060 | 167 | 69 | 41% | 0.052 | 0.048 |
| RTX PRO 6000 Blackwell | 27 | 15 | 56% | 1.02 | 1.08 |
| **All GPUs** | **9,707** | **4,120** | **42%** (26% excluding the V100 fleet) | | |

What the snapshot shows:
- **Geography (GPUs, rented):** US 2,735 (2,452), RU 2,371 (350), PL 426, UA 385, … **BR 145 (73), AR 140 (50), MX 13, DO 7, CR 4, VE 3 (1)**, CO 0, EC 0. Venezuelan hosts are present, and there are no Colombian or Ecuadorian hosts yet.
- **Supply is in excess:** most consumer SKUs show 7–40% rented, and the median rented price runs 20–50% below the median list price. Renters pick the cheapest offers.
- **Rental status is not clean demand evidence.** Clore keeps a public banned-GPU register for **self-renting** and hardware substitution. It also routes rigs to **Vast.ai and other large renters through "Clore Partners"** with dollar-pegged payouts. Some "rented" capacity may be self-rental (historically done to farm emissions) or resale to Vast. INFERENCE: the 100%-rented V100 and T4 fleets at $0.02–0.05/h look like one of these.
- **Fixed rental terms:** 72 h is the most common minimum rental length (676 servers), then 24 h, 300 h and 48 h.

### 2.5 Payouts, currencies and LATAM eligibility

| Platform | Payout method / currency | Minimum / frequency | KYC | Colombia | Ecuador | Venezuela |
|---|---|---|---|---|---|---|
| Clore.ai | Withdraw CLORE (ERC-20), BTC, USDT/USDC (ERC-20 or BEP-20) | USDT/USDC min **$10**, max $1,000 per withdrawal, $10k/day, $1 fee; CLORE min 200 (~$0.30); instant | Not by default; can be required at any time (ToS §8) | **Yes** (crypto) | **Yes** | **Likely yes.** ToS bars residents of countries under "U.S., EU, or UN embargo or sanctions regime". VE hosts are listed today, but VE is under US sanctions programs, so there is account-freeze risk (INFERENCE) |
| Octa.space | **USDC on Base**, settled per session | None stated | Sanctions/AML screening possible (ToS §2, §8) | Yes | Yes | Likely yes. The ToS bars "comprehensive" sanctions countries; US measures on VE are targeted, not comprehensive (INFERENCE) |
| QuickPod | **PayPal, Stripe Connect, Wise** | **$5**, weekly (Fridays) per docs; the agreement says "no fixed payout schedule" | Through the payout provider | Wise COP: **yes** (CONFIRMED). PayPal: likely (INFERENCE) | Stripe Global Payouts USD: **supported** (CONFIRMED); PayPal likely | **Hard.** Not supported by Stripe or Wise; PayPal VE accounts are limited (INFERENCE) |
| TensorDock | **Stripe Connect only**; TensorDock covers fees above $10k | Withdraw anytime | Stripe onboarding (SSN for US hosts) | Stripe COP is private preview only, so uncertain | Possible through Global Payouts if TensorDock enables it | **No** |
| CloudRift | "Nominated account" after each billing period | Not stated | Not stated | Unknown | Unknown | Unknown |
| Packet.ai | USD direct deposit every 14 days | Not stated | Not stated | Unknown | Unknown | Unknown |
| GPUnex | USDC on Solana, or bank transfer in "supported regions" | Weekly (with a threshold) or monthly | Not stated | Yes (USDC) | Yes | Likely (USDC) |
| Shadeform / Hyperbolic / Cudo / SF Compute | Contractual (B2B invoicing) | Negotiated | Full business due diligence | Needs a company and contract | Same | Very unlikely |

Stripe facts (CONFIRMED, docs.stripe.com, 2026-11-14):
- Self-serve Connect cross-border payouts run only between the US, UK, EEA, Canada and Switzerland.
- Global Payouts supports **Ecuador in USD (wire)** and **Colombia in COP as private preview only**. **Venezuela is absent.**

### 2.6 Supported hardware

| Platform | Consumer RTX | Old datacenter GPUs (V100/P40/T4) | Mining / CMP cards | CPU-only servers | AMD |
|---|---|---|---|---|---|
| Clore.ai | Yes (GTX 10-series and up) | Yes (V100, T4, P4, P40) | **Yes** (CMP 30HX–170HX, P104/P106) | No (GPU marketplace) | No |
| Octa.space | Yes (prefers RTX 30-series or newer) | Listed (Tesla M40 seen) | Yes (CMP 170HX seen) | VPN and CPU-only nodes possible | Yes (marketplace filter) |
| QuickPod | Yes | Yes (P40, T4, V100 seen in pricing) | Yes (CMP 30HX) | **Yes** (CPU pods) | – |
| TensorDock | Yes, but must be in a datacenter | Yes | Explicitly says mining rigs need "significant capital investments to upgrade" | Yes (CPU cloud) | – |
| CloudRift | Yes (4090, 5090, PRO 6000) | **Yes (V100 SXM2/SXM3 listed)** | – | – | Yes (MI350X) |
| GPUnex | Yes (4090, A6000) | Case by case | – | – | – |
| Packet.ai | No ("datacenter-grade NVIDIA") | Not listed | No | No | No |
| Shadeform | Consumer 4090/5090 are sold by some clouds (excesssupply, phyntec, boostrun) | V100 listed by legacy clouds | No | CPU instances exist | – |
| RunPod Secure / Cudo / Hyperbolic / SF Compute | RunPod: Ampere or newer; Cudo: any GPU in compliant DC hosts; Hyperbolic/SF Compute: H100-class only | No (RunPod excludes pre-Ampere; SF Compute HGX only) | No | Cudo yes | RunPod Secure lists MI300X |

### 2.7 Evidence of demand for hosts

| Platform | Demand signal | Read |
|---|---|---|
| RunPod | Sacra estimates **$325M annualized revenue in Sep 2026, up from $100M at end-2025** (SECONDARY). Live stock status: 4090, H200 and PRO 6000 "High". | Strong demand, but it is no longer open to new hosts. |
| Clore.ai | 4,120 of 9,707 GPUs rented (1,916 of 7,515 excluding the V100 fleet); 897 host accounts. | Real but price-depressed demand. The 5090 is the only consumer SKU near 50% rented. Older cards are mostly idle at 7–20%. |
| Octa.space | **148 nodes** listed as available. The 2026 roadmap claims 180,000+ sessions so far. Node pages show lifetime rental counts (a 5090 node: 263 rentals; a 3060 Laptop: 182; many new nodes have fewer than 10). | Small marketplace, frequent short sessions (averages of 2–11 h). |
| QuickPod | About **19 GPUs on 14 machines**, about 15 occupied. Hostnames such as "vastai6/7" and "clore-…" show hosts cross-list. | High occupancy ratio, but an absolute market of a few dollars per hour. Only useful as a secondary channel. |
| TensorDock | Public API returned 0 locations and 0 hostnodes (2026-11-14). Thunder Compute (a competitor, Nov 2026) reports ~6% availability in Oct 2025 and 0% in Nov 2025, with partial recovery. | Treat as dormant. Do not plan on it. |
| Shadeform | About 304 instance types across 30+ clouds. Flex VMs launched Oct 2026 with Spot resale. | Good demand aggregator for datacenter-grade capacity. Terms for small suppliers are unknown. |
| Hyperbolic | $30M Series A-1 (Oct 2026, SECONDARY); hiring a Head of Supply. | Wants large supply blocks, not small hosts. |
| CloudRift / Packet.ai / GPUnex | Marketing claims only ("revenue from Day 5", "sell every GPU up to 2.5×"). Packet.ai labels its 38% utilization figure illustrative. | Unproven. Worth an inquiry, not a business plan. |

---

## 3. Implications for the LATAM used-hardware rental business

1. **The centralized "community" route has mostly closed.** In 2024 a small operator could list on RunPod Community or TensorDock. By late 2026, RunPod has closed new hosts, TensorDock is dormant, and Cudo, Hyperbolic, SF Compute and Shadeform require Tier III datacenters, contracts and, usually, H100-class hardware.

2. **What is left for a garage- or office-scale operator is mostly crypto-paid marketplaces (Clore, Octa, GPUnex) and small fiat ones (QuickPod).** These have the lowest prices in the market. Typical host-net revenue per GPU-hour while rented:

   | GPU | Clore | Octa | QuickPod |
   |---|---|---|---|
   | RTX 3090 | $0.10–0.12 | ~$0.20 | ~$0.14 |
   | RTX 4090 | $0.21–0.25 | $0.26–0.30 | – |
   | RTX 5090 | $0.40–0.48 | ~$0.46 | $0.40–0.44 |
   | V100 | **~$0.05** | – | – |

   Illustrative net monthly revenue per GPU on Clore at the observed snapshot utilization (ESTIMATE):

   | GPU | Net per month |
   |---|---|
   | RTX 3090 | **$29–34** |
   | RTX 4090 | **$28–33** (18% rented) |
   | RTX 5090 | **$146–173** (50% rented) |
   | V100 | **$32–38** (at 100% rented, before power) |

   These figures come before electricity, internet, hardware failures and the operator's time.

3. **The "cheap used servers" thesis runs into price compression on old GPUs.** Pre-Ampere datacenter GPUs (V100, P40, T4) earn $0.02–0.06/h on open marketplaces. CloudRift's $0.25/h V100 price and RunPod's $0.19–0.23/h are the exceptions, and both have restricted supply. A 300 W V100 burns about $0.03–0.06/h at $0.10–0.20/kWh (ESTIMATE). Old datacenter GPUs only make sense with very cheap power and a buyer channel such as CloudRift. Consumer Ampere, Ada and Blackwell cards (3090, 4090, 5090) are the only hardware with a visible rental market. The **5090** shows by far the best demand on Clore.

4. **Clore and Octa price in USD, but their tokens are a risk.** Clore pays in CLORE when renters pay in CLORE (the 95% case). Converting at $0.0015, with a ~$76k/day 24 h trading volume, means slippage and token risk. Prefer USDT/USDC rentals (80% share), or swap immediately. Octa pays USDC on Base, which avoids token risk.

5. **Payout logistics favor Ecuador and crypto rails.**
   - Ecuador is dollarized, and Stripe Global Payouts supports USD wires there.
   - Colombia is workable through Wise (COP), PayPal or crypto.
   - Venezuela is workable only through crypto (Clore, Octa, GPUnex), with sanctions-related account risk.
   - None of the Stripe-only platforms (TensorDock, likely Packet.ai) can reliably pay a Venezuelan host. A US LLC with a US bank account is the usual workaround (INFERENCE; legal and tax review needed).

6. **Infrastructure gate.** Every platform that pays reasonable prices (Shadeform Flex, Packet.ai, CloudRift partners, Clore Bare Metal, TensorDock top hosts) wants or requires:
   - a datacenter or colocation facility (Tier III for Shadeform and SF Compute);
   - a static public IPv4 address;
   - ≥1 Gbps symmetric bandwidth;
   - 99%+ uptime.

   Residential connections in CO/EC/VE (CGNAT, asymmetric uplink, power cuts) qualify only for Clore, Octa, QuickPod and GPUnex Community. A colocated rack in Bogotá, Medellín or Quito changes the platform options far more than the hardware price does.

7. **Fees summary:**

   | Platform | Host keeps |
   |---|---|
   | Clore | 80–95% |
   | CloudRift (claimed) | 85% |
   | Octa | 80% |
   | QuickPod | 80% |
   | TensorDock | 75% |

   Fees are not the main constraint. Utilization and market price are.

### Ranked view: the three most realistic platforms for a small LATAM operator with used hardware

| Rank | Platform | Why | Main risks |
|---|---|---|---|
| **1** | **Clore.ai** | Open to individuals; any NVIDIA hardware, including mining rigs and old datacenter cards; largest open marketplace in scope (9.7k GPUs, ~4.1k rented); USD autopricing; crypto payouts with a $10 minimum work in CO/EC/VE; LATAM peers already earn there (BR, AR, VE). Clore Partners adds resale to Vast.ai with dollar-pegged payouts for 3090/4090/5090/A-series rigs. | Lowest prices in the market (3090 rented median $0.13/h); excess supply; collapsed CLORE token; 15% extra fee on stablecoin-paid rentals; fraud and self-rental environment; KYC can be demanded at any time. |
| **2** | **Octa.space (CUBE)** | Open to individuals, consumer GPUs, USD pricing set by the host, **USDC payouts per session** (no token exposure); LATAM nodes already present (Panama, Costa Rica, Argentina); prices about 50–100% above Clore for 3090/4090. | Small (about 148 available nodes); short sessions; 20% fee; strict anti-fraud locks (two detections = permanent lock); fee documentation is inconsistent (15% vs 20%). |
| **3** | **CloudRift operator program**; alternatively **Shadeform Flex VMs** if colocated in a Tier III DC | CloudRift lists consumer and enterprise GPUs including **V100 at $0.25/h** and 4090 at $0.45/h, claims an 85% revenue share and sets no facility-tier requirement, so it is the best fit for used datacenter servers. Shadeform aggregates 30+ clouds, already sells 4090/5090 capacity, and Flex VMs enrolment needs only SSH plus IPv4. | Neither publishes small-supplier minimums, payout methods or LATAM eligibility, so an inquiry is needed. Shadeform states Tier 3/4 only. |

**Secondary listing:** QuickPod (fiat payouts through PayPal/Wise/Stripe, $5 minimum) costs nothing to add as a second channel, but its whole market is about 19 GPUs. GPUnex Community tier is a similar low-cost secondary option with USDC payouts and unknown demand.

**Not realistic:**
- RunPod: Community closed; Secure needs 100 kW.
- TensorDock: dormant; datacenter and Stripe required.
- Cudo: 5-host minimum, renewable DC.
- Hyperbolic, SF Compute: H100-class contracts.
- Prime Intellect: no host program.
- Clore Bare Metal: Tier 3 plus a legal entity.
- Packet.ai: datacenter-grade GPUs only.

---

## 4. Confidence and gaps

| Item | Confidence | Notes |
|---|---|---|
| RunPod Community closed (24 Feb 2026) | High | Seen in RunPod's own blog content (through a SECONDARY mirror) and in removed hosting docs. The original blog URL now redirects to a cluster page. |
| RunPod Secure 100 kW and other requirements | Medium | Only search snippets of the official page; the live page redirects. |
| RunPod live prices | High | Public GraphQL `gpuTypes`, 2026-11-14. Some fields contain 0.5 placeholders. |
| Clore marketplace numbers and fees | High | Live API and official docs. "Rented" includes possible self-rental and Partner/Vast resale, so true third-party demand is likely lower. |
| CLORE price and market cap | High | CoinGecko API, 2026-11-14. |
| Octa fee (20% vs 15%) | Medium | ToS (30 Jul 2026) says 20%; the billing page says 15%. I used 20%. Only 18 of 148 nodes were parsed for prices (first page of results). |
| QuickPod size | High | Public API. Small enough that a single host changes the picture. |
| TensorDock status | Medium | Empty public API may need authentication for full data; the competitor report is consistent. Host page content is old (2022–2024 text). |
| Shadeform prices | High | Embedded catalogue, 2026-11-14. These are customer prices; Shadeform's cut and Flex VM payout terms are unknown. |
| CloudRift / Packet.ai / GPUnex | Low–Medium | Self-published program pages. No independent utilization data. CloudRift's 85% is from a comparison table and is not contractual. |
| Hyperbolic, Prime Intellect | Medium | Current pages show B2B-only supply. Older self-serve "Hyper-dOS" supplier docs are gone. |
| LATAM payout support | Medium | Stripe and Wise are confirmed. The PayPal country page was blocked (HTTP 403), so PayPal conclusions are INFERENCE. Venezuela sanctions interpretation is INFERENCE and needs legal review. |
| Cudo supplier pricing guidance | Low | Undated doc, likely 2023–2024 values. |

**Process gap:** the session's shared web-search budget ran out partway through, so a few items could not be searched further:
- Shadeform Flex VMs revenue share;
- PayPal coverage for Venezuela and Ecuador;
- independent 2026 reviews of CloudRift and GPUnex host earnings.

A follow-up session could close these by contacting each platform directly (support@shadeform.ai, the CloudRift operator form, partners@runpod.io). This agent did not do that, per the rules.

---

## 5. Sources (all accessed 2026-11-14)

**RunPod**
- RunPod GraphQL API (public `gpuTypes` query): https://api.runpod.io/graphql — live prices
- "An update on the Community Cloud hosting application process", 24 Feb 2026 (mirror): https://www.plushcap.com/content/runpod/blog/runpod-an-update-on-the-community-cloud-hosting-application-process ; original URL https://www.runpod.io/blog/an-update-on-the-community-cloud-hosting-application-process (now redirects)
- RunPod hosting docs (now redirect to the data-security page): https://docs.runpod.io/hosting/overview.md , https://docs.runpod.io/hosting/partner-requirements (snippets via search)
- RunPod docs PR #602 (hosting docs rewrite, merged 1 Apr 2026): https://github.com/runpod/docs/pull/602
- Sacra, RunPod profile (revenue estimates): https://sacra.com/research/runpod

**TensorDock**
- Host page: https://www.tensordock.com/host.html
- Homepage: https://tensordock.com/
- Docs (full text, including the Supplier Hosting Agreement of 26 Mar 2024 and the Downtime policy of 27 Jun 2024): https://docs.tensordock.com/llms-full.txt
- Public API endpoints probed: https://dashboard.tensordock.com/api/v2/locations , https://dashboard.tensordock.com/api/v0/client/deploy/hostnodes
- Voltage Park acquisition (Mar 2025): https://voltagepark.com/blog/voltage-park-acquires-tensordock-expanding-gpu-cloud-services-for-ai-and-machine-learning
- Thunder Compute, "TensorDock alternatives" (competitor, updated 4 Nov 2026): https://www.thundercompute.com/blog/tensordock-alternatives
- Spheron, "TensorDock pricing 2026" (competitor, 23 Jul 2026): https://www.spheron.network/blog/tensordock-pricing-2026/

**Clore.ai**
- Marketplace API: https://api.clore.ai/v1/marketplace
- Host fees: https://docs.clore.ai/for-hosts/host-fees.md
- Pricing guide: https://docs.clore.ai/for-hosts/server-settings/how-to-price-your-servers-for-rental.md
- Network requirements: https://docs.clore.ai/for-hosts/installing-clore-hosting/network-requirements.md
- Deposits and withdrawals: https://docs.clore.ai/getting-started/deposit-withdrawal.md
- Tokenomics: https://docs.clore.ai/main/tokenomics.md
- Clore Partners: https://docs.clore.ai/for-hosts/advanced/clore-partners-high-volume-rental-system-for-major-clients.md
- Bare Metal provider requirements: https://docs.clore.ai/for-hosts/advanced/bare-metal.md
- Banned GPUs: https://docs.clore.ai/for-hosts/list-of-all-banned-gpus.md
- Terms of Service: https://docs.clore.ai/legal/terms-of-service.md
- CoinGecko price API (CLORE, OCTA): https://api.coingecko.com/api/v3/simple/price?ids=clore-ai,octaspace

**Octa.space**
- Marketplace: https://marketplace.octa.space/api/v1/nodes (redirects to the cube.octa.computer marketplace)
- Billing: https://docs.octa.space/billing.md
- Terms and Conditions (effective 30 Jul 2026): https://docs.octa.space/terms-and-conditions.md
- Hardware requirements: https://docs.octa.space/overview.md
- Fraud control: https://docs.octa.space/fraud-control-rules-for-node-owners.md
- 2026 roadmap: https://docs.octa.space/2026-roadmap.md
- Node installation: https://docs.octa.space/node-installation.md

**QuickPod**
- Payouts and taxes: https://docs.quickpod.io/hosting/payouts-and-taxes.md
- Platform fee: https://docs.quickpod.io/hosting/platform-fee.md
- Earnings and payouts: https://docs.quickpod.io/hosting/earnings-and-payouts.md
- Hosting agreement: https://docs.quickpod.io/hosting/hosting-agreement.md
- Machine setup: https://docs.quickpod.io/hosting/machine-setup.md
- Public API: https://api.quickpod.org/swagger/doc.json , https://api.quickpod.org/gpu_distribution , https://api.quickpod.org/gpupricing , https://api.quickpod.org/rentable , https://api.quickpod.org/notrentable

**Cudo Compute**
- Suppliers: https://docs.cudocompute.com/suppliers.md
- Supplier requirements: https://docs.cudocompute.com/suppliers/requirements.md
- Supplier pricing guidance: https://docs.cudocompute.com/suppliers/pricing.md
- Homepage (fetched via WebFetch; direct curl was blocked): https://www.cudocompute.com/
- SemiAnalysis ClusterMAX review (6 Nov 2025): https://clustermax.semianalysis.com/cloudreview/cudocompute

**Hyperbolic**
- Suppliers page: https://hyperbolic.ai/suppliers
- On-demand pricing doc: https://hyperbolic.ai/docs/on-demand/pricing.md
- Partner (referral) program, 11 Aug 2025: https://www.hyperbolic.ai/blog/introducing-hyperbolic-partner-program

**Prime Intellect**
- Compute page: https://www.primeintellect.ai/compute
- FAQ: https://docs.primeintellect.ai/faq.md
- Docs index: https://docs.primeintellect.ai/llms.txt

**Shadeform**
- Homepage (embedded live instance catalogue): https://www.shadeform.ai/
- Flex VMs: https://www.shadeform.ai/flex-vms
- FAQ: https://docs.shadeform.ai/getting-started/faq.md
- Runtime Wire on Flex VMs (20 Oct 2026): https://runtimewire.com/article/shadeform-flex-vms-gpu-marketplace

**SF Compute**
- Cluster Requirements v1: https://sfcompute.com/requirements/clusters/v1
- Cluster Requirements v2: https://sfcompute.com/requirements/clusters/v2
- Reselling guide: https://docs.sfcompute.com/preview/guides/reselling.md
- Homepage: https://sfcompute.com/

**New entrants**
- CloudRift: https://www.cloudrift.ai/for-operators , https://www.cloudrift.ai/pricing
- Packet.ai: https://packet.ai/for-providers
- GPUnex: https://www.gpunex.com/knowledge-base/connecting-your-gpu
- Spheron supplier notes (Nov 2026): https://www.spheron.network/blog/sell-gpu-capacity-to-a-marketplace-onboarding-field-notes-2026/

**Payout rails**
- Stripe cross-border payouts: https://docs.stripe.com/connect/cross-border-payouts.md
- Stripe Global Payouts recipient countries: https://docs.stripe.com/global-payouts/recipient-countries.md
- Stripe recipient requirements: https://docs.stripe.com/global-payouts/recipient-requirements.md
- Wise, sendable countries: https://wise.com/help/articles/2571942/what-countries-can-i-send-to
- PayPal worldwide page: https://www.paypal.com/us/webapps/mpp/country-worldwide (HTTP 403, not used)

Raw downloads and the parsing scripts are in `/tmp/claude-0/-home-user-cowork-ulricht-project/6a906045-5aa8-5271-a0fd-a23952c77e55/scratchpad/agent02/` (untrusted data; parsed with `python3 -I`).
