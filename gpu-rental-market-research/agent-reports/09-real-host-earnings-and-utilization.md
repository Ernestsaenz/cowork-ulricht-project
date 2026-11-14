# 09 — What GPU hosts actually earn: first-hand reports, utilization, ROI, competition, location

**Agent:** 09 of 10 · **Date of research:** 2026-11-14 · **Scope:** realised host earnings, utilization by GPU class, ROI trend, location effects (with LATAM focus), and operational pain points on peer-to-peer and decentralized GPU marketplaces.

**Labels used throughout**
- **CONFIRMED:** primary, dated data. This means either my own capture of a platform's public API, or a platform's own published rate table.
- **ANECDOTE:** a first-hand host report (self-reported, not audited).
- **ESTIMATE:** modelled numbers, mine or third-party.
- **LOW-CRED:** a third-party "review" or SEO page whose numbers are unsourced or internally inconsistent.

> **Method note (important for weighting the evidence)**
> - Reddit was not reachable from this environment. Both the WebFetch and WebSearch tools refuse reddit.com, and direct JSON requests to reddit.com and old.reddit.com were blocked (403 or empty). So **no r/vastai, r/LocalLLaMA or r/homelab threads could be read directly.** I did not use third-party Reddit archives.
> - The shared WebSearch budget (200 calls for all 10 agents) ran out partway through this task. Topics I could not search afterwards are listed in §4.
> - To compensate, I collected **primary market data**:
>   - The public Vast.ai offer-search API (no account needed). A full snapshot of 7,394 offers, 4,400 machines and 13,361 GPUs was captured on 2026-11-14 at 12:07–12:13 UTC, a Saturday. A second snapshot about 15 minutes later is used for stability (§2.3).
>   - Akash's public console API.
>   - Salad's published host rate table.
>   - Hashrate.no's Vast occupancy tracker.
>   - Vast's own host documentation.
> - Many "how much can you earn" pages ranking in search are affiliate or SEO content with made-up or inconsistent figures. They are flagged LOW-CRED and are not used for the conclusions.

---

## 1) Executive summary

- **The platform is busy, but the money goes to verified, well-connected, multi-GPU hosts (CONFIRMED, my Vast API snapshot, 2026-11-14).**
  - About **72% of the GPUs listed on Vast.ai were occupied** at snapshot time: 9,605 of 13,361. Hashrate.no independently shows **74.2%**.
  - **Verified machines: 79% occupied. Unverified or deverified: 49%.**
  - Reliability ≥0.99: **78%**. Reliability 0.95–0.98: **53%**. Reliability 0.90–0.95: **44%**.
  - Upload <100 Mbps: **58%**. Upload ≥1 Gbps: **77%**.
- **Realised first-hand earnings in 2026 are modest (ANECDOTE).**
  - Verified RTX 4090: about **$6/day, ~$180/month gross** (RedPandaMining, May 2026).
  - Verified RTX 5090: about **$9/day, ~$270/month gross** (same source).
  - The same 4090 **unverified, at the same price, earned about $0.05/day.**
  - A new host with **5× RTX 5090 earned about $230 in 23 days in total**, roughly **$60 per GPU-month**, while unverified because upload was below 100 Mbps (bytwork.com, Oct 2026).
  - An RTX 3060 earned **$11.56 in its first week**, at 46% of hours rented (dev.to, Jun 2026).
- **Utilization by GPU class (CONFIRMED snapshot occupancy, verified machines):**

  | GPU | Occupancy (verified) | Median renter price |
  |---|---|---|
  | RTX 3090 | 87% | $0.25/h |
  | RTX 4090 | 85% | $0.48/h |
  | RTX 5090 | 74% | $0.71/h |
  | A100 SXM4 | 90% | $1.06/h |
  | H100 SXM | ~81% | $2.27/h (all listings) |
  | V100 | 78% | $0.14/h |
  | P100 | 48% | $0.09/h |
  | RTX 2080 Ti | 61% | $0.09/h |

  - **Unverified** occupancy is much lower: 4090 47%, 5090 54%, **A100 SXM4 21%**.
  - Old cards (V100, P40, 2080 Ti, 3060) do get rented, but at **$0.07–0.14 per GPU-hour** they gross only **$10–50 per GPU per month.**
- **What the host keeps.** On Vast, the renter price runs about **25% above host earnings**, so the host keeps about **80%** (Vast article, 2026-05-18). Hashrate.no lists a "25% hosting fee". At the Nov 2026 median prices, a GPU rented **100%** of the time grosses roughly:

  | GPU | Gross per month at 100% rented |
  |---|---|
  | RTX 3090 | ~$134 |
  | RTX 4090 | ~$274 |
  | RTX 5090 | ~$390 |
  | A100 SXM | ~$565 |
  | H100 SXM | ~$1,325 |
  | V100 | ~$62 |

- **Realistic monthly net per GPU** (my model, §2.8, before hardware depreciation and internet, at $0.10/kWh), conservative / typical / optimistic:

  | GPU | Conservative | Typical | Optimistic |
  |---|---|---|---|
  | RTX 3090 | $11 | $40 | $80 |
  | RTX 4090 | $31 | $97 | $185 |
  | RTX 5090 | $46 | $140 | $266 |
  | V100 / P40 | ~$1–3 | ~$13–16 | ~$30–34 |
  | A100 PCIe | $50 | $151 | $285 |

  These bands match the first-hand reports: bytwork sits at the conservative end, RedPandaMining at the optimistic end.
