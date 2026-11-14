# 01 — Vast.ai from the Host's Perspective: Prices, Fees, Requirements, Utilization, Revenue

**Agent:** 01 · **Research date:** 2026-11-14 (Saturday) · **Live data snapshot:** 2026-11-14, 12:19–12:53 UTC
**Scope:** Vast.ai only, seen from the host (supplier) side. Other marketplaces, hardware costs in LATAM, electricity and logistics belong to other agents.

> **How to read this report.** Every number has a label:
> **CONFIRMED** means it comes from a primary source (Vast docs or pages, Vast's public API or feed, Stripe or Wise docs) on the date given.
> **COMPUTED** means I calculated it from the live Vast API pull described in §2.1.
> **INFERENCE/ESTIMATE** means it is my reasoning from data and is not stated by Vast.
> Prices are in USD per GPU-hour ($/GPU-h). "Renter price" is what Vast's search shows renters. "Host-side" is what the host receives.
> Note: WebSearch was unavailable during this task because the shared search budget was used up. All sources below were fetched directly: Vast docs, pages, API and feed, plus Stripe and Wise pages. I found no third-party utilization trackers (see §4).

---

## 1. Executive summary

- **Vast keeps about 25% of what renters pay.** The host is charged nothing explicitly. Vast's hosting FAQ says *"The rate you set in the platform is the rate you receive — there is no fee or commission deducted from your earnings. Vast sets its own pricing to end users…"* (CONFIRMED, vast.ai/hosting).
  - In the live API, 96% of community and 89% of datacenter per-GPU renter prices become round numbers when multiplied by 0.75. Storage prices (98%) and bandwidth prices behave the same way.
  - So renter price ≈ host ask ÷ 0.75. That is a **+33% markup on the host price**, and the **host receives about 75% of gross renter spend** (INFERENCE, strong). Wise, PayPal or Stripe fees come on top.
- **Market size (COMPUTED, 2026-11-14):** **8,928 listed machines, 26,501 GPUs, 2,238 hosts.**
  - North America has 11.5k GPUs, Europe 7.6k and Asia/Middle East 6.7k.
  - **Latin America has only 260 GPUs on 178 machines (about 1.0% of supply).** Colombia has 1 machine (1× RTX 5090), Ecuador has 2 (1× RTX 3090 each, unverified) and **Venezuela has none**. Brazil (89 GPUs), Mexico (52), Argentina (51) and Chile (34) make up most of the region.
- **Live renter prices, medians (COMPUTED):**

  | GPU | Median $/GPU-h | GPU | Median $/GPU-h |
  |---|---|---|---|
  | RTX 3060 | 0.073 | A100 SXM4 80GB | 1.15 |
  | RTX 3080 | 0.133 | H100 SXM | 2.33 |
  | **RTX 3090** | **0.213** | H200 | 5.19 |
  | **RTX 4090** | **0.480** | B200 | 10.00 |
  | **RTX 5090** | **0.667** | **V100 32GB** | **0.080** |
  | RTX A4000 | 0.096 | **P40** | **≈0.20 (n=10)** |
  | RTX A6000 | 0.480 | **2080 Ti** | **0.080** |
  | RTX PRO 6000 WS | 1.467 | **1080 Ti** | **0.067** |

  - Host-side, multiply by 0.75. For example, an RTX 3090 earns about **$0.16/h** for the host and an RTX 4090 about **$0.36/h**.
- **Utilization looks high but depends heavily on status (COMPUTED, single snapshot).** About **74% of all listed GPUs** (bounds 72–76%) were under on-demand or reserved contracts. Interruptible usage is not visible in this data.
  - **Verified machines: about 82%. Unverified: about 47%. Deverified: about 45%.**
  - Reliability below 0.95 gives about 42–51% utilization; 0.995 or higher gives about 83%.
  - A new host starts unverified with low reliability, so **plan on roughly 45–50% for the first weeks.**
- **Price matters less than status.** Machines priced 20–50% below their model's median are only about 1 point more utilized (82%) than machines at the median (81%). Pricing 5–60% above the median drops utilization to 64–70%.
  - Datacenter ("Secure Cloud") machines command a **1.46× price** at the same utilization (78%).
  - Machines with VMs enabled get a **1.20× price**.
- **Prices have risen over 90 days for consumer GPUs and Blackwell.** Vast's public pricing feed shows these daily-median changes from 2026-08-16 to 2026-11-13 (CONFIRMED feed data):
  - RTX 3090 +39%, RTX 4090 +37%, RTX 5090 +51%, B200 +55%.
  - **Old datacenter cards fell:** V100 −57%, P100 −60%, A100 SXM4 −21%.
- **Payouts (CONFIRMED, docs.vast.ai):**
  - Only **Wise, PayPal or Stripe**. There is **no ACH, SWIFT or wire** payout, and the payout doc lists no crypto option.
  - The **minimum is $20**. Invoices are generated every Friday and paid the following Friday, so the first payout takes about 2 weeks.
  - Vast withholds no tax and does not handle VAT.
  - For **Colombia and Venezuela**, Stripe's self-serve cross-border payouts and its Global Payouts list do **not** include them. Ecuador is listed for Stripe Global Payouts (USD wire), but it is unconfirmed which Stripe product Vast uses.
  - Wise pays out in COP to Colombia but does not list Ecuador or Venezuela. PayPal works in all three, but I could not verify Venezuelan withdrawal limits.
  - **INFERENCE:** a host entity or payout account in Spain/EU or the US is the low-friction route.
- **Gross revenue for the host after Vast's cut, per GPU per month (730 h), at 30% / 50% / 70% utilization (COMPUTED from median prices):**

  | GPU | 30% | 50% | 70% |
  |---|---|---|---|
  | RTX 3060 | $12 | $20 | $28 |
  | RTX 3080 | $22 | $36 | $51 |
  | **RTX 3090** | **$35** | **$58** | **$82** |
  | **RTX 4090** | **$79** | **$131** | **$184** |
  | RTX 5090 | $110 | $182 | $255 |
  | RTX A6000 | $79 | $131 | $184 |
  | A100 SXM4 | $175 | $292 | $409 |
  | **V100** | **$13** | **$22** | **$31** |

  - These figures are before electricity, internet, depreciation and payout fees.
- **Verification has strict requirements (CONFIRMED):**
  - Ubuntu Server 22.04 or 24.04.
  - **At least 500 Mbps download and 500 Mbps upload** over wired Ethernet.
  - **A public IPv4 address. CGNAT is not allowed.** At least 5 forwarded ports per GPU (100 recommended).
  - **System RAM at least 0.95 × total VRAM.** At least 2 physical CPU cores per GPU, a 200 GB SSD dedicated to Docker, more than 7 GB VRAM per GPU, CUDA 11.8 or newer.
  - Reliability above 90%, and the machine must be dedicated (no mining or gaming).
  - **Datacenter/Secure Cloud tier:** an ISO/IEC 27001-certified facility, a registered business, at least 5 GPU servers, and identity verification.

---

## 2. Detailed findings

### 2.1 Method: live pull from the public offers API (COMPUTED)

- **Endpoint:** `POST https://console.vast.ai/api/v0/bundles/` with a JSON query. This is the endpoint that `vastai search offers` uses in `vast.py` of github.com/vast-ai/vast-cli. It works **without authentication**. `cloud.vast.ai` serves the same API.
- **API quirk that matters for anyone repeating this:** the endpoint returns **at most 64 rows per query**, and it truncates silently. A query can return fewer than 64 rows and still be incomplete, because rows are collapsed per machine and bundle size. Filtering by price band was therefore unreliable.
  - I swept the **`machine_id` space in adaptive ranges**: 2,235 calls returned 15,625 bundles on 8,928 machines.
  - A second sweep used **`rentable=true`** in groups of 5 or fewer machines and 16 or fewer GPUs, to count free GPUs per machine (2,355 calls).
  - In a validation re-query about 10 minutes later, 7 of 120 random machines gave a different free-GPU count. That is consistent with rental churn, with a slight bias toward undercounting free GPUs, i.e. overstating utilization by perhaps 1–3 points.
- **Fields used:**
  - Per-GPU renter price = `dph_base / num_gpus`. This excludes storage.
  - `min_bid` gives the interruptible price.
  - `gpu_frac` gives the total GPUs in the machine.
  - Also used: `rentable`, `verification` (verified, unverified or deverified), `hosting_type` (1 = datacenter; checked against the `datacenter=true` filter), `reliability`, `inet_up`/`inet_down`, `cpu_ram`, `disk_space`, `storage_cost` ($/GB-month), `internet_up/down_cost_per_tb`, and `geolocation`.
- **How utilization is computed:** each machine lists bundles of 1, 2, 4, 8… GPUs. A bundle refers to specific GPU IDs and is flagged `rentable=false` if any of its GPUs is under contract.
  - Free GPUs = the largest rentable bundle. Upper and lower bounds come from the next bundle size.
  - Utilization = (total GPUs − free GPUs) / total GPUs.
  - **INFERENCE check:** my free-GPU counts are the same order of magnitude as the "available" counts in Vast's own public pricing feed. For example, the RTX 5090 has 1,123 free *verified* GPUs in my data versus 1,022 "available" in the feed an hour earlier.
- **A compact summary is saved at** `/tmp/claude-0/-home-user-cowork-ulricht-project/6a906045-5aa8-5271-a0fd-a23952c77e55/scratchpad/agent01/vast_pull_summary_2026-11-14.json` (92 KB). The scripts are in `/tmp/claude-0/-home-user-cowork-ulricht-project/6a906045-5aa8-5271-a0fd-a23952c77e55/scratchpad/agent01/scripts/`.

### 2.2 Live prices and utilization by GPU model (COMPUTED, 2026-11-14 12:41 UTC)

GPU-weighted, so each listed GPU counts once. All verification tiers are included. Renter-facing $/GPU-h, excluding storage and bandwidth.

| GPU | machines | GPUs listed | renter p25 | renter median | renter p75 | host-side median (×0.75) | median of RENTED GPUs | median of FREE GPUs | interruptible min-bid median | est. utilization (lo–hi) |
|---|---|---|---|---|---|---|---|---|---|---|
| RTX 3060 | 458 | 1139 | 0.060 | 0.073 | 0.099 | 0.055 | 0.073 | 0.076 | 0.060 | 73–77% |
| RTX 3060 Ti (8GB) | 67 | 118 | 0.067 | 0.087 | 0.160 | 0.065 | – | – | – | 64% |
| RTX 3070 | 79 | 173 | 0.080 | 0.107 | 0.147 | 0.080 | 0.107 | 0.093 | 0.080 | 63–67% |
| RTX 3080 | 130 | 235 | 0.107 | 0.133 | 0.160 | 0.100 | 0.133 | 0.133 | 0.120 | 54–57% |
| RTX 3080 Ti | 74 | 154 | 0.127 | 0.185 | 0.200 | 0.139 | – | – | – | 62% |
| **RTX 3090** | **835** | **2277** | 0.187 | **0.213** | 0.267 | **0.160** | 0.207 | 0.227 | 0.180 | **80–83%** |
| RTX 3090 Ti | 45 | 64 | 0.213 | 0.253 | 0.267 | 0.190 | – | – | – | 85% |
| RTX 4060 Ti | 110 | 272 | 0.120 | 0.147 | 0.187 | 0.110 | 0.157 | 0.147 | 0.113 | 64–70% |
| RTX 4070 | 32 | 92 | 0.093 | 0.120 | 0.167 | 0.090 | 0.093 | 0.167 | 0.120 | 60% |
| RTX 4070S | 48 | 234 | 0.093 | 0.097 | 0.107 | 0.073 | 0.107 | 0.093 | 0.093 | 63–68% |
| RTX 4080 | 46 | 90 | 0.227 | 0.248 | 0.267 | 0.186 | 0.250 | 0.240 | 0.227 | 68–71% |
| RTX 4080S | 51 | 121 | 0.213 | 0.241 | 0.307 | 0.180 | 0.253 | 0.240 | 0.200 | 71–74% |
| **RTX 4090** | **1177** | **3653** | 0.427 | **0.480** | 0.560 | **0.360** | 0.467 | 0.529 | 0.400 | **76–80%** |
| RTX 5060 Ti | 302 | 858 | 0.120 | 0.133 | 0.195 | 0.100 | 0.133 | 0.147 | 0.120 | 66–70% |
| RTX 5070 Ti | 273 | 565 | 0.171 | 0.200 | 0.267 | 0.150 | 0.200 | 0.240 | 0.200 | 60–64% |
| RTX 5080 | 311 | 928 | 0.200 | 0.241 | 0.267 | 0.181 | 0.227 | 0.267 | 0.213 | 66–68% |
| **RTX 5090** | **2335** | **7164** | 0.533 | **0.667** | 0.800 | **0.500** | 0.651 | 0.707 | 0.560 | **74–78%** |
| RTX A4000 | 133 | 431 | 0.093 | 0.096 | 0.120 | 0.072 | 0.096 | 0.120 | 0.096 | 70–73% |
| RTX A5000 | 37 | 115 | 0.200 | 0.227 | 0.231 | 0.170 | 0.227 | 0.227 | 0.213 | 56–59% |
| RTX A6000 | 57 | 167 | 0.400 | 0.480 | 0.480 | 0.360 | 0.480 | 0.467 | 0.333 | 90–92% |
| RTX 6000 Ada | 45 | 133 | 0.620 | 0.665 | 0.787 | 0.499 | 0.667 | 0.627 | 0.600 | 89–90% |
| RTX PRO 4000 | 56 | 153 | 0.253 | 0.279 | 0.373 | 0.209 | 0.267 | 0.333 | 0.253 | 50–55% |
| RTX PRO 5000 (48GB) | 69 | 200 | 0.667 | 0.776 | 0.887 | 0.582 | – | – | – | 81% |
| RTX PRO 6000 Blackwell WS | 326 | 646 | 1.373 | 1.467 | 1.733 | 1.100 | 1.467 | 1.600 | 1.095 | 80–81% |
| RTX PRO 6000 Blackwell Server | 165 | 840 | 1.520 | 1.680 | 2.000 | 1.260 | 1.600 | 2.000 | 1.547 | 69–74% |
| RTX PRO 6000 Max-Q | 172 | 446 | 1.213 | 1.387 | 1.650 | 1.040 | 1.367 | 1.540 | 0.989 | 81–84% |
| A40 | 28 | 103 | 0.600 | 0.680 | 0.733 | 0.510 | 0.600 | 0.733 | 0.227 | 64–70% |
| L40 | 5 | 13 | 0.453 | 0.453 | 0.507 | 0.340 | 0.453 | 1.333 | 0.400 | 69% |
| L40S | 61 | 295 | 0.467 | 0.600 | 0.800 | 0.450 | 0.600 | 0.800 | 0.533 | 74–80% |
| L4 | 25 | 52 | 0.307 | 0.347 | 0.480 | 0.260 | 0.333 | 0.347 | 0.333 | 50–54% |
| A10 | 5 | 23 | 0.227 | 0.240 | 0.240 | 0.180 | 0.240 | 0.827 | 0.240 | 65–70% |
| A100 PCIe 40GB | 36 | 152 | 0.508 | 0.611 | 0.733 | 0.458 | – | – | – | 74% |
| A100 PCIe 80GB | 18 | 64 | 0.867 | 0.867 | 1.133 | 0.650 | – | – | – | 77% |
| A100 SXM4 40GB | 43 | 171 | 0.533 | 0.560 | 0.733 | 0.420 | – | – | – | 68% |
| A100 SXM4 80GB | 46 | 265 | 1.067 | 1.147 | 1.287 | 0.860 | – | – | – | 93% |
| H100 PCIe | 9 | 31 | 2.667 | 2.800 | 3.203 | 2.100 | 2.667 | 3.203 | 2.922 | 77–84% |
| H100 SXM | 38 | 163 | 1.840 | 2.333 | 3.333 | 1.750 | 2.333 | 2.667 | 1.800 | 78–83% |
| H100 NVL | 17 | 41 | 2.800 | 3.120 | 3.413 | 2.340 | 3.120 | 2.800 | 2.267 | 76–83% |
| H200 | 34 | 242 | 4.342 | 5.188 | 7.029 | 3.891 | 5.188 | 5.188 | 4.523 | 74–81% |
| H200 NVL | 59 | 265 | 3.880 | 4.000 | 4.267 | 3.000 | 4.000 | 4.176 | 3.600 | 71–77% |
| B200 | 45 | 339 | 8.750 | 10.000 | 10.625 | 7.500 | 10.625 | 10.000 | 8.750 | 74–79% |
| B300 | 16 | 128 | 10.469 | 10.750 | 11.875 | 8.062 | 10.750 | 10.750 | 8.750 | 75–83% |
| **Tesla V100 32GB** | 119 | 834 | 0.067 | **0.080** | 0.120 | 0.060 | – | – | – | 81% |
| Tesla V100 16GB | 17 | 68 | 0.093 | 0.093 | 0.124 | 0.070 | – | – | – | 54% |
| **Tesla P40** | 6 | 10 | 0.105 | 0.200 | 0.313 | 0.150 | 0.293 | 0.105 | 0.166 | 70–80% (n tiny) |
| **Tesla P100** | 8 | 24 | 0.093 | 0.093 | 0.093 | 0.070 | 0.093 | 0.093 | 0.084 | **25–38%** |
| **Tesla T4** | 10 | 32 | 0.082 | 0.141 | 0.148 | 0.105 | 0.148 | 0.112 | 0.055 | **41–44%** |
| **RTX 2080 Ti** | 40 | 127 | 0.067 | 0.080 | 0.131 | 0.060 | 0.080 | 0.093 | 0.080 | **43–52%** |
| **GTX 1080 Ti** | 19 | 35 | 0.063 | 0.067 | 0.067 | 0.050 | 0.067 | 0.067 | 0.053 | 60–66% |
| Titan RTX | 9 | 13 | 0.200 | 0.200 | 0.240 | 0.150 | – | – | – | 38% |
| Quadro RTX 8000 (48GB) | 11 | 29 | 0.252 | 0.253 | 0.267 | 0.190 | – | – | – | 84% |
| CMP 170HX (mining card) | 40 | 173 | 0.400 | 0.440 | 0.513 | 0.330 | 0.467 | 0.400 | 0.373 | 61–64% |

Notes:
- **Model names on Vast.** "RTX PRO 6000 S" is the Server Edition, "WS" the Workstation edition and "Max-Q" the 300 W edition.
- **Supply is concentrated.** The RTX 5090 (7.2k GPUs) and RTX 4090 (3.7k) dominate, followed by the RTX 3090 (2.3k) and RTX 3060 (1.1k).
- **A rented-versus-free price gap is small.** Within a model, the median price of rented GPUs is usually equal to or slightly below the median of free GPUs. Cheaper offers fill first, but the clearing price is close to the median.
- **Interruptible floors** (`min_bid` ÷ on-demand price, per machine) are p10 0.49, p25 0.67, median 0.875 and p75 1.0. Many hosts set the floor at, or close to, their on-demand price. Vast's own guide calls this a common mistake and advises setting it near the cost of power.

### 2.3 Cross-check with Vast's public pricing feed and 90-day trend (CONFIRMED, feed updated 2026-11-14T11:30:22Z)

Source: `https://storage.googleapis.com/vast-public-gpu-pricing/gpu-pricing-public.json`, linked from https://vast.ai/pricing.md.
- The "current" block covers *available* offers only: min, p10 and median, renter-facing.
- The "daily" series has 90 days of daily medians. Its level is about 0.75× the live renter median for most models, so it may be host-side or based on rented contracts. That is UNVERIFIED, so use the series for **trend direction only**.
- The feed's terms: *"Free for display and citation with attribution."*

| GPU | feed "available" | current min | current p10 | current median | daily median: 08-16 → 09-15 → 10-15 → 11-13 | 90-day change |
|---|---|---|---|---|---|---|
| RTX 3060 | 208 | 0.040 | 0.054 | 0.074 | 0.043 → 0.045 → 0.060 → 0.055 | +29% |
| RTX 3080 | 98 | 0.092 | 0.096 | 0.135 | 0.079 → 0.080 → 0.133 → 0.100 | +27% |
| RTX 3090 | 264 | 0.094 | 0.148 | 0.214 | 0.116 → 0.120 → 0.150 → 0.160 | +39% |
| RTX 4080S | 59 | 0.160 | 0.161 | 0.235 | 0.100 → 0.140 → 0.229 → 0.170 | +70% |
| RTX 4090 | 609 | 0.134 | 0.400 | 0.494 | 0.270 → 0.370 → 0.400 → 0.370 | +37% |
| RTX 5060 Ti | 291 | 0.091 | 0.107 | 0.134 | 0.080 → 0.128 → 0.126 → 0.100 | +25% |
| RTX 5080 | 175 | 0.175 | 0.193 | 0.263 | 0.130 → 0.220 → 0.500 → 0.200 | +54% |
| RTX 5090 | 1022 | 0.387 | 0.467 | 0.668 | 0.327 → 0.500 → 0.560 → 0.495 | +51% |
| RTX A4000 | 152 | 0.071 | 0.072 | 0.108 | 0.100 → 0.068 → 0.100 → 0.090 | −10% |
| RTX A6000 | 20 | 0.375 | 0.375 | 0.467 | 0.333 → 0.350 → 0.300 → 0.350 | +5% |
| RTX PRO 6000 WS | 92 | 1.001 | 1.269 | 1.535 | 0.900 → 1.143 → 1.208 → 1.206 | +34% |
| L40S | 66 | 0.441 | 0.441 | 0.800 | 0.350 → 0.350 → 0.350 → 0.510 | +46% |
| A100 PCIe | 60 | 0.485 | 0.485 | 0.668 | 0.600 → 0.522 → 0.550 → 0.500 | −17% |
| A100 SXM4 | 77 | 0.308 | 0.376 | 0.801 | 0.800 → 0.685 → 0.580 → 0.630 | −21% |
| H100 SXM | 24 | 1.841 | 1.841 | 2.667 | 2.038 → 1.700 → 2.200 → 2.000 | −2% |
| H200 | 57 | 1.975 | 2.501 | 4.343 | 3.212 → 3.030 → 3.450 → 3.868 | +20% |
| B200 | 86 | 7.501 | 8.033 | 10.000 | 5.250 → 6.200 → 6.700 → 8.125 | +55% |
| Tesla V100 | 204 | 0.054 | 0.055 | 0.118 | 0.139 → 0.107 → 0.100 → 0.060 | **−57%** |
| Tesla P40 | 7 | 0.106 | 0.106 | 0.106 | 0.079 → 0.050 → 0.067 → 0.072 | −8% |
| Tesla P100 | 19 | 0.044 | 0.044 | 0.095 | 0.105 → 0.070 → 0.070 → 0.042 | **−60%** |
| Tesla T4 | 25 | 0.047 | 0.047 | 0.149 | 0.111 → 0.110 → 0.111 → 0.110 | −1% |
| RTX 2080 Ti | 81 | 0.063 | 0.067 | 0.093 | 0.060 → 0.060 → 0.072 → 0.060 | 0% |
| GTX 1080 Ti | 13 | 0.061 | 0.061 | 0.067 | 0.048 → 0.050 → 0.050 → 0.050 | +5% |

### 2.4 Geography: US/EU/Asia versus Latin America (COMPUTED)

**Supply and utilization by region:**

| Region | machines | GPUs | GPU-weighted utilization (est.) |
|---|---|---|---|
| North America (US + CA) | 3,582 | 11,511 | 75% |
| Europe | 2,637 | 7,641 | 73% |
| Asia / Middle East | 2,362 | 6,727 | 73% |
| **Latin America** (incl. Puerto Rico) | **178** | **260** | 77% |
| Other (AU, NZ, ZA, RU…) | 169 | 362 | 67% |

- **Top countries by GPUs:** US 8,959, Canada 2,552, China 1,590, Korea 1,330, Taiwan 1,173, Japan 1,150, Czechia 895, Norway 704, Vietnam 644, UK 605. Spain has 503 GPUs on 230 machines at 80% utilization.

**Latin America by country:**

| Country | machines | GPUs | hosts | verified machines | util. (est.) | price index vs global same-GPU median | median upload Mbps | median reliability |
|---|---|---|---|---|---|---|---|---|
| Brazil | 57 | 89 | 32 | 28 | 67% | 0.94 | 410 | 0.989 |
| Mexico | 44 | 52 | 13 | 33 | 77% | 0.88 | 725 | 0.988 |
| Argentina | 36 | 51 | 11 | 32 | 80% | 1.00 | 693 | 0.994 |
| Chile | 20 | 34 | 8 | 19 | 82% | 1.00 | 875 | 0.996 |
| Puerto Rico (US) | 14 | 27 | 3 | 14 | 100% | 1.05 | 2,102 | 0.993 |
| Peru | 2 | 2 | 2 | 1 | 50% | 0.81 | 795 | 0.983 |
| **Ecuador** | **2** | **2** | 1 | 0 | 50% | 0.93 | 655 | 0.985 |
| **Colombia** | **1** | **1** | 1 | 1 | 100% | 1.00 | 872 | 0.983 |
| Panama | 1 | 1 | 1 | 1 | 100% | 1.07 | 457 | 0.994 |
| Paraguay | 1 | 1 | 1 | 0 | 0% | 0.90 | 931 | 0.978 |
| **Venezuela** | **0** | **0** | – | – | – | – | – | – |

- **The three target countries in detail:**
  - Colombia: 1× RTX 5090 at $0.667, verified, rented.
  - Ecuador: 2× single RTX 3090 at $0.199, both unverified, one rented.
  - Venezuela: none.

**Same GPU, Latin America versus global:**

| GPU | LatAm GPUs | LatAm median | global median | LatAm / global | LatAm util | global util |
|---|---|---|---|---|---|---|
| RTX 5090 | 76 | 0.667 | 0.667 | 1.00 | 84% | 76% |
| RTX 3090 | 63 | 0.200 | 0.213 | 0.94 | 87% | 81% |
| RTX 4090 | 38 | 0.413 | 0.480 | 0.86 | 76% | 78% |
| RTX 3080 | 11 | 0.167 | 0.133 | 1.25 | 36% | 56% |
| RTX 5060 Ti | 8 | 0.120 | 0.133 | 0.90 | 38% | 68% |
| RTX 5080 | 7 | 0.253 | 0.241 | 1.05 | 86% | 67% |

- **Overall, Latin American offers are priced about 4% below the global same-GPU median** (price index 0.96) and are about as utilized.
- **Renters do not appear to penalize LatAm location much** for popular cards, but the sample is tiny: 260 GPUs. (INFERENCE)
- **Regional price differences elsewhere are modest.** Asia is usually 5–15% cheaper (RTX 5090 $0.573 vs $0.667 in North America; H100 SXM $1.84 vs $3.07 in Europe). Europe is slightly more expensive for consumer cards (RTX 5090 $0.715).

### 2.5 What correlates with utilization and price (COMPUTED)

The pool is 16 main models with 20k GPUs. "Price index" is a machine's $/GPU-h divided by its model's median.

| Factor | Bucket → utilization (median price index) |
|---|---|
| **Verification** | **verified 82% (1.00)**, unverified 47% (0.88), deverified 45% (1.00) |
| **Datacenter tier** | community 76% (1.00), **datacenter 78% (1.46)** |
| **Reliability** | <0.90: 51%; 0.90–0.95: 42%; 0.95–0.98: 59%; 0.98–0.99: 75%; 0.99–0.995: 78%; **≥0.995: 83%** |
| **Price index** | <0.8: 82%; 0.8–0.95: 81%; 0.95–1.05: 81%; 1.05–1.25: 68%; 1.25–1.6: 70%; ≥1.6: 64% |
| **Upload bandwidth** | **<100 Mbps: 59% (0.90)**; 100–500: 76%; 500–1000: 76%; 1–5 Gbps: 76% (1.10); ≥5 Gbps: 79% (1.20) |
| **System RAM per GPU** | **<16 GB: 58%**; 16–32: 75%; 32–64: 77%; 64–128: 80% (1.06); ≥128: 76% (1.19) |
| **Disk per GPU** | <100 GB 73% … ≥1 TB 81% (1.07) |
| **GPUs per machine** | 1: 81%; 2–3: 76%; 4–7: 77%; 8: 74%; >8: 70% |
| **VMs enabled** | 76% at **1.20×** price; no VMs 76% at 1.00× |

- **Reliability and search ranking:**
  - Reliability is shown publicly per machine. Across all listings the distribution is p10 0.971, p25 0.988, median 0.995, p90 0.9985.
  - The API also exposes a `reliability_mult`, which falls steeply as reliability falls:
    - reliability 0.937 → multiplier 0.62
    - 0.959 → 0.71
    - 0.981 → 0.84
    - 0.991 → 0.92
  - The CLI's default sort is `score`, which appears to combine DLPerf per dollar with this multiplier. That is INFERENCE from the fields. Vast's docs confirm the auto-sort "is comprised of both ranking various factors as well as an element of randomness" (CONFIRMED).
  - Offline time therefore costs both search rank and verification eligibility.
- **Other listing facts:**
  - About 51% of machines have a static IP and 6% have VMs enabled.
  - Offer durations (time to the offer end date) are p25 16 days, median 34 days, p75 103 days.
  - About 18% of bundles offer reserved discounts (`credit_discount_max` of 5–40%).

### 2.6 Non-GPU charges that hosts set (COMPUTED, per machine)

Renter-facing values; host-side is ×0.75 (INFERENCE).

| Charge | p10 | p25 | median | p75 | p90 | share at $0 |
|---|---|---|---|---|---|---|
| Storage, $/GB-month (renter) | 0.133 | 0.200 | 0.200 | 0.333 | 0.533 | 0% |
| → host-side $/GB-month | 0.10 | 0.15 | **0.15** | 0.25 | 0.40 | |
| Upload bandwidth, $/TB (renter) | 1.33 | 4.00 | 4.00 | 10.67 | 33.33 | 1% |
| Download bandwidth, $/TB (renter) | 1.33 | 2.67 | 2.73 | 9.33 | 33.33 | 1% |
| → host-side $/TB (median up / down) | | | **3.00 / 2.05** | | | |

- Storage is billed for as long as the renter's instance exists, **including while it is stopped**. Bandwidth is billed per byte (CONFIRMED, docs.vast.ai pricing).
- VMs earn no bandwidth revenue (CONFIRMED, docs.vast.ai/host/vms).
- **INFERENCE:** storage plausibly adds about $5–20 per GPU-month (e.g. 50–100 GB at $0.15). Bandwidth is minor unless the host's link is unmetered and renters move a lot of data.

### 2.7 Fees, payouts and countries

| Item | Finding | Status / source |
|---|---|---|
| Explicit host commission | None: "The rate you set in the platform is the rate you receive — there is no fee or commission deducted… Vast sets its own pricing to end users" | CONFIRMED, vast.ai/hosting FAQ (2026-11-14) |
| Implicit take rate | Renter price = host price ÷ 0.75 for GPU, storage and bandwidth. Vast keeps 25% of renter spend, which is a 33% markup | INFERENCE (strong). Holds for 96% of community and 89% of datacenter per-GPU prices and 98% of storage prices in the live API |
| Earnings calculator wording | "Customer-facing prices may differ because the marketplace also accounts for platform operations, support, demand generation…". It also says **"Vast does not publish per-GPU utilization figures"** | CONFIRMED, vast.ai/hosting/calculator |
| Payout methods | **Wise, PayPal, Stripe only.** "Direct bank transfers, ACH payments, wire transfers, and SWIFT payments are not available." The payout doc lists no crypto option | CONFIRMED, docs.vast.ai/host/payment |
| Minimum and schedule | **$20 minimum**. Invoice generated weekly on Friday, paid the next Friday, so the first payout takes up to about 2 weeks. Provider processing time comes on top | CONFIRMED, same |
| Requirement on the host's payout account | The host must be able to receive **B2B payments** in their country via the chosen provider | CONFIRMED, same |
| Tax | Vast withholds no tax and gives no tax documents to non-US hosts. Vast does not collect or remit VAT | CONFIRMED, docs.vast.ai/host/guide-to-taxes |
| Sanctions | Vast's Terms exclude Cuba, Iran, North Korea, Syria and occupied regions of Ukraine, plus SDN-listed parties. **Venezuela is not in the comprehensive-embargo list.** Counterparties tied to the Government of Venezuela are blocked under US sanctions (EO 13884) | CONFIRMED for the Terms (vast.ai/terms). EO 13884 is from my background knowledge |
| Stripe for CO / EC / VE | Self-serve Connect cross-border payouts reach only US, UK, EEA, Canada and Switzerland. Stripe **Global Payouts** (US sender) lists **Ecuador (USD wire)**, Peru, Mexico, Panama and Costa Rica, but **not Colombia, Venezuela, Brazil, Argentina or Chile**. Which Stripe product Vast uses is unknown; its tax page mentions "Stripe Connect / Stripe Express" | CONFIRMED for Stripe docs. Applicability to Vast is INFERENCE |
| Wise | Wise can pay out in **COP to Colombia**. **Ecuador and Venezuela are not listed** as destinations; USD via SWIFT "might" work for Ecuador | CONFIRMED, Wise help page. Account-holding rules for residents unverified |
| PayPal | Operates in CO, EC and VE. I could not verify Venezuelan account limits (withdrawals to local banks) because the paypal.com pages returned 403 | GAP |

### 2.8 Host requirements

**Minimum requirements for verification** (CONFIRMED, docs.vast.ai/host/verification-stages):

| Area | Minimum |
|---|---|
| GPU | NVIDIA, Maxwell or newer. **More than 7 GB VRAM per GPU.** CUDA 11.8 or newer. All GPUs in a machine identical. PCIe above 2.85 GiB/s per GPU. On ARM64, CUDA 12.6 or newer is required, so Maxwell and Pascal cannot be verified on ARM |
| CPU | x86_64 or ARM64 with AVX. **At least 2 physical cores per GPU** |
| RAM | **System RAM at least 0.95 × total VRAM.** For example, 8× RTX 3090 (192 GB VRAM) needs about 183 GB RAM |
| Network | **At least 500 Mbps download and 500 Mbps upload**, wired (fiber recommended). **Public IPv4; machines behind CGNAT or a shared ISP IP "cannot be used for hosting".** At least 5 forwarded ports per GPU, 100 recommended |
| OS | **Ubuntu Server** 22.04 LTS (24.04 recommended), latest kernel patch level, supported NVIDIA driver. SSH keys only (password login off), a unique key per machine, Secure Boot disabled. Desktop editions are not supported |
| Storage | SSD. A **200 GB drive dedicated to Docker**, plus 20 GB free on root |
| Reliability | **Above 90%.** A new machine "typically reaches 90% within a few days" |
| Use | **Dedicated machines only.** Mining, gaming or personal jobs automatically fail verification |

**How verification works:** it is automated and "proprietary". It weighs reliability (sustained uptime of 99.99% or more "favored"), infrastructure, DLPerf, and **supply and demand**.
- Top-tier GPUs (B300/B200/H200/H100, RTX PRO 6000, 8× 5090 and 8× 4090 builds) are prioritized.
- Within a GPU type, more GPUs per machine helps. Enabling VMs "significantly improves verification likelihood".
- Reducing hardware after the machine is created triggers deverification (CONFIRMED, docs.vast.ai/host/understanding-verification).
- **Implication:** old, unpopular cards in small boxes are the configurations least likely to be verified (INFERENCE).

**Datacenter / "Secure Cloud" tier** (CONFIRMED, docs.vast.ai/host/datacenter-status):
- **Requirements:**
  - An **active ISO/IEC 27001** certificate.
  - Equipment owned by a registered business with verifiable owners.
  - A signed Datacenter Hosting Agreement.
  - Identity verification of the owner.
  - **At least 5 GPU servers.**
  - Documents: IDs, a certificate of good standing, the datacenter's name, address and certificates, and a datacenter contract or invoice.
- **Benefits:** a blue label, inclusion in Secure Cloud searches, "increased reliability scoring", and higher ranking.
- The live data shows a **46% price premium** for datacenter machines (COMPUTED).

**Host obligations** (CONFIRMED, docs.vast.ai/host/hosting-overview):
- Rental contracts lock in price and end date. The host must keep the machine online until the latest rental end date and cannot reprice existing contracts.
- Hosts need a separate host account.
- "Vast does not offer support for getting your machine working." Help is through host-only Discord channels.
- The `min_gpu` setting controls slicing into 1, 2, 4 or 8 GPUs. Vast says search volume for 8× rentals is about 2× that for 1×.

**Market statistics:** cloud.vast.ai/host/market and the `/api/v0/metrics/gpu/*` endpoints, which include `usage` and `usage_30d` per GPU, **require a host API key**. I could not access them; the unauthenticated call returned "This action requires login" (CONFIRMED).

---

## 3. Gross revenue per GPU per month, host-side after Vast's 25% (COMPUTED)

Assumptions: 730 h per month, host-side price = renter median × 0.75, GPU compute only (storage and bandwidth would add a little). **These figures exclude electricity, internet, cooling, depreciation, payout and FX fees.**

| GPU | renter median $/h | host $/h | host $/mo @30% | @50% | @70% | observed util. (all / verified) | host $/mo at verified util. | **new unverified host case** (0.88× price, 47% util.) |
|---|---|---|---|---|---|---|---|---|
| RTX 3060 | 0.073 | 0.055 | $12 | $20 | $28 | 75% / 79% | $32 | $17 |
| RTX 3070 | 0.107 | 0.080 | $18 | $29 | $41 | 65% / 69% | $41 | $24 |
| RTX 3080 | 0.133 | 0.100 | $22 | $36 | $51 | 56% / 62% | $45 | $30 |
| **RTX 3090** | 0.213 | 0.160 | **$35** | **$58** | **$82** | 81% / 85% | $99 | **$48** |
| RTX 4070S | 0.097 | 0.073 | $16 | $27 | $37 | 65% / 75% | $40 | $22 |
| RTX 4080S | 0.241 | 0.180 | $40 | $66 | $92 | 73% / 75% | $99 | $54 |
| **RTX 4090** | 0.480 | 0.360 | **$79** | **$131** | **$184** | 78% / 84% | $220 | **$109** |
| RTX 5060 Ti | 0.133 | 0.100 | $22 | $36 | $51 | 68% / 74% | $54 | $30 |
| RTX 5070 Ti | 0.200 | 0.150 | $33 | $55 | $77 | 62% / 72% | $78 | $45 |
| RTX 5080 | 0.241 | 0.181 | $40 | $66 | $92 | 67% / 86% | $113 | $55 |
| RTX 5090 | 0.667 | 0.500 | $110 | $182 | $255 | 76% / 80% | $291 | $151 |
| RTX A4000 | 0.096 | 0.072 | $16 | $26 | $37 | 71% / 89% | $47 | $22 |
| RTX A5000 | 0.227 | 0.170 | $37 | $62 | $87 | 57% / 78% | $97 | $51 |
| RTX A6000 | 0.480 | 0.360 | $79 | $131 | $184 | 91% / 93% | $245 | $109 |
| RTX 6000 Ada | 0.665 | 0.499 | $109 | $182 | $255 | 89% / 91% | $332 | $151 |
| RTX PRO 6000 WS | 1.467 | 1.100 | $241 | $402 | $562 | 80% / 84% | $674 | $332 |
| A40 | 0.680 | 0.510 | $112 | $186 | $261 | 67% / 67% | $249 | $154 |
| L40S | 0.600 | 0.450 | $99 | $164 | $230 | 77% / 87% | $287 | $136 |
| A100 PCIe | 0.667 | 0.500 | $110 | $182 | $255 | 75% / 83% | $305 | $151 |
| A100 SXM4 | 1.067 | 0.800 | $175 | $292 | $409 | 83% / 92% | $537 | $242 |
| H100 SXM | 2.333 | 1.750 | $383 | $639 | $894 | 81% / 94% | $1,199 | $528 |
| H200 | 5.188 | 3.891 | $852 | $1,420 | $1,988 | 77% / 79% | $2,255 | $1,175 |
| B200 | 10.000 | 7.500 | $1,642 | $2,738 | $3,832 | 76% / 78% | $4,247 | $2,264 |
| **Tesla V100** | 0.080 | 0.060 | **$13** | **$22** | **$31** | 79% / 86% | $38 | **$18** |
| Tesla P40 | 0.200 | 0.150 | $33 | $55 | $77 | n=10 | – | $45 |
| Tesla T4 | 0.141 | 0.105 | $23 | $39 | $54 | 42% / 79% | $61 | $32 |
| RTX 2080 Ti | 0.080 | 0.060 | $13 | $22 | $31 | 47% / 55% | $24 | $18 |
| GTX 1080 Ti | 0.067 | 0.050 | $11 | $18 | $26 | 63% / 62% | $23 | $15 |

**Electricity check (ESTIMATE, for context only; other agents cover power):**
- An RTX 3090 drawing about 350 W at full load for 730 h uses about 255 kWh. At $0.10–0.20/kWh that is about **$26–51 per month at 100% load**, or about $13–26 at 50% utilization, before idle draw.
- That consumes a large share of the RTX 3090's $58 gross revenue at 50% utilization.
- **Older cards (V100, 2080 Ti, 1080 Ti, P100) earn $13–31 per month gross, which is close to or below their power cost.** (INFERENCE)

---

## 4. Implications for the LATAM used-hardware rental business

1. **Margin is set globally, not locally.** Vast's renters pay global prices, and LatAm offers clear at about 0.96× the global median. Buying hardware cheaply in Colombia, Ecuador or Venezuela helps only on capex. Revenue per GPU is capped at the global host price: about $0.16/h for an RTX 3090 and about $0.36/h for an RTX 4090.
2. **Which cards make sense:**
   - **The RTX 3090 (24 GB) is the best "old consumer" card** on Vast. It has deep demand (2.3k GPUs, 81% utilization, prices up 39% in 90 days) and a fair price (renter $0.21/h).
   - **RTX 4090 and 5090** earn far more per card ($131–182 per month at 50%). They are not "old/cheap" hardware, though.
   - **Old datacenter and Pascal/Turing cards (V100, P100, P40, T4, 2080 Ti, 1080 Ti) are poor fits.** They earn $13–31 per month gross, prices are falling (V100 −57% and P100 −60% in 90 days), and utilization is often 25–50%.
   - Cards with 6 GB VRAM or less fail verification (the minimum is more than 7 GB).
3. **Expect a ramp-up.** New machines start unverified, and unverified or low-reliability machines run at about 45–50% utilization versus about 82% for verified ones. Verification is automated and favors popular GPUs, higher GPU counts per box, VMs and 99.99%+ uptime. The "new unverified host" column in §3 is a better base case for the first 1–3 months than the market average.
4. **Connectivity and CGNAT are likely the main LATAM bottleneck.**
   - Verification needs **500 Mbps upload and download plus a public IPv4 address. CGNAT is disqualifying.**
   - Machines with under 100 Mbps upload run at 59% utilization.
   - The existing LatAm hosts median 410–875 Mbps upload (Brazil is lowest at 410).
   - A business fiber link with a static IP in Bogotá, Medellín, Quito or Guayaquil needs to be costed, ideally in a colocation facility.
5. **Server builds need a lot of RAM.** Verification requires system RAM of at least 0.95× total VRAM and at least 2 physical CPU cores per GPU. Machines with under 16 GB RAM per GPU run at 58% utilization. An 8× RTX 3090 node needs about 192 GB of RAM, which erodes the "cheap old server" advantage.
6. **The datacenter tier pays well but is hard to reach.** Secure Cloud machines get a 46% price premium. Qualifying requires ISO/IEC 27001 colocation, a registered business, at least 5 servers and identity verification. Few LATAM colocation sites hold ISO 27001 (unverified), so this is a phase-2 option at best.
7. **Payout route:**
   - Venezuela is the hardest case: no Stripe, no Wise, PayPal only, and US-sanctions exposure if any state-linked party is involved.
   - Colombia: Wise in COP; Stripe likely not available.
   - Ecuador: Stripe Global Payouts in USD *may* work; Wise is unclear.
   - **INFERENCE:** running the host account through the entrepreneur's Spanish or EU entity, receiving through Stripe or Wise in EUR/USD, and paying LATAM operators locally is the most robust structure. It also satisfies the "B2B payments" requirement.
8. **The market itself is real and fairly liquid.** There are 26.5k listed GPUs, about 74% occupied in this snapshot, and consumer and Blackwell prices are rising. A new LatAm supplier would barely be noticed in aggregate (LatAm is about 1% of supply). Competition comes from global hosts, not local ones.

---

## 5. Confidence and gaps

| Item | Confidence | Why |
|---|---|---|
| Per-GPU renter prices (medians, p25/p75) | **High** | Full sweep of about 8.9k machines from Vast's own search API. Per-machine pricing is directly observed |
| 25% implicit take rate | **High–medium** | Strong numeric evidence (96% of prices become round under ×0.75), consistent with Vast's "no fee deducted… Vast sets its own pricing" wording. Not stated as a percentage anywhere; Vast could vary it dynamically |
| Utilization (~74%; verified 82% vs unverified 47%) | **Medium** | One Saturday-midday snapshot. It assumes `rentable=false` means an on-demand or reserved contract. Interruptible usage is invisible. Unlisted or offline machines are excluded. Validation showed about 6% per-machine churn or mismatch. Verified versus unverified is correlation, not causation |
| LatAm comparisons | **Low–medium** | Only 260 GPUs. CO/EC/VE have n = 1–2. Geolocation is self-reported or IP-based |
| Feed 90-day trend | **Medium** | Vast's own feed, but the basis of the daily median (host-side or rented price?) is undocumented |
| Payout availability per country | **Medium–low** | Stripe and Wise docs are confirmed, but which Stripe product Vast uses is unknown. PayPal Venezuela limits are unverified (paypal.com returned 403) |
| Host requirements and datacenter criteria | **High** | Vast docs fetched 2026-11-14 |

**Gaps and next steps:**
- Vast's official per-GPU `usage` and `usage_30d` figures exist only behind a host API key (/api/v0/metrics/gpu/current). A host account with one registered machine would unlock 30-day utilization, which would be much better than one snapshot.
- Re-run the free-GPU sweep on a weekday and at several times of day. The scripts are in the scratch folder.
- Confirm with Vast support which countries Stripe, Wise and PayPal payouts cover for CO, EC and VE, and whether Vast's 25% markup is fixed.
- Check CGNAT and symmetric-fiber availability with the main ISPs in Colombia and Ecuador, and ISO 27001 colocation availability.
- WebSearch was unavailable (budget exhausted). I could not look for secondary sources such as host forums, Reddit or third-party trackers to triangulate utilization.

---

## 6. Sources (all accessed 2026-11-14)

- Vast public offers API (search-offers backend), unauthenticated POST: https://console.vast.ai/api/v0/bundles/ (pulled 12:19–12:53 UTC; also https://cloud.vast.ai/api/v0/bundles/)
- vast-cli source showing query format and defaults (`search offers`, default order `score-`): https://github.com/vast-ai/vast-cli (raw: https://raw.githubusercontent.com/vast-ai/vast-cli/master/vast.py)
- Vast public GPU pricing feed (updated 2026-11-14T11:30:22Z): https://storage.googleapis.com/vast-public-gpu-pricing/gpu-pricing-public.json, linked from https://vast.ai/pricing.md
- Vast hosting page FAQ ("no fee or commission deducted…"): https://vast.ai/hosting
- Vast Host Earnings Calculator FAQ ("Vast does not publish per-GPU utilization figures"): https://vast.ai/hosting/calculator
- Host Payouts: https://docs.vast.ai/host/payment.md
- Hosting Overview (contracts, min_gpu, reliability FAQ, CGNAT, search ranking): https://docs.vast.ai/host/hosting-overview.md
- Verification Stages (minimum requirements table): https://docs.vast.ai/host/verification-stages.md
- Understanding Verification: https://docs.vast.ai/host/understanding-verification.md
- Self-Test: https://docs.vast.ai/host/how-to-self-test.md
- Datacenter Status (Secure Cloud requirements): https://docs.vast.ai/host/datacenter-status.md
- Optimize Your Earnings (pricing, min bid, disk and bandwidth pricing, min_gpu): https://docs.vast.ai/host/optimization-guide.md
- GPU Market Metrics (host-only API, usage fields): https://docs.vast.ai/host/market-metrics.md and https://docs.vast.ai/api-reference/machines/show-gpu-metrics.md
- Tax Guide for Hosts: https://docs.vast.ai/host/guide-to-taxes.md
- VMs (premium, no bandwidth revenue on VMs): https://docs.vast.ai/host/vms.md
- Rental types FAQ, DLPerf: https://docs.vast.ai/guides/reference/faq/rental-types.md
- Instance pricing (storage billed while stopped, bandwidth per byte): https://docs.vast.ai/guides/instances/pricing.md
- Vast Terms of Service (export and sanctions clause): https://vast.ai/terms
- Stripe Connect cross-border payouts: https://docs.stripe.com/connect/cross-border-payouts
- Stripe Global Payouts recipient countries: https://docs.stripe.com/global-payouts/recipient-requirements
- Wise send-to countries: https://wise.com/help/articles/2571942/what-countriesregions-can-i-send-to

**Scratch artifacts:**
- Summary JSON: `/tmp/claude-0/-home-user-cowork-ulricht-project/6a906045-5aa8-5271-a0fd-a23952c77e55/scratchpad/agent01/vast_pull_summary_2026-11-14.json`
- Scripts: `/tmp/claude-0/-home-user-cowork-ulricht-project/6a906045-5aa8-5271-a0fd-a23952c77e55/scratchpad/agent01/scripts/` (`sweep.py`, `sweep_free.py`, `analyze.py`, `tables.py`)
