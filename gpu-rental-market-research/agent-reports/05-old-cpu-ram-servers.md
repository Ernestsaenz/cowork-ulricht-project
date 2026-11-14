# Agent 05: What old CPU/RAM-heavy enterprise servers earn when rented

**Scope:** Used Dell PowerEdge R620/R720/R730/R740, HPE DL360/DL380 Gen8–Gen10 and Supermicro boxes with dual Xeon E5 v2–v4 or Xeon Scalable gen 1/2 and 128–768 GB ECC RAM, with little or no GPU. The question is whether they can earn money as rental assets, as raw material for selling parts, or not at all.
**Research date:** 2026-11-14. All USD conversions use EUR/USD 1.1052 (the ECB reference rate for 2026-11-13, via frankfurter.dev).
**Labels used:** **CONFIRMED** means taken from a primary source or a live API pulled today. **SECONDARY** means a third-party report. **ESTIMATE** means my own calculation from stated assumptions.
**Method note:** The web-search budget shared by all agents ran out partway through this task. The last sections therefore lean on primary pages and live APIs I fetched directly (Hetzner, OVH, Akash, Vast.ai, Flux, CoinGecko, OpenRouter, SPECpower) and on searches made earlier in the session. The gaps are listed in Section 4.

---

## 1. Executive summary

- **Retail price that sets the ceiling (CONFIRMED, 2026-11-14).** OVH Kimsufi KS-6-B (2× Xeon E5-2680 v3, 24 cores/48 threads, 256 GB DDR4) is listed at **€86.99/mo, about $96** (the OVH US site lists **$102**). That works out to roughly **$0.38/GB-RAM-month and $2/thread-month**, with bandwidth, DDoS protection and an SLA included. OVH's marginal price for extra RAM is only **$0.18–0.35/GB-month**.
  - Old high-RAM OVH models (KS-6-B, KS-6) are **out of stock** in every datacenter.
  - The Hetzner auction feed holds only **98 servers**. Its cheapest 256 GB box (E5-1650 v3) is **€145, about $160**.
  - Hetzner raised prices in 2026 because of RAM/NVMe costs (SECONDARY).
  - LATAM retail costs far more: HostDime Bogotá charges **$799/mo** for 2× E5-2670 v3 with 64 GB.
- **Akash (CPU/RAM leases) is the only real CPU marketplace, and an unknown new provider gets almost no leases.**
  - Default bid prices (CONFIRMED, Akash provider pricing script): **$1.60/thread-month and $0.80/GB-RAM-month.** An R730 with 56 threads and 256 GB is worth **$294/mo** only if 100% leased.
  - Network-wide utilization today (CONFIRMED, Akash console API) is **26% of CPU and 26% of RAM**. About **11,000 vCPU and 64 TB of RAM sit idle**.
  - Among 23 online CPU-only providers, the 14 **unaudited** ones run at **1.5% CPU and 1.5% RAM utilization**. At that rate an R730 would earn about **$4/mo**. Audited ones reach 43% CPU and 25% RAM, which would mean about $89/mo.
  - **Zero LATAM providers are online.** Fifteen have ever registered (9 in Brazil, 3 in Argentina, 2 in Colombia).
- **Other CPU marketplaces are not usable.**
  - **Vast.ai has no CPU-compute market.** Its 64 "0-GPU" offers are disk-only bundles at a flat $0.01/h, and none was rented.
  - **Fluence** pays a "$10/core-month" FLT target, but requires Tier-3/4 datacenters, SOC2/ISO 27001, 10 GbE and Cascade Lake or newer CPUs. E5 v2–v4 servers are excluded. FLT trades at **$0.0023** (market cap **$0.79 M**).
  - **Flux** rewards are token emissions, not customer demand. A Stratus node (8 cores/16 threads, 64 GB) earns about **$18.5/mo** in FLUX (ESTIMATE) and needs 40,000 FLUX of collateral, about $1,940.
  - **Golem:** the stats API was unreachable (HTTP 502) and the stats page showed 0 providers online. GLM trades at $0.095.
- **Storage DePIN is not an income source for drive-filled servers.**
  - Storj pays **$1.35/TB-month stored, $1/TB egress and $1/TB repair**, in USDC on Ethereum L1, as of 2026-09-01 (CONFIRMED).
  - **Storj Labs filed for Chapter 11 on 2026-07-26.** A minimum payout threshold of about $50–70 per wallet applies.
  - A node fills at roughly 0.5–1 TB/month per /24 subnet (forum anecdotes). A 48 TB R720xd would earn **under $10/mo in year 1, which is less than its electricity**.
  - Filecoin needs sealing hardware, FIL collateral and verified deals. It does not suit a small operator.
- **CPU-only LLM inference is uneconomic against API prices.**
  - Measured speeds on old Xeon/EPYC with DDR4 are **2–4 tok/s on DeepSeek-671B (Q3/Q4)**.
  - At 350 W and 3 tok/s, **electricity alone costs about $3.2 per million output tokens at $0.10/kWh**. The market price for DeepSeek-V3.2 output is **$0.38/M** (OpenRouter), and DeepSeek's own V4.1-Flash is **$0.60–1.20/M**.
  - Only small-active-parameter models (gpt-oss-120b) with batching reach electricity parity, and nobody buys that capacity. I found no paid marketplace for CPU inference.
- **Power (CONFIRMED vendor SPECpower, minimal configs).**
  - R720: 51–54 W idle, 230–250 W at full load.
  - R730 / DL360 Gen9: 45–51 W idle, 270–290 W full.
  - R740 / DL380 Gen10 (Platinum): 49–55 W idle, 430–470 W full.
  - Realistic with 256–512 GB and redundant PSUs (ESTIMATE): **110–180 W idle, 320–550 W full.** At 170 W average, a server uses 124 kWh/month, which costs **$6 / $12 / $19 / $25 per month at $0.05 / $0.10 / $0.15 / $0.20 per kWh**.
- **Net monthly margin for an R730 (56 threads/256 GB) at $0.05 / $0.10 / $0.15 / $0.20 per kWh (ESTIMATE):**
  - Unaudited Akash: **−$0.7 / −$5.8 / −$10.9 / −$16**.
  - Audited-average Akash (hard to reach): +$82 / +$75 / +$68 / +$61.
  - 3× Flux Stratus: +$48 / +$41 / +$34 / +$26, with about $5.8k of FLUX collateral at risk.
  - Storj, year 1: about $0 or negative.
  - All figures are before hardware depreciation, internet, cooling and the time spent running it.