- **Location: LATAM is almost absent from the supply side, and LATAM hosts discount to get rented (CONFIRMED snapshot).**
  - Only **87 of 13,361 GPUs (0.65%) are in Latin America.** Brazil has 47, Mexico 16, Argentina 9, Puerto Rico 8, Chile 5, Peru 1, **Ecuador 1 (unverified, idle)**. **Colombia and Venezuela have none.**
  - LATAM same-model medians are **about 18–28% below the global median**: 4090 $0.338 vs $0.470; 3090 $0.189 vs $0.229.
  - Overall LATAM occupancy is 69%, similar to North America and Europe at 72–73%, but only **59% of LATAM GPUs are verified**, against 77–78% in North America and Europe.
  - **Implication:** a Colombia, Venezuela or Ecuador host can get rented, but should expect to price below US/EU peers. Rentals depend on verification, and verification needs **500/500 Mbps wired, a public IPv4 address and >90% reliability** (Vast docs, Nov 2026).
- **ROI has compressed for older cards and moved toward 24–32 GB consumer cards and datacenter GPUs.**
  - In September 2026, Salad **raised** 4090 and 5090 host rates ("demand exceeded supply for months") but **cut RTX 3090 rates by 32%** at the top tier ($0.150→$0.102/h) and cut 15 GPU classes (CONFIRMED, Salad blog 2026-09-04).
  - A 2023 Hacker News comment priced a Vast 3090 at about **$0.20/h**. The Nov 2026 median is **$0.229/h**, so prices are flat in nominal terms while supply grew.
  - The bytwork host estimates payback for AI rental only at **~3 years for a new 5090** and **~2 years for a used 4090** (Oct 2026).
- **Pain points that matter more than price:**
  - Verification takes **2–4 weeks** (Woven AI) to **months** (Habr host, 2024).
  - Machines are auto-deverified on errors.
  - Reliability penalties apply for restarts and offline time, and breaking a rental contract early "carries a serious penalty".
  - Payouts go only via **Wise, PayPal or Stripe**, weekly, with a **$20 minimum** (Vast docs). Stripe and Wise coverage is limited in Venezuela, and this must be verified for each country.
  - On Salad, cash-out fees eat small balances (Trustpilot, Nov 2026).
  - Rentals are lumpy: one 2×5090 rig was rented 7–8 consecutive days, then nothing.

---

## 2) Detailed findings

### 2.1 First-hand host reports (2024–2026)

No Reddit access (see method note). These are the first-hand or near-first-hand reports I could read. "Gross" means before electricity.

| # | Date of report | Platform | GPU(s) | Host location | Reported earnings | Utilization / notes | Electricity | Label | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Oct 2026 (updated 2026-10-21) | Vast.ai | 5× RTX 5090 across 4 rigs (EPYC 7B12, 7950X, 2× 7945HX mini-PCs) | Not stated (Russian-language author) | **~$230 total in 23 days**, ≈ $2.0/GPU-day, ≈ $60/GPU-month gross | Unverified, because upload was below 100 Mbps, despite 99.29% reliability; priced "near the very top of the listings" and still mostly idle | n/r | ANECDOTE (screenshots) | bytwork.com/en/articles/ai-income |
| 2 | same | Vast.ai | 2× RTX 5090 (EPYC rig) | same | ~$138 in 23 days | "Rented for about seven or eight consecutive days… since then, it has earned practically nothing" | n/r | ANECDOTE | same |
| 3 | same | Vast.ai | 1× RTX 5090 (7950X) | same | ~$59 in 23 days | Rented fairly consistently in the last week | n/r | ANECDOTE | same |
| 4 | same | Vast.ai | 2× RTX 5090 in laptop-CPU (7945HX) mini-PCs | same | ~$15 and ~$11 in 23 days | Rarely or never rented. Weak CPU and platform hurt the listing. | n/r | ANECDOTE | same |
| 5 | same | Vast.ai | RTX 4060 Ti (×3 rigs) | same | ~$0.35–0.50/day at first, then ~0 | "The cards were idle almost all the time"; "unverified machines receive practically no orders" | n/r | ANECDOTE | same |
| 6 | same | Vast.ai storage | SSD rental | same | ~$14/month | More than 10% of the extra income. Bandwidth income was negligible. | — | ANECDOTE | same |
| 7 | same | Salad vs Vast | 1× RTX 5090 | same | Earned more on Salad than on Vast "at the time" | Host's mining alternative (Pearl) would have earned ~$1,380 over the same 23 days | — | ANECDOTE | same |
| 8 | May 2026 (YouTube video) | Vast.ai | RTX 5090, verified | US (channel) | **~$9/day ≈ $270/month gross** | Live dashboard shown on camera | n/r | ANECDOTE (second-hand summary of a video) | RedPandaMining, via endlessmining.com/renting-your-gpu-for-ai-2026/ |
| 9 | May 2026 | Vast.ai | RTX 4090, verified (several) | US | **~$6/day each ≈ $180/month gross** | — | n/r | ANECDOTE (second-hand) | same |
| 10 | May 2026 | Vast.ai | RTX 4090, **unverified**, same asking price | US | **~$0.05/day** | Verification is the decisive variable | n/r | ANECDOTE (second-hand) | same |
| 11 | Jun 2026 (edited Oct) | Vast.ai | RTX 3060 12GB at $0.15/h | Probably Turkey ("Turkish electricity rates") | **$11.56 in week 1**; author projects $50–130/month for mid-tier GPUs | 77 of 168 hours rented (46%); daily range 0–22 h | Est. $8–15/month | ANECDOTE | dev.to/samhartley_dev/… |
| 12 | 2026-10-19 | Salad | RTX 5090 workstation | India | **$105 in 15 days ≈ $7/day** | — | n/r | ANECDOTE (review) | trustpilot.com/review/salad.com |
| 13 | 2026-11-12 | Salad | RTX 5060 Ti mini-PC | US | n/r | Must reboot twice a day; goes down overnight. Uptime problems kill earnings. | — | ANECDOTE (review) | same |
| 14 | 2026-11-10 | Salad | n/r | US | Cash-out fee ~$2 on a $10 balance | Removed machines | — | ANECDOTE (review) | same |
| 15 | 2026-11-02 | Salad | n/r | US | "Very slow income" | — | — | ANECDOTE (review) | same |
| 16 | Jun 2024 | Vast.ai | 2× RTX 3090 (dual Xeon E5-2697v2) plus a second machine | Russian-speaking (inferred) | n/r | Both machines rented **about ⅔ of the time** | n/r | ANECDOTE | habr.com/en/articles/821203/comments (user riv9231) |
| 17 | Jun 2024 | Vast.ai | 6× RTX 4090 | same | n/r | First rental a week after listing (2 GPUs). Remaining GPUs **idle about 3 weeks**. Verification "often takes months". | — | ANECDOTE | same |
| 18 | Jun 2024 | Clore.ai | Ryzen 7950X server | same | n/r | "Only miners rented"; the CLORE token then fell about 4× | — | ANECDOTE | same |
| 19 | Sep 2026 | Vast.ai | n/r | NL, PL | "Great returns"; "payments and invoicing processed promptly" | No figures given | — | ANECDOTE (review) | trustpilot.com/review/vast.ai |
| 20 | 2026-06-09 | Own cloud (AMD MI300X, datacenter) | — | US | "Renting my GPUs out for more money now due to supply being so tight" | Datacenter operator, not a peer-to-peer hobby host | — | ANECDOTE | news.ycombinator.com/item?id=48455436 |
| 21 | Dec 2025 (as told) | Vast.ai | RTX 4090, verified | Chiang Mai, Thailand | "$340/month at ~42% utilization" | **Internally inconsistent**: implies ≈ $1.12/h host income, about 3× the market price | n/r | **LOW-CRED** (second-hand) | passiveyieldlab.com/blog/cloud-gpu-rental-passive-income-2026/ |

**Reading the table.**
- The two most credible 2026 points bracket reality.
  - A **verified** 4090 or 5090 in a good setup grosses **$180–270 per GPU per month** (RedPandaMining).
  - A **new, unverified, bandwidth-limited** host grosses **about $60 per 5090 per month**, or close to zero on mid-range cards (bytwork).
- Reports of about ⅔ rented time appeared already in 2024 (Habr).

### 2.2 Platform-level utilization and prices (CONFIRMED primary data)

**A. Vast.ai full-market snapshot (my capture of the public `bundles` API).**
- Capture time: 2026-11-14, 12:07–12:13 UTC, Saturday. On-demand offers, `external=false`.
- **"Occupied"** means a machine's GPUs are not available for on-demand rental at snapshot time:
  - total GPUs = largest bundle offered by the machine;
  - free GPUs = largest bundle still rentable.
- Totals: **4,400 machines, 13,361 GPUs, 1,578 hosts; 71.9% occupied.**
- Cross-check: Hashrate.no shows **74.16%**, with 7,802 GPUs available and 22,393 rented, and a 25% fee (hashrate.no/platforms/vast, accessed 2026-11-14). Hashrate counts more GPUs, probably because it uses a different counting method.

| GPU (≥60 listed GPUs) | GPUs listed | Occupied | Median renter list price $/GPU-h | Host gross at 100% rented (~80% of list × 730 h) |
|---|---|---|---|---|
| RTX 5090 | 2,418 | 67.5% | 0.668 | ~$390/mo |
| RTX 4090 | 1,655 | 75.6% | 0.470 | ~$274/mo |
| RTX 3090 | 1,077 | 81.6% | 0.229 | ~$134/mo |
| RTX 3060 | 626 | 78.6% | 0.077 | ~$45/mo |
| RTX 5060 Ti | 526 | 67.9% | 0.147 | ~$86/mo |
| RTX 5080 | 430 | 68.4% | 0.255 | ~$149/mo |
| Tesla V100 | 380 | 72.6% | 0.107 | ~$62/mo |
| RTX PRO 6000 (S / WS / Max-Q) | 912 | 74–83% | 1.39–1.66 | ~$810–970/mo |
| A100 SXM4 | 341 | 80.4% | 0.968 | ~$565/mo |
| A100 PCIe | 169 | 72.2% | 0.669 | ~$391/mo |
| H100 SXM | 108 | 80.6% | 2.269 | ~$1,325/mo |
| H200 / H200 NVL | 342 | 78–79% | 4.0–4.6 | ~$2,340–2,690/mo |
| RTX A4000 | 253 | 62.8% | 0.102 | ~$60/mo |
| RTX 3080 | 167 | 63.5% | 0.136 | ~$79/mo |
| RTX 2080 Ti | 111 | 52.3% | 0.088 | ~$51/mo |
| Tesla P100 | 21 | 48% | 0.094 | ~$55/mo |
| Tesla P40 | 8 | 75% | 0.201 | (too few listings to rely on) |

Prices are the renter price, which includes Vast's fee and a little storage. The "Host gross" column is my approximation (×0.8).

**B. Vast occupancy: verified vs unverified for the key GPUs (CONFIRMED, same snapshot).**

| GPU | Verified: GPUs / occupied / median $ | Unverified: GPUs / occupied / median $ | Deverified: GPUs / occupied |
|---|---|---|---|
| RTX 3090 | 848 / **87%** / 0.249 | 143 / 62% / 0.177 | 86 / 62% |
| RTX 4090 | 1,254 / **85%** / 0.482 | 153 / **47%** / 0.401 | 248 / 48% |
| RTX 5090 | 1,805 / **74%** / 0.708 | 224 / 54% / 0.513 | 389 / 46% |
| RTX 3060 | 502 / 82% / 0.080 | 59 / 71% / 0.069 | 65 / 62% |
| Tesla V100 | 190 / 78% / 0.139 | 83 / 71% / 0.074 | 107 / 64% |
| A100 SXM4 | 287 / **90%** / 1.062 | 34 / **21%** / 0.650 | 20 / 50% |