- **The RAM inside the server is the real asset.**
  - Used DDR4 RDIMM resale values (SECONDARY, amcompute, data through 2026-08):
    - 32 GB: **$100–150**, up 335% year on year (**$3.1–4.7/GB**).
    - 64 GB: **$250–370**, up 285% (**$3.9–5.8/GB**).
    - 16 GB: $47–60, up 250%.
    - 64 GB LRDIMM: $100–170.
  - eBay asking prices for 64 GB DDR4-2666 are $300–400. I could not reach eBay sold listings (HTTP 403).
  - The **256 GB in one R730 resells for $800–1,200**. A **768 GB box resells for $2,400–4,400**.
  - That equals **more than 15 years of realistic Akash income** for an unaudited provider, or **about 11–16 months of best-case audited net income**.
  - DDR4 chip spot prices have slipped about 11% from their 2026-09-04 peak (SECONDARY, PCSP, 2026-10-30), so the selling window may be closing.
- **Verdict:**
  - **An old CPU-only server is not a viable P2P/DePIN rental asset.**
  - **A DDR4-era server (R730/DL380 Gen9/R740/Gen10) is a strong parts-arbitrage asset in 2026, mainly for its RDIMMs and secondarily its SSDs.**
  - **DDR3-era servers (R620/R720/Gen8) are probably neither:** their RAM did not get the same AI-driven price jump (no 2026 data found) and they are inefficient per watt.
  - GPU-capable chassis (Supermicro 4028GR/4029GP, R740) only make sense as hosts for GPUs. Their income depends on the GPUs, and old hosts list about 2–20% lower per GPU-hour on Vast.

---

## 2. Detailed findings

### 2.1 Retail benchmark: what the same capacity rents for from established providers

**Table A. Dedicated servers comparable to old enterprise boxes.** Status is CONFIRMED unless marked otherwise. EU prices exclude VAT.

| Provider / model (location) | CPU | RAM | List price | USD/mo | $/GB-RAM-mo | $/thread-mo | Source |
|---|---|---|---|---|---|---|---|
| **OVH Kimsufi KS-6-B** (EU) | 2× Xeon E5-2680 v3, 24c/48t | **256 GB** DDR4-2400 | €86.99 (base 64 GB €54.99) | **96.1** | 0.38 | 2.00 | OVH catalog API (IE) |
| OVH KS-6-B (US site) | same | 256 GB | $102 | 102 | 0.40 | 2.12 | OVH US catalog API |
| OVH KS-6 (EU) | EPYC 7351P 16c/32t | 256 GB | €70.99 | 78.5 | 0.31 | 2.45 | OVH API |
| OVH KS-5-B (EU) | E5-1650 v4 6c/12t | 128 GB | €33.99 | 37.6 | 0.29 | 3.13 | OVH API |
| OVH So You Start SYS-5 (EU / US) | 2× Silver 4214R 24c/48t | **384 GB** | €189.99 / $245 | 210 / 245 | 0.55 / 0.64 | 4.4 / 5.1 | OVH API |
| OVH SYS-4 (EU / US) | EPYC 7371 16c/32t | **512 GB** | €209.99 / $290 | 232 / 290 | 0.45 / 0.57 | 7.3 / 9.1 | OVH API |
| OVH RISE-8 (EU) | EPYC 7532 32c/64t | 512 GB / **1,024 GB** | €317.99 / €569.99 | 351 / 630 | 0.69 / 0.62 | 5.5 / 9.8 | OVH API |
| **Hetzner Server Auction** (FSN1) | E5-1650 v3 6c/12t | **256 GB** ECC | €145 | 160 | 0.63 | 13.4 | Hetzner live feed |
| Hetzner Server Auction | E5-1650 v3 | 128 GB | €114–121 | 126–134 | 0.98 | 10.5 | Hetzner live feed |
| Hetzner AX162 (new) | EPYC 9454P 48c/96t | up to 512 GB DDR5 | €319–614 | up to 679 | 1.33 | 7.1 | hetzner.com matrix |
| **HostDime Bogotá** | 2× E5-2670 v3 24c/48t | 64 GB | $799 | 799 | 12.5 | 16.6 | hostdime.com |
| HostDime Bogotá | 2× E5-2650 v3 20c/40t | 64 GB | $599 | 599 | 9.4 | 15.0 | hostdime.com |
| Latitude.sh (Bogotá, São Paulo, Mexico City, Santiago and Buenos Aires are among its sites) | EPYC 9254 24c | 384 GB | $1,482 | 1,482 | 3.9 | 30.9 | latitude.sh/pricing |
| Latitude.sh | EPYC 9354P 32c / 9275F 24c | **768 GB** | $2,351 / $1,916 | — | 2.5–3.1 | 37–40 | latitude.sh/pricing |
| LATAM price floors (Valebyte aggregator) | various | — | Brazil from $93.50, Mexico from $185, Chile from $295 | — | — | — | valebyte.com, checked 2026-11-13 (SECONDARY) |

**Marginal price of extra RAM at OVH (CONFIRMED add-on prices):**
- KS-6-B, 64→256 GB: €32 for 192 GB, which is **$0.18/GB-month**.
- SYS-4, 256→512 GB: €80, which is **$0.35/GB-month**.
- SYS-5, 96→384 GB: €90, which is **$0.35/GB-month**.
- RISE-8, 256→1,024 GB: €380, which is **$0.55/GB-month**.