Unverified hosts already price 15–40% lower and are still rented far less. Unverified listings only appear to renters who tick a "somewhat hidden" checkbox (bytwork, Oct 2026).

**C. Other platforms (CONFIRMED unless noted).**

| Platform | Data point | Date | Source |
|---|---|---|---|
| **Salad** (fixed host rates, no price-setting) | High / Med / Low / Lowest $/h: RTX 5090 0.300 / 0.271 / 0.233 / 0.175; RTX 4090 0.198 / 0.178 / 0.152 / 0.112; **RTX 3090 0.102 / 0.093 / 0.082 / 0.063 (was 0.150 at High)**; RTX 3080 0.084 / 0.074 / 0.061 / 0.042. At 100% uptime, a 4090 is $82–145/mo and a 3090 $46–74/mo. Salad cites 5090/4090 "demand exceeded supply for months" and says it "does not guarantee 100% uptime". | Effective 2026-09-12 | blog.salad.com/earning-rate-changes-september-2026 |
| **Akash** | 458 GPUs on the whole network, 299 allocated (65%). H100 79% (56 GPUs, 3 providers, $2.56/h median); A100-80G 61% (200 GPUs, 4 providers, $1.49/h); **V100 SXM2 22%** (40 GPUs, 1 provider, $0.31/h); consumer cards in single digits (3090: 11 GPUs, 100% used, $0.16/h). A tiny market dominated by a few providers. | 2026-11-14 | console-api.akash.network/v1/gpu and /v1/gpu-prices |
| **Clore.ai** | "Rented servers": 133 with RTX 3090, 112 with 4090, 112 with 5090. "Earn up to" $330 / $620 / $700 per card per month, but only on bare-metal contracts of 2+ to 8+ GPUs on 14–30-day terms (vendor ceiling, not realised). | Page accessed 2026-11-14 | clore.ai/host-3090.html |
| **RunPod** | The docs index (llms.txt) has no host or provider onboarding pages, and runpod.io/host returns 404. The community-host route appears closed or invite-only for small operators (INFERENCE). | 2026-11-14 | docs.runpod.io/llms.txt |

### 2.3 What drives utilization (CONFIRMED snapshot cross-tabs, plus Vast docs)

| Driver | Bucket | GPUs | Occupied |
|---|---|---|---|
| **Verification** | verified | 10,230 | **78.9%** |
| | unverified | 1,779 | 49.0% |
| | deverified | 1,352 | 48.9% |
| **Reliability score** | ≥0.99 | 8,700 | **77.9%** |
| | 0.98–0.99 | 2,300 | 69.5% |
| | 0.95–0.98 | 1,628 | 52.9% |
| | 0.90–0.95 | 388 | 44.3% |
| **Upload bandwidth** | ≥1,000 Mbps | 5,091 | **76.6%** |
| | 500–1,000 | 5,296 | 69.8% |
| | 100–500 | 2,322 | 70.4% |
| | <100 | 652 | 58.0% |
| **Price vs same-GPU median** | <0.8× | 2,433 | 77.3% |
| | 0.95–1.05× | 1,903 | 72.5% |
| | >1.5× | 1,907 | 65.6% |
| **Machine size** | 1 / 2 / 4 / 8 GPUs | 1,801 / 1,902 / 2,820 / 4,696 | 74% / 70% / 69% / 73% |
| **Datacenter flag** | community / datacenter | 12,254 / 1,099 | 71.8% / 72.5%; datacenter median price 2.4× higher |

How to read this:
- **Price elasticity is weaker than you might expect.** Going from 0.8× to 1.5× the median price costs only about 12 points of occupancy.
- **Verification and reliability matter much more:** 25–30 points.
- Vast confirms that verification is algorithmic and weighs GPU tier (B200 > H200 >> 5090 > 4070), GPU count per machine ("8×5090 >> 2×5090 > 1×5090"), VM support, symmetric bandwidth, and "supply & demand" (docs.vast.ai/host/understanding-verification, accessed 2026-11-14).

**Minimum requirements for verification** (docs.vast.ai/host/verification-stages, accessed 2026-11-14):
- **500 Mbps down and 500 Mbps up**, wired.
- A **public IPv4** address.
- Reliability >90%.
- SSD with ≥200 GB dedicated to Docker.
- System RAM ≥95% of total VRAM.
- ≥2 CPU cores per GPU.
- PCIe >2.85 GiB/s per GPU.
- CUDA ≥11.8, VRAM >7 GB, and identical GPUs within a machine.

**Market concentration.**
- The top 100 hosts hold **45%** of listed GPUs, and the top 10 hold 11%.
- 724 of the 1,578 hosts list only 1–2 GPUs.
- A small operator competes against a few professional fleets, but the market is not a monopoly.

**Stability check (second snapshot, about 15 minutes later).** See §2.3b below.

### 2.3b Snapshot stability
*(Filled in from the second capture; see the note at the end of this section.)*

### 2.4 ROI and payback: how it changed from 2023/24 to 2026

| Evidence | 2023–2024 | 2026 | Label / source |
|---|---|---|---|
| Vast RTX 3090 renter price | "literally $0.2 per hour" (HN, May 2023) | Median **$0.229/h** list; verified $0.249 | ANECDOTE (news.ycombinator.com/item?id=36026101) vs CONFIRMED snapshot |
| Time rented, mid-range hobby host | ~⅔ for 2× 3090 (Habr, Jun 2024) | 46% for a 3060 in week 1 (dev.to, Jun 2026); near 0 for unverified 4060 Ti or 5090 (bytwork, Oct 2026) | ANECDOTE |
| Salad 3090 host rate (High tier) | — | $0.150 → **$0.102/h** (−32%) from 2026-09-12; 4090 $0.180 → $0.198 (+10%); 5090 $0.270 → $0.300 (+11%) | CONFIRMED (Salad blog) |
| Vast price volatility in 2026, on-demand medians across regions (third-party scrape of the public API) | — | RTX 4090: May $0.67 → Aug $0.47 → Oct $0.57. RTX 5090: May $1.00 → Aug $0.40 → Oct $0.71. H100 SXM: May $3.72 → Jul $2.27 → Oct $3.06. A100 SXM 80G: steady $1.00–1.13. | CONFIRMED-ish (github.com/woodsonl/gpu-pricing-tracker, data/observations.csv, accessed 2026-11-14) |
| Host-estimated payback, AI rental only | — | New RTX 5090: **~3 years** (2 years with mining in idle time). RTX 5080: "a little over 2 years". Used RTX 4090: **~2 years**. | ANECDOTE / ESTIMATE (bytwork, Oct 2026) |
| Mining as idle filler | Clore's renters were mostly miners; the CLORE token fell ~4× (2024) | Pearl mining would have earned **~6×** the AI rental income over the same 23 days for 5× 5090 (Oct 2026). Vast lets hosts run "default jobs" (e.g., mining) in idle time. | ANECDOTE; docs.vast.ai/host/using-your-own-machine |

**Synthesis on ROI.**
- **Consumer 24 GB cards:** nominal prices are roughly flat since 2023 for the 3090. The 4090 still lists at about $0.47–0.57.
- **Supply has grown,** so a new entrant's utilization depends on verification and reliability, not on simply being listed.
- **Prices became more volatile in 2026.** The tracker shows 5090 swinging 2.5× between May and August.
- **Old cards keep being devalued.** Salad cut 15 classes in September 2026.
- **The upside:** 2026 is a supply-tight year for high-VRAM cards. Salad raised 4090/5090 rates, a datacenter operator reports tight supply, and RTX PRO 6000 and H200 listings are 74–83% occupied.

### 2.5 Location effects

**A. Where Vast supply sits (CONFIRMED snapshot, 2026-11-14).**

| Region | GPUs | Occupied | Verified share | Median upload (Mbps) |
|---|---|---|---|---|
| North America | 5,845 (43.7%) | 72.4% | 77% | 906 |
| Europe | 4,233 (31.7%) | 73.0% | 78% | 881 |
| Asia / Middle East (excl. China) | 1,653 | 72.5% | 79% | 634 |
| China / HK / TW | 1,366 | 67.5% | 71% | 637 |
| Oceania | 126 | 58.7% | 65% | 513 |
| **Latin America** | **87 (0.65%)** | **69.0%** | **59%** | **522** |
| Russia / CIS | 22 | **22.7%** | **0%** | 673 |
| Africa | 19 | 89.5% | 95% | 874 |

**LATAM detail.**

| Country | GPUs | Occupied | Median $/GPU-h |
|---|---|---|---|
| Brazil | 47 | 72% | 0.269 |
| Mexico | 16 | 56% | 0.189 |
| Argentina | 9 | 78% | 0.141 |
| Puerto Rico | 8 | 100% | 0.295 |
| Chile | 5 | 40% | 0.228 |
| Peru | 1 | idle | — |
| Ecuador | 1 (RTX 3090, unverified) | idle | 0.201 |
| **Colombia** | **0** | — | — |
| **Venezuela** | **0** | — | — |

- Brazil includes one 8× H200 (8/8 rented at $7.24/GPU-h) and one 8× 5090 (8/8 rented).
- Puerto Rico's machines have about 2 Gbps upload and are all verified.

**B. Same-GPU pricing by region (CONFIRMED snapshot, median renter list $/GPU-h, occupancy in brackets).**

| GPU | North America | Europe | China/HK/TW | Asia (other) | LATAM |
|---|---|---|---|---|---|
| RTX 3090 | 0.214 (79%) | 0.251 (87%) | 0.167 (72%) | 0.244 (84%) | **0.189 (75%, n=12)** |
| RTX 4090 | 0.481 (79%) | 0.488 (71%) | 0.468 (70%) | 0.467 (84%) | **0.338 (92%, n=12)** |
| RTX 5090 | 0.707 (68%) | 0.735 (64%) | 0.560 (71%) | 0.575 (69%) | 0.667 (75%, n=16) |
| A100 SXM4 | 0.669 (75%) | 1.067 (94%) | — | 1.147 (65%) | — |
| H100 SXM | 2.303 (100%) | 2.302 (72%) | — | 1.841 (81%) | — |

**Interpretation.**
- **Customers do rent outside the US and EU.** Occupancy in Asia and Brazil is similar to North America and Europe.
- **However, non-US/EU hosts list lower.**
  - China, Korea, Vietnam and Malaysia median list prices are well below North America and Europe; for example, Korea's overall median is $0.12 and Vietnam's $0.116, driven by mix and price.
  - LATAM 4090s list about **28% below** the North America median and still get rented.
- New Zealand shows **33% occupancy at a $0.069 median**: a thin, remote market with low prices *and* low use.
- Russia/CIS shows **0% verified and 23% occupancy**, consistent with payment and compliance friction (INFERENCE).
- **Bottom line on location:** a location penalty exists but is moderate, about **0–25% on price**. The bigger LATAM handicaps are **verification-grade connectivity** (only 59% of LATAM GPUs are verified; median upload 522 Mbps vs ~900 in North America and Europe) and **payout rails**.

**C. Workload latency and bandwidth (Vast optimization guide, accessed 2026-11-14).**
- Rental segments by duration:
  - serverless and inference: "hours to days";
  - experimentation and fine-tuning: "days to weeks";
  - training: "weeks to months+".
- **8× bundles get about 2× the search volume of 1× bundles.** Longer listed durations and auto-extend increase expected earnings.
- Training and batch jobs are latency-insensitive but **download-heavy.** Container images, model weights and datasets run to tens or hundreds of GB, so **symmetric bandwidth matters more than ping.** That is why verification demands 500/500 Mbps.
- Interactive inference endpoints prefer proximity to users, mostly US and EU (INFERENCE).
- CGNAT works on Vast via WireGuard, but RunPod-style setups need a static or port-forwardable IP (miningboard.com guide, Nov 2026, LOW-CRED for numbers but plausible for this requirement). A public IPv4 address is a hard verification requirement on Vast.