**Supply signals (CONFIRMED):**
- OVH's availability API shows **every KS-6-B and KS-6 configuration as unavailable** in every datacenter. Some SYS-4 512 GB and SYS-5 384 GB configurations show "1H-low" (limited stock).
- The Hetzner auction JSON reports `serverCount: 98`. Prices there look high for the hardware: an i7-6700 with 32 GB costs €77. Historically the auction listed many hundreds of servers with similar boxes at about €30–40. That comparison comes from my own background knowledge and is not re-verified (INFERENCE).
- SECONDARY sources (Tom's Hardware, heise, DCD): Hetzner raised prices from 2026-04-01 by up to 37%, with Server Auction getting a flat +3%. A further round on 2026-06-15 targeted setup fees, citing RAM and NVMe costs.
- **Contabo:** the site returns HTTP 403 (bot protection). PricingSaaS (SECONDARY) logged July 2026 increases on Contabo dedicated tiers, for example Ryzen €86.40→€139.40 and Genoa €152.10→€182.10.

**Takeaways:**
- In Europe, an old dual-E5 server with 256 GB rents for about **$95–100/month at retail**. Extra RAM is sold at **$0.2–0.55/GB-month**.
- Inside LATAM, comparable dedicated servers cost **4–10× more** ($600–800 for 64 GB at HostDime Bogotá).
- That premium is earned by datacenter colocation, IP transit, SLA and support. A P2P marketplace does not pay it.

### 2.2 Marketplaces for CPU/RAM capacity: what a supplier is paid, and whether anyone buys

**Table B. Akash network state (CONFIRMED, console-api.akash.network, 2026-11-14 12:00 UTC).**

| Metric | Value |
|---|---|
| Active providers | 54 (53 online in the provider list) |
| Total / leased CPU | 14,881 vCPU / 3,885 leased (**26%**) |
| Total / leased RAM | 86.4 TB / 22.3 TB (**26%**) |
| Total GPUs / leased | 457 / 291 |
| Daily spend, whole network | about **$10,006/day, roughly $304k/month** (mostly GPU) |
| Active leases | 727 |
| CPU-only providers, **audited** (9) | CPU 793/1,847 (**42.9%**), RAM 1,314/5,338 GB (**24.6%**) |
| CPU-only providers, **unaudited** (14) | CPU 24/1,584 (**1.5%**), RAM 43/2,813 GB (**1.5%**) |
| LATAM providers | 15 ever registered (BR 9, AR 3, CO 2, plus 1 tagged US), **0 online** |

**Pricing:** The default bid script used by Akash providers (CONFIRMED, akash-network/helm-charts `price_script_generic.sh`) sets:
- **CPU: $1.60/thread-month**
- **RAM: $0.80/GB-month**
- Ephemeral disk: $0.02/GB-month
- Persistent storage: HDD $0.01, SSD $0.03, NVMe $0.04 per GB-month
- Public IP: $5/month

The provider calculator's sample breakdown matches these defaults exactly: CPU $16 = 10 threads, memory $204.80 = 256 GB.

**What all leased CPU and RAM on Akash would bring in at default prices (ESTIMATE):** 3,885 vCPU × $1.60 plus 22,341 GB × $0.80 comes to about **$24k/month across the whole network**. That is roughly 8% of total spend, and it is an upper bound because part of it is attached to GPU leases.

**Table C. Akash income for the reference servers (ESTIMATE, default bid prices, before network take rate).**

| Server | 100% leased | Audited-average utilization | Network-average (26%) | **Unaudited (1.5%)** |
|---|---|---|---|---|
| R720 2× E5-2670 v2, 40 threads, 256 GB | $269 | $78 | $70 | **$4.0** |
| R730 2× E5-2680 v4, 56 threads, 256 GB | $294 | $89 | $77 | **$4.4** |
| R730, 56 threads, 512 GB | $499 | $139 | $130 | **$7.5** |
| R740 2× Gold 6148, 80 threads, 768 GB | $742 | $206 | $193 | **$11** |

**Interpretation:**
- Akash's default RAM price ($0.80/GB-month) is 2–4× higher than OVH's retail marginal RAM price. Tenants who can use a Kimsufi box have little reason to pay Akash defaults. That explains why so much capacity sits idle.
- Leases go to audited providers. The audited set is dominated by a few US and EU datacenter operators; the top one leases 245 of its 318 vCPU.
- A new, unaudited, home-hosted LATAM provider should plan for roughly zero utilization.

**Table D. Other CPU/RAM marketplaces.**

| Marketplace | What a supplier is paid | Real demand? | Fit for old LATAM servers | Status |
|---|---|---|---|---|
| **Vast.ai** | No CPU-compute product. The 64 `num_gpus=0` offers are `resource_type: disk` bundles at a flat **$0.01/h** placeholder, and none was rented | No | No | CONFIRMED (Vast public API) |
| **Fluence** (CPU Cloud) | FLT idle reward "target $10/core-month" plus USDC rentals at provider-set prices. Customer-side examples: about $5.39/vCPU-month (vendor blog) | Small: about $1M provider ARR claimed (undated, SECONDARY) | **Excluded:** needs Tier-3/4 DC, SOC2 Type 1 and 2, ISO 27001, 10 GbE, Cascade Lake or newer / Zen 2 or newer. **FLT trades at $0.0023, market cap $0.79M** (down from a $1.52 all-time high) | CONFIRMED (fluence.ai page dated 2026-11-05; CoinGecko) |
| **Flux** (FluxNodes) | Emissions: about 12.6 FLUX/block (`getblocksubsidy`), split roughly 0.9 / 3.15 / 8.1 to Cumulus / Nimbus / Stratus, 30 s blocks. With 3,417 / 1,690 / 1,859 nodes that gives about **$1.1 / $7.9 / $18.5 per node-month** at FLUX $0.0485 | Rewards come from inflation, not paying customers | Old servers pass the benchmark. A 56-thread/256 GB box could host about 3 Stratus nodes (16 threads, 64 GB and 880 GB SSD each), about **$55/mo**, but needs 120,000 FLUX (about $5.8k) collateral and 3 public IPs | Node counts, subsidy and price CONFIRMED (Flux API, CoinGecko). Per-tier split ESTIMATE based on the PoUW v2 article (2025-10-23) scaled to 12.6 |
| **Golem** | Provider-set GLM prices | `api.stats.golem.network` returned **HTTP 502**. stats.golem.network showed "0 providers online", which may be a loading artifact. GLM trades at $0.095 | Unknown; probably negligible | Partly verified |
| **SaladCloud** | Customer price **$0.005/vCPU-h plus $0.001/GB-h** for CPU-only containers. Supplier share not published | Supply is mainly consumer Windows PCs; CPU-only demand not quantified | Weak: built for desktop GPUs | CONFIRMED (salad.com/pricing), share unknown |
| **Hivenet** | No third-party supplier program found. Compute is "operated by Hivenet end-to-end" | n/a | No | CONFIRMED (hivenet.com/compute) |

### 2.3 Storage DePIN as an alternative use for drive bays

| Network | Current pay (supplier) | Realistic small-operator earnings | Risks | Status |
|---|---|---|---|---|
| **Storj** | **$1.35/TB-month stored, $1.00/TB egress, $1.00/TB audit/repair**, effective 2026-09-01, paid in **USDC on Ethereum L1** (zkSync dropped). Payout threshold is set by gas fees, about **$50–70 per wallet** in the examples; below it, earnings roll over | Fill rate is limited per /24 subnet: forum anecdotes give about 25 GB/day net across 3 nodes on one subnet (about 0.75 TB/month), and about 6.3 TB/month gross on average across 12,700 subnets. A 12×4 TB R720xd (48 TB) would hold about 9 TB after 12 months, earning roughly **$12–15/mo by month 12 and averaging about $5–10/mo in year 1** (ESTIMATE). That is less than the server's electricity (about $13/mo at 180 W and $0.10/kWh) | **Storj Labs filed Chapter 11 on 2026-07-26** (N.D. W.Va., case 5:26-bk-00512). In July 2026 a Storj employee asked operators how far payouts could be cut. A 450 TB operator says he "just" breaks even. STORJ token is −89% year on year (market cap $7.4M) | Rates CONFIRMED (storj.dev). Chapter 11 CONFIRMED (Storj blog plus press). Fill rates SECONDARY/anecdotal |
| **Filecoin** | Block rewards plus deal payments (USDFC via Filecoin Pay). One unofficial estimate is about 0.0037 FIL/TiB-day, roughly $0.08/TiB-month raw at FIL $0.686 (×10 quality-adjusted for verified deals) | Requires sealing hardware (GPU plus large RAM/NVMe), FIL collateral, verified-deal pipeline and strict uptime. Messari says paid on-chain usage is still small and was mainly pilots in Q1 2026 | Slashing; token price; programme changes (the "Solstice" proposal would redirect part of block rewards) | SECONDARY |

**Takeaway:**
- Filling the drive bays of an old server for storage DePIN does not cover the server's own power bill in year 1. The leading network for small operators is in bankruptcy restructuring.
- The drives themselves, especially enterprise SSDs, are better treated as **resale inventory**. Hetzner cites rising NVMe costs (SECONDARY). I found no 2026 used-HDD/SSD price data.

### 2.4 Running large LLMs on CPU only

**Measured decode speeds on old CPU servers** (CONFIRMED as user reports in llama.cpp discussion #11765, 2025–2026; insiderllm guide updated 2026-10-16):

| Hardware | Memory | Model / quant | Decode tok/s |
|---|---|---|---|
| 1× Xeon E5-2699 v3 (Haswell) | 512 GB DDR4-2133, 4 channels | DeepSeek Q3_K_XL (296 GB) | **2.1** |
| 1× Xeon Gold 6230 (Cascade Lake) | 384 GB DDR4-2666, 6 channels | DeepSeek Q3_K_XL | **3.2** |
| 1× EPYC 7402P (Rome) | 512 GB DDR4-2666, 8 channels | DeepSeek Q3_K_XL | **about 4.2** |
| 2× Xeon Gold 6126 (Skylake) | 384 GB | DeepSeek 671B 2.51-bit | **2–3** (NUMA off) |
| 2× EPYC 7K62 / 1× EPYC 7K62 | 16 / 8 × 64 GB | R1 Q5_K_S | 2.9 / 4.2 (dual socket was slower than single) |
| Broadwell Xeon (E5 v4), ik_llama.cpp | DDR4 | 70B dense | 2.7–5.05 |

**Bandwidth-based estimates for a dual E5-2680 v4 with 8× DDR4-2400** (about 154 GB/s theoretical, about 100 GB/s usable; ESTIMATE):

| Model | Approx. speed | Remarks |
|---|---|---|
| DeepSeek-V3.x/R1 (37B active) | ≤ 3–4 tok/s | Q4 needs ≥ 400 GB RAM |
| Qwen3-235B-A22B | about 5–7 tok/s | |
| Kimi-K2 (32B active, Q4 needs about 550–600 GB, so a 768 GB box) | about 2–3 tok/s | |
| gpt-oss-120b (5.1B active) | about 10–15 tok/s single stream, maybe 50–80 tok/s batched (AVX2 compute ceiling) | Does not need large RAM |

Prompt processing (prefill) on AVX2 CPUs without AMX or AVX-512 is slow (often tens to low hundreds of tok/s). That is a serious handicap because real workloads read far more input than they write.

**API prices the CPU would compete with:**
- OpenRouter `/api/v1/models`, pulled 2026-11-14 (CONFIRMED):

  | Model | Input $/M | Output $/M | Batch tier |
  |---|---|---|---|
  | DeepSeek-V3.2 | 0.26 | **0.38** | — |
  | DeepSeek-V4-Flash | 0.09 | 0.18 | — |
  | Qwen3-235B-A22B-2507 | 0.14 | 0.80 | — |
  | gpt-oss-120b | 0.15 | 0.60 | $0.03 / $0.136 |
  | Kimi-K2.x | 0.50–0.65 | 2.3–3.4 | — |

- DeepSeek official (CONFIRMED, api-docs.deepseek.com):
  - V4.1-Flash: input (cache miss) $0.15/$0.30 off-peak/peak, output **$0.60/$1.20**.
  - V4-Pro: output $1.98/$3.96.

**Table E. Energy cost per token versus market price (ESTIMATE; 350 W at the wall, dual E5 v4).**

| Workload | J/token | kWh per M tokens | Electricity per M tokens at $0.10 / $0.05 | Market price per M output | Verdict |
|---|---|---|---|---|---|
| DeepSeek-671B Q3/Q4 at 3 tok/s | 117 | 32.4 | **$3.24 / $1.62** | $0.38 (V3.2) | Electricity costs 4–8× the selling price |
| Qwen3-235B at 6 tok/s | 58 | 16.2 | $1.62 / $0.81 | $0.80 | Loses money |
| Kimi-K2 at 2.5 tok/s (768 GB box) | 140 | 38.9 | $3.89 / $1.94 | $2.3–2.5 | Loses money |
| gpt-oss-120b, single stream 15 tok/s | 23 | 6.5 | $0.65 / $0.32 | $0.60 list, $0.136 batch | Break-even at best |
| gpt-oss-120b, batched 60 tok/s | 5.8 | 1.6 | $0.16 / $0.08 | $0.136 batch | About parity on power alone, with no margin for hardware and no buyer |

**Monthly revenue at full utilization if every token were sold at API prices (ESTIMATE):**
- DeepSeek at 3 tok/s: 7.9M tokens/month, about **$3/month**.
- gpt-oss-120b batched at 60 tok/s: 158M tokens/month, about **$95/month** at list price and about $21/month at batch price.

**Is there any paid market for this capacity?**
- I found none. Vast.ai has no CPU market. Akash leases for CPU inference would be priced like any other CPU lease (Table C) and compete with APIs that are 10–100× cheaper per token.
- The only plausible niche is a *service*: private, in-country inference for data-residency-sensitive LATAM clients such as hospitals, legal firms and government, sold as an appliance or managed service. Even there, one used GPU is usually better value than a CPU box (INFERENCE).
- Hybrid CPU+GPU engines (KTransformers, ik_llama.cpp) get much of their speedup from AMX/AVX-512 CPUs and DDR5. Old E5 v2–v4 servers lack both (background knowledge, not re-verified this session).

### 2.5 Power draw and net margin

**Table F. Server power (CONFIRMED SPECpower_ssj2008 vendor results, minimal tuned configs; realistic columns are ESTIMATE).**

| Model (SPEC run) | CPUs, RAM in SPEC run | SPEC active idle | SPEC 100% load | Realistic idle with 256–512 GB, 2 PSUs, disks | Realistic full load |
|---|---|---|---|---|---|
| Dell R620 / R720 (2012) | 2× E5-2660/2670, 24 GB | 51–56 W | 230–263 W | **140–180 W** (DDR3: 16–24 DIMMs at about 3–5 W each) | **320–400 W** |
| Dell R630 / R730 (2015–16) | 2× E5-2699 v3/v4, 64–128 GB | 45–51 W | 269–287 W | **110–150 W** | **320–380 W** |
| HPE DL360 Gen9 (2016) | 2× E5-2699 v3, 64 GB | 45 W | 276 W | 110–150 W (DL380 Gen9 similar) | 320–380 W |
| Dell R740 / HPE DL360/DL380 Gen10 (2017–19) | 2× Platinum 8180/8280, 96–192 GB | 49–55 W | 432–469 W | **130–170 W** | **450–550 W** |

Typical real-world additions (ESTIMATE):
- Each 3.5-inch HDD draws 6–9 W.
- Redundant PSUs and fans add 20–40 W.
- The iDRAC/iLO management controller draws 5–10 W even with the server off.
- In hot lowland cities (Barranquilla, Guayaquil, Maracaibo), air conditioning adds 30–60% on top (PUE 1.3–1.6). Bogotá and Quito's cool highland climate largely avoids this.

**Table G. Electricity cost per month by average draw (730 h).**

| Average draw | kWh/mo | $0.05/kWh | $0.10/kWh | $0.15/kWh | $0.20/kWh |
|---|---|---|---|---|---|
| 130 W (mostly idle) | 94.9 | $4.75 | $9.49 | $14.24 | $18.98 |
| 170 W (lightly leased) | 124.1 | $6.21 | $12.41 | $18.61 | $24.82 |
| 250 W | 182.5 | $9.12 | $18.25 | $27.38 | $36.50 |
| 350 W (full CPU load) | 255.5 | $12.78 | $25.55 | $38.32 | $51.10 |
| 450 W (R740 at load) | 328.5 | $16.43 | $32.85 | $49.27 | $65.70 |

**Table H. Net monthly margin, R730 with 2× E5-2680 v4, 56 threads, 256 GB.**
Revenue minus electricity only; excludes depreciation, internet/IPs, cooling overhead, marketplace fees and labour. All figures ESTIMATE.

| Scenario | Revenue/mo | Average W | Revenue per kWh | Net at $0.05 | Net at $0.10 | Net at $0.15 | Net at $0.20 |
|---|---|---|---|---|---|---|---|
| **Akash, unaudited (1.5% utilization), the realistic case** | $4.4 | 140 | $0.04 | **−$0.7** | **−$5.8** | **−$10.9** | **−$16.0** |
| Akash, audited-average (43% CPU / 25% RAM) | $88.8 | 190 | $0.64 | +$81.9 | +$75.0 | +$68.0 | +$61.1 |
| Akash, 100% leased at default bids (theoretical ceiling) | $294.4 | 330 | $1.22 | +$282 | +$270 | +$258 | +$246 |
| Flux, 3× Stratus (needs about $5.8k FLUX collateral) | $55.5 | 200 | $0.38 | +$48.2 | +$40.9 | +$33.6 | +$26.3 |
| Storj with 8× 8 TB HDDs, year-1 average | $7 | 180 | $0.05 | +$0.4 | −$6.1 | −$12.7 | −$19.3 |
| CPU LLM, DeepSeek-V3.2 at 3 tok/s, every token sold at $0.38/M | $3.0 | 350 | $0.01 | −$9.8 | −$22.6 | −$35.3 | −$48.1 |
| CPU LLM, gpt-oss-120b batched at 60 tok/s, 100% sold at $0.60/M list (hypothetical; no buyer) | $94.6 | 350 | $0.37 | +$81.8 | +$69.1 | +$56.3 | +$43.5 |
| *Reference: what OVH charges a retail customer for the same capacity (KS-6-B)* | $96.1 | 190 | $0.69 | +$89 | +$82 | +$75 | +$68 |

Capex for comparison (ESTIMATE; US used market, not LATAM): an R730 barebone with 2× E5-2680 v4 costs roughly $250–450 (background knowledge, not re-verified in 2026), plus 8× 32 GB RDIMM at $800–1,200. **The RAM alone costs more than 10 years of unaudited Akash income.**

### 2.6 Adding GPUs to the old server

**Table I. Old chassis that take GPUs.** Specifications are from vendor documentation as I know it and were not re-fetched this session, because the search budget had run out. Verify against Dell/HPE/Supermicro GPU matrices before buying.

| Chassis | Platform | GPU capacity | Key requirements and limits |
|---|---|---|---|
| **Dell R730** (not R730xd) | 2× E5 v3/v4, PCIe 3.0 | up to **2 double-width 300 W** | GPU enablement kit (x16 risers, GPU power cables), 1100 W PSUs, extra-height-capable shroud. **Consumer cards with top-edge power connectors usually do not fit under a 2U lid**; 2-slot blower cards fit best. R730xd: no double-width GPUs |
| **Dell R740** (not R740xd) | Xeon Scalable gen 1/2, PCIe 3.0 | up to **3 double-width 300 W** or 6 single-width | GPU riser configuration, 1600–2000 W+ PSUs, high-performance fans. Same consumer-card height problem |
| **HPE DL380 Gen9 / Gen10** | E5 v3/v4 / Scalable, PCIe 3.0 | 2–3 double-width (per QuickSpecs) | GPU enablement kit, 3-slot risers, high-performance fans, ≥1400–1600 W PSUs |
| **Supermicro SYS-4028GR-TRT / TRT2** (board X10DRG-O/OT) | 2× E5 v3/v4, 24 DIMMs, PCIe 3.0 x16 via PLX switches | **8 double-width** | 4× 1600 W (2+2) PSUs that need **200–240 V**. At 100–127 V they derate to about 1,000 W, and Colombian, Ecuadorian and Venezuelan homes are 110–120 V. Cards must be ≤2 slots |
| **Supermicro SYS-4029GP-TRT / TRT2** (X11DPG-OT) | Xeon Scalable gen 1/2, PCIe 3.0 | **8 double-width** | 4× 2000 W; 200–240 V |
| **Gigabyte G291-280 / G481-series** | Xeon Scalable | 8 double-width in 2U / 8–10 in 4U | 2200 W-class PSUs at 200–240 V |
| **ASUS ESC4000 G3/G4, ESC8000 G4** | E5 v3/v4 / Scalable | 4 / 8 double-width | High-wattage 200–240 V PSUs |

Common limits:
- PCIe 3.0 (about 16 GB/s per x16 link): acceptable for inference, a handicap for multi-GPU training.
- No AVX-512 on E5 v2–v4.
- Older iDRAC/iLO and BIOS may not boot newer GPUs, which can need firmware updates and Above-4G/Resizable-BAR support.
- 3-slot RTX 3090/4090/5090 retail cards do not fit 2-slot spacing.
- A full 8-GPU box needs a dedicated 2.5–3.5 kW, 220 V circuit.

**Income when filled with GPUs** (CONFIRMED listing prices; Vast.ai public API, 2026-11-14; the 64 cheapest on-demand offers per query, so biased toward the low end):

| GPU | Median $/GPU-h, old-Xeon hosts (E5 v2–v4, Scalable gen 1/2) | Median $/GPU-h, newer hosts | Old-host discount |
|---|---|---|---|
| RTX 3090 | $0.170 (n=15) | $0.211 (n=49) | about −19% |
| RTX 4090 | $0.491 (n=6) | $0.501 (n=58) | about −2% |
| RTX 3060 | $0.066 (n=33) | $0.074 (n=31) | about −11% |
| Tesla V100 | $0.096 (n=59) | $0.121 (n=5) | about −21% |

Example listings on exactly these chassis:
- SYS-4029GP-TRT with 8× RTX 4090 (UK): $4.17/h total, which is $0.521/GPU-h.
- X10DRG-OT (4028GR-TRT board) with 8× RTX 3060: $0.429/h total.
- X10DRG-OT with 8× Quadro RTX 8000: $2.03/h.
- DGX-1 (E5-2698 v4) with 8× V100: $0.75/h.
- X9DRi with 4× RTX 3090 on E5-2695 v2: $0.214/GPU-h.

An 8× RTX 3090 box at $0.17/GPU-h would gross about **$990/month at 100% occupancy**. At about 2.6 kW full load it uses about 1,900 kWh/month, which costs **$95 / $190 / $285 / $380 at $0.05 / $0.10 / $0.15 / $0.20 per kWh** (ESTIMATE). The GPU-focused agents should model occupancy and fees.

**Used 8-GPU chassis prices:** I found no 2026-dated source. My background estimate, which is unverified and pre-2026, is:
- 4028GR-TRT barebone: about $500–1,500.
- 4029GP-TRT and ESC8000 G4: about $1,500–3,000.

Units sold with RAM installed will cost more in 2026 because of DRAM prices.

**Takeaway:** The GPU route turns an old chassis into a GPU host. The income belongs to the GPUs. The old platform costs a modest per-GPU-hour discount plus 220 V and cooling requirements.

### 2.7 DRAM prices: is the RAM worth more than renting the server?

**Table J. Used and refurbished server RAM prices in 2026.**

| Item | Price | $/GB | Year-on-year | Source / date | Status |
|---|---|---|---|---|---|
| DDR4 **32 GB** RDIMM, used | **$100–150** | **$3.1–4.7** | **+335%** | amcompute appraisal, data through 2026-08 | SECONDARY (aggregated sales) |
| DDR4 **64 GB** RDIMM, used | **$250–370** | **$3.9–5.8** | **+285%** | amcompute, through 2026-08 | SECONDARY |
| DDR4 16 GB RDIMM, used | $47–60 | $2.9–3.8 | +250% | amcompute | SECONDARY |
| DDR4 64 GB LRDIMM, used | $100–170 | $1.6–2.7 | +115% | amcompute | SECONDARY |
| DDR4 32 GB RDIMM, refurbished retail | $160–235 | $5.0–7.3 | "30–50% above late-2025" | PC Server & Parts, modified 2026-11-02 | SECONDARY (seller catalog) |
| DDR4 64 GB RDIMM, refurbished retail | about $300 | about $4.7 | — | PC Server & Parts | SECONDARY |
| DDR4-2666 64 GB RDIMM, eBay **asking** | $300–400 | $4.7–6.3 | — | eBay search snippets, 2026 (sold listings blocked) | SECONDARY |
| DDR4-2400 8× 16 GB ECC RDIMM kit | $800–1,000 | $6.3–7.8 | — | insiderllm build guide, prices refreshed 2026-10-15 | SECONDARY |
| New DDR4-3200 32 GB RDIMM | about $400 | about $12.5 | — | PCSP | SECONDARY |
| DDR4 chip spot price trend | 11% below the 2026-09-04 peak by 2026-10-30 | — | — | PCSP post (via search snippet) | SECONDARY |
| DDR3 RDIMM (R620/R720/Gen8) | **no 2026 data found** | — | — | — | GAP |

**Table K. Resale value of the RAM in typical boxes (ESTIMATE from the amcompute ranges).**

| Server RAM | Resale | Equivalent months of *unaudited* Akash income (about $4–11/mo) | Equivalent months of *audited-average* Akash net income at $0.10/kWh |
|---|---|---|---|
| 256 GB as 8× 32 GB (R730/DL380 Gen9) | **$800–1,200** | about 180–270 months | about 11–16 months |
| 256 GB as 16× 16 GB | $750–960 | about 170–220 months | about 10–13 months |
| 512 GB as 16× 32 GB | **$1,600–2,400** | about 210–320 months | about 13–19 months |
| 768 GB as 12× 64 GB (R740/Gen10) | **$3,000–4,440** | about 270–400 months | about 16–24 months |
| 768 GB as 24× 32 GB | $2,400–3,600 | about 220–330 months | about 13–19 months |

**Interpretation:**
- Prices for DDR4 server memory roughly tripled to quadrupled in 12 months. Used RDIMMs did rise alongside new DRAM.
- Selling the RAM today brings in more than a decade of realistic P2P rental income, and more than a year even under an optimistic audited-provider case.
- That is the clearest answer to whether RAM resale beats renting the server: **yes, by a wide margin, for DDR4 RDIMMs.**
- DDR3 is a different story. DDR3 RDIMMs traded at about $0.3–1/GB before the spike (background knowledge), and I found no evidence they shared the AI-driven increase.

---

## 3. What this means for the LATAM used-hardware business

1. **Do not plan on CPU/RAM rental income from P2P or DePIN marketplaces.**
   - Akash is the only real CPU/RAM marketplace, and it is about 74% idle. Unaudited CPU providers run at about 1.5% utilization, and there are 0 LATAM providers online.
   - Vast has no CPU market. Fluence excludes this class of hardware and its token has collapsed. Flux pays inflation (about $18 per 16-thread/64 GB node-month). Storj's operator is in Chapter 11.
   - For an R730 the realistic revenue is **$0–10/month**, which is **below electricity cost at $0.10/kWh and above**.
2. **Value servers as bundles of parts, not as rental capacity.**
   - A DDR4 server with 256 GB is worth $800–1,200 in RDIMMs alone at 2026 resale prices. Sellers in Colombia, Ecuador and Venezuela may still price these servers as "obsolete chassis". The arbitrage hypothesis is **most plausible for the RAM**, not for compute rental.
   - Other agents should compare LATAM purchase prices with these resale values.
   - Execution risks:
     - export/import paperwork and duties;
     - courier shipping (RAM has high value per gram, which helps);
     - testing (memtest) and returns;
     - eBay/marketplace fees of about 13–15%;
     - counterfeit or relabeled modules;
     - US sanctions (OFAC) and payment friction for anything sourced from or paid via Venezuela;
     - **price-cycle timing**: DDR4 spot prices have already slipped about 11% from the September 2026 peak.
3. **Sort hardware by generation.**
   - **DDR4 servers (R630/R730/R740, DL360/DL380 Gen9/Gen10, Supermicro X10/X11):** strip and sell RDIMMs, or resell populated units to buyers who want RAM. Enterprise SSDs and NVMe drives are also resale inventory.
   - **DDR3 servers (R620/R720/Gen8, X9):** low resale and power-inefficient. Treat them as scrap, cheap homelab resale, or occasional GPU hosts (a 4× RTX 3090 X9DRi box lists at $0.214/GPU-h on Vast).
4. **If you keep any chassis, keep the GPU-capable ones.** Examples are 4028GR-TRT/4029GP-TRT, ESC4000/8000 and R740 non-xd, used purely as GPU hosts. Budget for 220 V circuits and 2.5–3.5 kW per 8-GPU box, 2-slot or blower cards, and cooling. Expect old hosts to list about 2–20% below newer hosts per GPU-hour.
5. **The legitimate high-margin use of old CPU servers in LATAM is not P2P.** In-country dedicated servers retail at $600–800/month at HostDime Bogotá and Latitude.sh's EPYC plans start at $456/month. Old hardware could serve local B2B hosting, colocation or private-inference niches, but that is a datacenter/hosting business: Tier-III colocation, IP transit, SLA, support and invoicing. It is a different plan from "rent to Vast/Akash", and its numbers should be modelled separately (colocation cost, bandwidth, customer acquisition).
6. **Electricity sensitivity barely matters for the CPU-only verdict.** Even at $0.05/kWh, the realistic marketplace cases are close to zero. Power price only decides the outcome in the GPU route.

---

## 4. Confidence and gaps

| Topic | Confidence | Notes |
|---|---|---|
| OVH/Hetzner retail prices and stock status | **High** | Pulled from live APIs/feeds on 2026-11-14. EU prices exclude VAT. The Hetzner `live_data_sb_EUR.json` URL in the brief returns 404; the working feed is `/_resources/app/data/app/live_data_sb.json`, which carries EUR and USD |
| Contabo prices | Low | Site blocks bots (HTTP 403). Only PricingSaaS change logs used |
| LATAM retail (HostDime, Latitude) | Medium | Live pages, but HostDime shows no date. Latitude's per-location plan availability not confirmed |
| Akash utilization and default prices | **High** | Live API plus the official pricing script. Actual winning bid prices and network take rate not measured; the default prices are an upper bound |
| Vast CPU-only market | **High** | API shows only disk bundles |
| Fluence eligibility; FLT price | High / High | Fluence provider page dated 2026-11-05; CoinGecko |
| Flux per-node income | Medium | Node counts, subsidy and price are live. The per-tier split is inferred from the PoUW v2 announcement (14 → 12.6 scaled). "Parallel Assets" bonus rewards not counted |
| Golem | Low | Stats endpoints down (502) |
| Storj rates and Chapter 11 | **High** | storj.dev and Storj blog. Fill rates are forum anecdotes (low confidence) |
| Filecoin small-provider economics | Low | Secondary only |
| CPU LLM speeds | Medium | Mix of measured user reports (llama.cpp discussions) and bandwidth estimates. No direct dual-E5 v4 DeepSeek measurement found |
| API prices | **High** | OpenRouter API and DeepSeek docs, 2026-11-14 |
| Power draw | Medium | SPECpower figures are primary but use minimal configs. Realistic figures are estimates; measure with a wall meter |
| Used RDIMM prices | Medium | Aggregated appraisal data through Aug 2026 plus seller catalogs. **eBay sold listings could not be accessed (403)**. Oct–Nov 2026 sold prices not verified |
| DDR3 prices; used 8-GPU chassis prices; LATAM purchase prices | **Gap** | Not found before the search budget ran out. LATAM purchase prices are presumably covered by another agent |
| GPU chassis specifications | Medium | From vendor documentation as I know it; not re-fetched. Verify the exact riser, PSU and CPU-TDP rules per model |

Open questions worth a follow-up:
- 2026 eBay **sold** prices for 32/64 GB DDR4 RDIMM and 16 GB DDR3 RDIMM.
- What used R730 and 4028GR-TRT units actually cost in Colombia and Ecuador (MercadoLibre).
- Whether an Akash audit is achievable from a LATAM colocation site, and what audited providers actually bid.

---

## 5. Sources (all accessed 2026-11-14 unless noted)

**Retail benchmarks**
- Hetzner Server Auction live feed: https://www.hetzner.com/_resources/app/data/app/live_data_sb.json (the brief's `live_data_sb_EUR.json` returns 404)
- Hetzner AX matrix: https://www.hetzner.com/dedicated-rootserver/matrix-ax/
- Hetzner 2026 price increases (SECONDARY): https://www.tomshardware.com/tech-industry/hetzner-to-raise-prices-by-up-to-37-percent-from-april-1 ; https://heise.de/-11185981 ; https://www.datacenterdynamics.com/en/news/german-cloud-firm-hetzner-hikes-prices-by-up-to-50-percent-due-to-drastic-component-price-increases
- OVH public catalog (EU/IE): https://eu.api.ovh.com/v1/order/catalog/public/eco?ovhSubsidiary=IE
- OVH public catalog (US): https://api.us.ovhcloud.com/1.0/order/catalog/public/eco?ovhSubsidiary=US
- OVH availability: https://eu.api.ovh.com/v1/dedicated/server/datacenter/availabilities?planCode=25sk602b (also 24sk602, 24sk702, 24sys043, 24sys053)
- FX, ECB reference rate 2026-11-13: https://api.frankfurter.dev/v1/latest?base=EUR&symbols=USD
- Contabo (SECONDARY): https://pricingsaas.com/companies/contabo (contabo.com returned 403)
- HostDime Colombia: https://www.hostdime.com/colombia-dedicated-servers
- Latitude.sh: https://www.latitude.sh/pricing ; https://www.latitude.sh/locations
- Valebyte LATAM floors (SECONDARY, checked 2026-11-13): https://valebyte.com/en/servers/amd-epyc-9124-3ghz-16-cores-bogota-co

**CPU/RAM marketplaces**
- Akash dashboard: https://console-api.akash.network/v1/dashboard-data
- Akash network capacity: https://console-api.akash.network/v1/network-capacity
- Akash provider list: https://console-api.akash.network/v1/providers?scope=all
- Akash default bid script: https://raw.githubusercontent.com/akash-network/helm-charts/main/charts/akash-provider/scripts/price_script_generic.sh
- Akash provider calculator: https://akash.network/pricing/provider-calculator
- Vast.ai public offers API: https://console.vast.ai/api/v0/bundles/ (queries `num_gpus=0`, `num_gpus` 4/8, per-GPU-model)
- Fluence provider requirements (dated 2026-11-05): https://fluence.ai/employ-your-servers
- Fluence CPU Cloud docs: https://fluence.dev/docs/build/cpu_cloud/overview
- Fluence staking guide (SECONDARY): https://blockworks.co/news/revolutionary-depin-staking-fluence
- Flux PoUW v2 (2025-10-23): https://www.runonflux.com/forking-flux-proof-of-useful-work-v2/
- Flux rewards docs: https://docs.runonflux.com/fluxcloud/dashboard/rewards
- Flux node count: https://api.runonflux.io/daemon/getfluxnodecount
- Flux block subsidy: https://api.runonflux.io/daemon/getblocksubsidy
- Token prices: https://api.coingecko.com/api/v3/simple/price?ids=zelcash,akash-network,golem,fluence-2,storj,filecoin&vs_currencies=usd
- Golem stats page: https://stats.golem.network/ (the API at api.stats.golem.network returned 502)
- SaladCloud pricing: https://salad.com/pricing
- Hivenet: https://www.hivenet.com/compute

**Storage DePIN**
- Storj payouts: https://storj.dev/node/payouts
- Storj forum, July 2026 (payout-cut discussion): https://forum.storj.io/t/helping-the-network-become-profitable-what-can-operators-contribute-while-staying-viable-calculator-inside/32104
- Storj restructuring announcement: https://storj.io/blog/storj-announces-voluntary-financial-restructuring-to-resolve-legacy-liabilities-and-position-the-business-for-growth
- Storj Chapter 11 coverage: https://www.crowdfundinsider.com/2026/07/294125-decentralized-cloud-storage-network-provider-storj-labs-files-for-bankruptcy/ ; https://cointelegraph.com/news/storj-chapter-11-bankruptcy-tokenholder-equity
- Storj USDC switch (SECONDARY): https://www.usagepricing.com/blueprint/activity/storj-2026-09-25-usdc-replaces-storj-token
- Storj fill-rate anecdotes: https://forum.storj.io/t/very-low-utilization/28300?page=2 ; https://forum.storj.io/t/there-are-12-700-subnets-with-nodes-how-is-traffic-distributed/31110
- Filecoin: https://messari.io/report/filecoin-solstice-and-the-shift-to-a-demand-driven-service-economy ; https://filecoin.io/blog/the-2026-filecoin-network-strategy ; https://docs.filecoin.io/mine ; https://portfolio-indiebuidl.vercel.app/blog/filcoin-fil-decentralized-storage-moat-and-token-capture-assessment (SECONDARY)

**CPU-only LLM inference**
- llama.cpp CPU DeepSeek reports: https://github.com/ggml-org/llama.cpp/discussions/11765
- CPU-only LLM guide (updated 2026-10-16): https://insiderllm.com/guides/cpu-only-llms-what-actually-works/
- OpenRouter model prices: https://openrouter.ai/api/v1/models
- DeepSeek API pricing: https://api-docs.deepseek.com/quick_start/pricing

**Power**
- SPECpower_ssj2008 results: https://www.spec.org/power_ssj2008/results/power_ssj2008.html

**DRAM prices**
- amcompute 32 GB DDR4 RDIMM appraisal (also lists 16 GB, 64 GB and 64 GB LRDIMM): https://www.amcompute.com/appraisals/ddr4-32gb-rdimm
- PC Server & Parts, 2026 server RAM price crisis: https://pcserverandparts.com/news/refurbished-ddr4-server-memory-2026-server-ram-price-crisis/
- eBay 64 GB DDR4 RDIMM asking prices (SECONDARY, sold listings returned 403): https://www.ebay.com/sch/i.html?_nkw=64gb+ddr4+ecc+rdimm&_sop=12

Raw pulls, parsing scripts and calculations are in `/tmp/claude-0/-home-user-cowork-ulricht-project/6a906045-5aa8-5271-a0fd-a23952c77e55/scratchpad/agent05/`. That is scratch space and may be cleared.