**D. LATAM and Venezuela-specific first-hand reports.**
- Searches in Spanish ("alquilar GPU vast.ai ganancias", "rentar GPU Venezuela") and Portuguese ("vast.ai host Brasil lucro") returned **no first-hand LATAM host reports.** They returned only generic guides: Xataka (2025-09-09), "no te vas a hacer rico" ("you won't get rich"); promptquorum; ganardineros.
- **No evidence was found of Venezuelan ex-crypto-miners pivoting to AI GPU rental.** This is consistent with **zero Venezuelan machines on Vast** in the snapshot.
- The search budget ran out before I could check Discord or Telegram mining groups in Venezuela (see §4).

### 2.6 Operational pain points (hosts)

| Pain point | Evidence | Label / source |
|---|---|---|
| **Verification gate** | Unverified 4090: ~$0.05/day vs ~$6/day verified. Verification takes "~2–4 weeks" (Woven AI) or "often months" (Habr 2024). It requires 500/500 Mbps and a public IPv4 address. | ANECDOTE / CONFIRMED docs (wovenai.ca; docs.vast.ai/host/verification-stages) |
| **Automatic deverification** | Any detected error, closed ports, low bandwidth, failing storage, NVML errors, container failures, or "detected abuse or policy violations" deverifies a machine temporarily. Reducing hardware after creation (fewer GPUs or less RAM) triggers deverification. | CONFIRMED (Vast docs) |
| **Reliability penalties** | Restarts during rentals, lost connectivity and failed instance starts reduce reliability. Offline time is penalized. Ending a contract early "carries a serious penalty". Driver auto-updates must be disabled. | CONFIRMED (docs.vast.ai/host/hosting-overview; optimization guide) |
| **Lumpy demand** | 2×5090 rented 7–8 days, then ~0. 6×4090: remaining GPUs idle about 3 weeks. 3060: 0 to 22 h/day. | ANECDOTE (bytwork; Habr; dev.to) |
| **Fragmentation** | A renter took 2 GPUs "from the centre" of a 6-GPU rig, after which the platform refused 4-GPU bundles (2024). Vast now recommends a mix of minimum-GPU settings. | ANECDOTE / CONFIRMED docs |
| **Payouts** | Vast: Wise, PayPal or Stripe only; weekly invoices on Fridays; **$20 minimum**; first payout up to 2 weeks. Hosts must be able to receive B2B payments in their country. Salad: cash-out fees noticeable on small balances. | CONFIRMED (docs.vast.ai/host/payment); ANECDOTE (Trustpilot) |
| **Hardware wear and uptime** | The rental on/off load cycle may stress used cards more than steady mining (host opinion). A consumer mini-PC needed reboots twice a day. | ANECDOTE (bytwork; Trustpilot) |
| **Renter abuse / mining** | 2024: on Clore, "only miners rented". Vast lists "detected abuse" as a cause of deverification. **No 2025–2026 first-hand reports of illegal content or of unpaid earnings on Vast** were found in accessible sources (Reddit inaccessible). | ANECDOTE / gap |
| **Security perception** | "A host can snoop on your workloads very easily" (HN, 2023). This caps what enterprise renters will run on community hosts; ISO 27001 datacenter hosts get the "Secure Cloud" label and higher prices (datacenter median price 2.4× community). | ANECDOTE / CONFIRMED docs (datacenter-status) |
| **Datacenter tier is gated** | Requires ISO/IEC 27001, a registered business, a signed agreement, KYC, and ≥5 GPU servers. | CONFIRMED (docs.vast.ai/host/datacenter-status) |

### 2.7 Synthesis: realistic monthly net per GPU (ESTIMATE)

**Formula:** net = 730 h × [renter median × 0.80 × location factor × utilization − kW_load × $/kWh × utilization − kW_idle × $/kWh × (1 − utilization)].

**Inputs:**
- Renter medians from my 2026-11-14 Vast snapshot.
- Host share 0.80 (Vast article 2026-05-18).
- Power per GPU including a share of the system: 3060 0.20 kW; 3080 0.37; 3090 0.42; 4090 0.50; 5090 0.65; V100 0.32; P40 0.27; A100 PCIe 0.33; A100 SXM 0.50; H100 SXM 0.85. Idle 0.04–0.10 kW.

**Scenarios:**
- **Conservative:** 20% utilization, price at 75% of the global median. This represents a new, unverified or LATAM host, as in bytwork.
- **Typical:** 50% utilization, 85% of median. This represents a verified host in its first months, or one with reliability of 0.95–0.98.
- **Optimistic:** 78% utilization, 100% of median. This represents a verified host with reliability ≥0.99 and ≥1 Gbps, matching snapshot verified occupancy.

**Excluded:** hardware depreciation, internet, rent and labour.

| GPU class | Conservative, $0.10/kWh (gross) | Typical, $0.10/kWh (gross) | Optimistic, $0.10/kWh (gross) | Typical at $0.20/kWh | Typical at $0.05/kWh |
|---|---|---|---|---|---|
| RTX 3060 12GB | $1 ($7) | $10 ($19) | $23 ($35) | $2 | $15 |
| RTX 3080 10GB | $4 ($12) | $18 ($34) | $40 ($62) | $3 | $26 |
| **RTX 3090 24GB** | **$11** ($20) | **$40** ($57) | **$80** ($104) | $23 | $48 |
| **RTX 4090 24GB** | **$31** ($41) | **$97** ($117) | **$185** ($214) | $77 | $107 |
| **RTX 5090 32GB** | **$46** ($59) | **$140** ($166) | **$266** ($304) | $114 | $153 |
| Tesla V100 | $1 ($9) | $13 ($27) | $30 ($49) | −$1 | $20 |
| Tesla P40 | $3 ($10) | $16 ($27) | $34 ($50) | $4 | $21 |
| A100 PCIe | $50 ($59) | $151 ($166) | $285 ($305) | $137 | $159 |
| A100 SXM4 80G | $73 ($85) | $219 ($240) | $411 ($441) | $198 | $230 |
| H100 SXM | $181 ($199) | $528 ($563) | $984 ($1,034) | $494 | $546 |

**Checks against first-hand data.**
- RedPandaMining's verified 4090 at ~$180/month gross and 5090 at ~$270 sit at the optimistic gross ($214 / $304).
- Bytwork's ~$60/month per 5090 equals the conservative gross ($59).
- Salad's fixed rates at 100% uptime ($82–145 for a 4090; $46–74 for a 3090) sit between typical and optimistic gross, with no price-setting risk but no utilization guarantee.

**Payback illustration (ESTIMATE; hardware prices are for other agents to confirm):** payback months = (GPU + share of chassis/PSU/CPU/RAM/SSD) ÷ monthly net.
- Used 3090 at about $700 all-in per GPU: **~18 months typical, ~9 optimistic, >5 years conservative.**
- Used 4090 at about $1,900 all-in: **~20 months typical, ~10 optimistic.**
- Used V100 or P40 at about $150–250: **12–20 months typical**, but on very thin absolute dollars ($13–16/month). These cards also face a CUDA and feature support cliff and are not the AI workloads renters want.

---

## 3) Implications for the LATAM used-hardware rental business

1. **Verification is the business, not the hardware.** The same 4090 earns $0.05/day unverified and ~$6/day verified. Vast's verification needs:
   - **500/500 Mbps wired, a public IPv4 address, >90% reliability**;
   - balanced, server-grade CPU, RAM and NVMe;
   - and it favours **multi-GPU boxes** (8× ≫ 2× ≫ 1×) and VM support.

   A Colombia, Venezuela or Ecuador site must secure **symmetric fibre with a static IPv4 address and reliable power (UPS or generator)** before the GPU purchase price matters. LATAM's verified share is 59%, against 77–78% in North America and Europe, and median upload is 522 Mbps against about 900. That gap is exactly this handicap.
2. **Old cards are a trap for absolute dollars.**
   - V100, P40, 2080 Ti and 3060-class cards gross **$7–50 per GPU per month** even when well utilized.
   - Salad cut 3090 and older rates in September 2026.
   - "Cheap" only works if the hardware is close to free and power costs ≤$0.05/kWh. Each GPU still consumes chassis, PCIe, RAM and bandwidth that would earn more under a 24–32 GB card.
   - The demand signal in 2026 favours **RTX 3090/4090/5090, RTX PRO 6000, A100/H100/H200.** Verified 3090s are 87% occupied, 4090s 85%, A100 SXM 90%.
3. **Expect a location discount of roughly 0–25%.** LATAM 4090s list about 28% below the US median yet are 92% occupied (n=12). Brazil shows that even 8× H200 and 8× 5090 boxes fill up from South America. Plan revenue at **75–85% of the US median price**, and avoid latency-sensitive inference positioning. Target training and batch renters, who care about bandwidth rather than ping.
4. **There is no incumbent supply in Colombia or Venezuela.** This is not proof of demand, but there is also no local competition. Supply is effectively zero in both countries and one idle unverified 3090 in Ecuador. **There is no visible evidence that Venezuelan miners have pivoted**, either because it is not viable (power reliability, connectivity, payouts) or because it is invisible to this method.
5. **Payout rails are a gating item for Venezuela.** Vast pays only via Wise, PayPal or Stripe and requires B2B-receivable accounts. Confirm country availability before investing. A Colombian or foreign legal entity receiving payouts may be required.
6. **Plan for a ramp.**
   - Model months 1–2 at the conservative band, about 20% utilization: verification takes 2–4 weeks or more.
   - Expect lumpy demand, with multi-day full rentals followed by idle weeks.
   - Use **idle-time filler jobs** (Vast default jobs: mining, or Salad on separate boxes) to cover power.
   - Sell storage: about $14/month per host was more than 10% of one host's extra income.
7. **Scale matters for both verification and the datacenter tier.**
   - Fleets of **4–8 identical GPUs per box** rank and verify better, and 8× bundles get about 2× the search volume.
   - The higher-priced "Secure Cloud" tier (datacenter median price 2.4× community) needs ISO 27001, a registered business and ≥5 servers. This is plausible only via colocation in a certified LATAM datacenter, for example in Bogotá or Quito, rather than a home or warehouse site.
8. **Realistic unit economics** (verified, typical case, at $0.10/kWh, per GPU per month, before capex and internet): 3090 about $40, 4090 about $97, 5090 about $140, A100 PCIe about $150. A 32-GPU fleet of used 3090s grosses roughly **$1,800/month typical and $3,300 optimistic**. A fixed 1 Gbps symmetric business line plus colocation or power infrastructure can consume a large share of that at small scale.

---

## 4) Confidence and gaps

| Item | Confidence | Why |
|---|---|---|
| Vast occupancy by GPU, verification, reliability and region (snapshot) | **Medium-high** for 2026-11-14 | Primary API data; matches Hashrate.no (72% vs 74%). Caveats below. |
| Realised 2026 earnings per verified 4090/5090 | **Medium** | Two independent first-hand sources bracket each other. The video figure is second-hand via a blog. |
| LATAM location discount | **Medium-low** | Direction is consistent, but n=87 GPUs, and the LATAM GPU mix differs. |
| ROI trend 2023→2026 | **Low-medium** | No dated 2023–24 price series was accessible. Evidence is anecdotal plus Salad's confirmed 2026 rate changes. |
| Pain points | **Medium** | Docs are confirmed; abuse, disputes and unpaid-earnings frequency is unknown because Reddit and Discord were not accessible. |

**Snapshot caveats.**
- "Occupied" = not available for **on-demand** rental. It can include **self-rentals** by hosts, which are free and allowed by Vast, and reserved contracts.
- It excludes interruptible (bid) usage and hosts' default jobs. In other words, **occupancy ≠ paid third-party utilization** and is an upper bound for a new host.
- Prices are list asks, not transaction prices.
- It is a single weekend timepoint, and offline or unlisted machines are invisible. Survivorship bias also applies: hosts who quit because of low earnings are not in the sample.

**Gaps.**
- **No Reddit data:** r/vastai, r/LocalLLaMA, r/homelab and r/gpumining were blocked.
- Search was exhausted before I could cover:
  - X/Twitter, YouTube transcripts and Discord quotes;
  - Vast host-fee policy history;
  - Venezuelan and Colombian mining-community channels;
  - io.net worker earnings (the explorer page is JavaScript-only and returned no data);
  - TensorDock host terms.
- **Not resolved:** whether Wise, PayPal or Stripe B2B payouts work in Venezuela, Colombia and Ecuador; local electricity and internet prices (other agents' topics).
- **Suggested follow-ups:**
  - Repeat the snapshot over 7+ days, on weekdays, to measure churn.
  - Ask 2–3 Brazilian, Mexican or Argentine Vast hosts directly for dashboards.
  - Get a host API key and pull Vast's own `metrics/gpu/locations` and `gpu-trends` endpoints, which require a host key (docs.vast.ai/host/market-metrics).

---

## 5) Sources (all accessed 2026-11-14 unless noted)

**Primary data captured**
- Vast.ai public offer-search API (`https://console.vast.ai/api/v0/bundles/`): full on-demand snapshot 2026-11-14 12:07–12:13 UTC (7,394 offers, 4,400 machines). Raw files are in the scratchpad (`agent09/dl/snap_all_20261114.json`).
- Akash console API: https://console-api.akash.network/v1/gpu and https://console-api.akash.network/v1/gpu-prices
- Hashrate.no Vast tracker: https://www.hashrate.no/platforms/vast and https://www.hashrate.no/platforms/vast/gpus
- GPU price tracker (scrape of Vast's public API, Feb–Oct 2026): https://github.com/woodsonl/gpu-pricing-tracker (`data/observations.csv`)

**Platform documentation and official posts**
- Salad host rate change (published 2026-09-04, effective 2026-09-12): https://blog.salad.com/earning-rate-changes-september-2026
- Vast, "How Much Money Can You Earn…" (2026-05-18): https://vast.ai/article/how-much-money-can-you-earn-renting-out-your-gpu-on-vast-ai
- Vast, "Scaling a GPU Hosting Business…" (2026-10-19): https://vast.ai/article/scaling-a-gpu-hosting-business-data-center-vs-home-server-rack-operations
- Vast docs:
  - https://docs.vast.ai/host/understanding-verification.md
  - https://docs.vast.ai/host/verification-stages.md
  - https://docs.vast.ai/host/optimization-guide.md
  - https://docs.vast.ai/documentation/host/hosting-overview
  - https://docs.vast.ai/host/payment.md
  - https://docs.vast.ai/host/using-your-own-machine.md
  - https://docs.vast.ai/host/datacenter-status.md
  - https://docs.vast.ai/host/market-metrics.md
  - https://docs.vast.ai/cli/reference/search-offers
  - https://docs.vast.ai/llms.txt
- Clore.ai RTX 3090 hosting page: https://clore.ai/host-3090.html
- RunPod docs index: https://docs.runpod.io/llms.txt (runpod.io/host returned 404)

**First-hand and anecdotal**
- bytwork.com, "GPU Payback Period for AI Computing Rentals" (updated 2026-10-21): https://bytwork.com/en/articles/ai-income
- Endless Mining, summary of a RedPandaMining video (May 2026): https://endlessmining.com/renting-your-gpu-for-ai-2026/
- Sam Hartley, DEV Community (Jun 2026, edited Oct): https://dev.to/samhartley_dev/i-rented-out-my-gpu-for-passive-income-heres-what-happened-after-my-first-week-1mbh
- Trustpilot, Salad reviews (Oct–Nov 2026): https://www.trustpilot.com/review/salad.com
- Trustpilot, Vast.ai reviews (Sep 2026): https://www.trustpilot.com/review/vast.ai
- Habr comment thread (Jun 2024): https://habr.com/en/articles/821203/comments
- Hacker News: https://news.ycombinator.com/item?id=48455436 (2026-06-09); https://news.ycombinator.com/item?id=36026101 (May 2023)
- Passive Yield Lab (2026-05-02, LOW-CRED): https://passiveyieldlab.com/blog/cloud-gpu-rental-passive-income-2026/

**Context and low-credibility secondary pages (not used for conclusions)**
- https://ownyourmind.ai/use/gpu-provider-income/ (2026-06-27, updated 2026-10-20; modelled)
- https://miningboard.com/guides/rent-gpu-for-ai-earnings (Nov 2026; unsourced utilization claims of "60–85%")
- https://www.cloudearn.net/vastai/ (2026; unsourced)
- https://auradigitalglobal.com/blog/vast-ai-gpu-server-earnings/ (modelled)
- https://wovenai.ca/ (vendor; verification "~2–4 weeks", ingests ">24,000 offers, 5,000 machines" per cycle)
- https://www.xataka.com/robotica-e-ia/puedes-ganar-dinero-tu-gpu-cuando-no-usas-basta-que-se-prestes-a-quienes-entrenan-modelos-ia (2025-09-09)
- https://github.com/GeiserX/CashPilot/blob/main/docs/guides/vast-ai.md
