#!/usr/bin/env python3
"""
Unit-economics model: used hardware bought for a small LATAM GPU cluster, rented on
P2P / decentralized compute marketplaces.

Run:   python3 unit_economics.py          -> prints all markdown tables
       python3 unit_economics.py --csv    -> also writes results.csv next to this file

All money is USD. Every input below is an assumption taken from the agent reports in
../agent-reports/ (report number in brackets, e.g. [06]). Change any number and re-run.
Prices are a snapshot of 2026-11-14.

Model logic (per 4-GPU box, monthly, over a 36-month horizon):
  revenue   = GPU-hours rented x listed $/GPU-hr x (1 - platform fee) x price-path multiplier
  power     = (rented-hours x load W + idle-hours x idle W) x PUE x blended $/kWh
  fixed     = site fixed costs / boxes per site
  capex     = box landed cost + share of site build-out (UPS, generator, electrical)
  residual  = resale value at month 36 (% of box capex)
Utilization ramps up during the first months (marketplace verification takes 2-4+ weeks [09]).
"""
from __future__ import annotations

import csv
import sys
from dataclasses import dataclass, replace
from pathlib import Path

HOURS_PER_MONTH = 730
HORIZON_MONTHS = 36
BOXES_PER_SITE = 4          # 4 boxes x 4 GPUs = 16-GPU site (the size costed in [08])

# Rental-price level at the END of year 1, 2, 3 relative to today (cumulative) [06].
# The model interpolates linearly month by month from 1.0 today.
PRICE_PATHS = {
    "bull": [1.00, 0.95, 0.855],      # 0%, -5%, -10%  per year
    "base": [0.90, 0.72, 0.576],      # -10%, -20%, -20%
    "bear": [0.70, 0.49, 0.343],      # -30%, -30%, -30%
}


def price_multiplier(path: list[float], month: int) -> float:
    """Linear interpolation between yearly anchor points (month 0 = 1.0)."""
    anchors = [1.0] + list(path)
    yr, frac = divmod(month, 12)
    if yr >= len(path):
        return anchors[-1]
    return anchors[yr] + (anchors[yr + 1] - anchors[yr]) * frac / 12


@dataclass
class Rig:
    name: str
    gpus: int                   # GPUs per box (0 = CPU-only, priced per box-hour)
    gpu_unit_price: float       # used price per GPU, US market Nov 2026 [07]
    host_cost: float            # chassis/board/CPU/RAM/PSU/disk for the box, US used price [05][07]
    landed_mult: float          # import / landed multiplier into the country [07]
    watts_load: float           # whole-box wall power when rented [05][08]
    watts_idle: float
    list_price: float           # $/GPU-hr (or $/box-hr if gpus=0) a LATAM host can list at [01][06][09]
    utilization: float          # steady-state share of hours rented [06][09]
    platform_fee: float         # marketplace take [01][02][09]
    resale_pct_36m: float       # resale value at month 36, % of box capex
    life_months: int = 36       # months the hardware stays rentable [10]
    note: str = ""

    @property
    def box_capex(self) -> float:
        return (self.gpus * self.gpu_unit_price + self.host_cost) * self.landed_mult


@dataclass
class Site:
    name: str
    grid_kwh: float             # commercial tariff, USD/kWh [08]
    gen_share: float            # share of hours on diesel generator (blackouts) [08][10]
    gen_kwh: float              # diesel fuel cost per kWh generated [08]
    pue: float                  # cooling/overhead multiplier [08]
    fixed_monthly: float        # site: business fiber + public IP, space, part-time tech, misc [08]
    site_capex: float           # UPS + generator + electrical for a 16-GPU site [08]
    note: str = ""

    @property
    def blended_kwh(self) -> float:
        return (1 - self.gen_share) * self.grid_kwh + self.gen_share * self.gen_kwh


RAMP = [0.5, 0.75]  # months 1-2: unverified new hosts run ~45-50% vs ~82% verified [01][09]


def cashflows(rig: Rig, site: Site, path: list[float]) -> list[float]:
    flows = []
    for m in range(HORIZON_MONTHS):
        if m >= rig.life_months:
            flows.append(0.0)
            continue
        price = rig.list_price * price_multiplier(path, m)
        util = rig.utilization * (RAMP[m] if m < len(RAMP) else 1.0)
        units = max(rig.gpus, 1)
        rented_h = HOURS_PER_MONTH * util
        idle_h = HOURS_PER_MONTH - rented_h
        revenue = rented_h * units * price * (1 - rig.platform_fee)
        kwh = (rented_h * rig.watts_load + idle_h * rig.watts_idle) / 1000 * site.pue
        flows.append(revenue - kwh * site.blended_kwh - site.fixed_monthly / BOXES_PER_SITE)
    return flows


def evaluate(rig: Rig, site: Site, scenario: str = "base") -> dict:
    flows = cashflows(rig, site, PRICE_PATHS[scenario])
    capex = rig.box_capex + site.site_capex / BOXES_PER_SITE
    cum, payback = -capex, None
    for i, f in enumerate(flows, start=1):
        cum += f
        if payback is None and cum >= 0:
            payback = i
    residual = rig.box_capex * rig.resale_pct_36m
    profit = sum(flows) + residual - capex
    steady = flows[min(3, len(flows) - 1)]
    return {
        "rig": rig.name, "site": site.name, "scenario": scenario,
        "capex": capex, "month4_net": steady, "payback_months": payback,
        "profit_36m": profit, "roi_36m": profit / capex,
    }


def max_bid_per_gpu(rig: Rig, site: Site, target_months: int, scenario: str = "base") -> float:
    """Highest US-equivalent price per GPU you can pay and still pay back within target_months."""
    flows = cashflows(rig, site, PRICE_PATHS[scenario])
    earned = sum(flows[:target_months])
    budget = earned - site.site_capex / BOXES_PER_SITE      # what the box itself may cost, landed
    per_gpu = (budget / rig.landed_mult - rig.host_cost) / max(rig.gpus, 1)
    return per_gpu


# ---------------------------------------------------------------------------
# SITES  [08] operating costs, [10] risk
# ---------------------------------------------------------------------------
SITES = [
    Site("Quito/Cuenca (EC)", grid_kwh=0.09, gen_share=0.05, gen_kwh=0.24, pue=1.15,
         fixed_monthly=900, site_capex=14000,
         note="commercial LV meter $0.086-0.094; altitude free cooling; 2024-style blackouts -> generator"),
    Site("Guayaquil (EC)", grid_kwh=0.09, gen_share=0.05, gen_kwh=0.24, pue=1.6,
         fixed_monthly=900, site_capex=18000,
         note="same tariff, hot coastal climate needs A/C"),
    Site("Bogota (CO)", grid_kwh=0.34, gen_share=0.01, gen_kwh=0.27, pue=1.15,
         fixed_monthly=1000, site_capex=9000,
         note="commercial ~$0.314 incl. 20% contribution, + El Nino excess penalty -> blended 0.34"),
    Site("Barranquilla (CO)", grid_kwh=0.36, gen_share=0.01, gen_kwh=0.27, pue=1.6,
         fixed_monthly=1000, site_capex=12000,
         note="hot coast, highest power cost per GPU in [08]"),
    Site("Caracas (VE)", grid_kwh=0.05, gen_share=0.25, gen_kwh=0.09, pue=1.4,
         fixed_monthly=650, site_capex=16000,
         note="cheap power on paper; 82% households daily outages; mining-ban seizure risk NOT priced"),
]

# ---------------------------------------------------------------------------
# RIGS  (4-GPU boxes unless noted)
# list_price = live Vast.ai renter-price median (2026-11-14) x 0.95 LATAM factor [01][06][09]
# Vast host receives ~75% of the renter price (inferred from API, [01]) -> platform_fee=0.25
# ---------------------------------------------------------------------------
RIGS = [
    Rig("Old CPU server (R730, 256 GB, no GPU) on Akash", gpus=0, gpu_unit_price=0,
        host_cost=1450, landed_mult=1.0, watts_load=420, watts_idle=150,
        list_price=294 / HOURS_PER_MONTH, utilization=0.05, platform_fee=0.0,
        resale_pct_36m=0.35,
        note="Akash default bids = $294/mo if 100% leased; unaudited CPU providers ~1.5% utilized [05]"),
    Rig("4x V100 16GB (old 4U GPU server)", gpus=4, gpu_unit_price=400, host_cost=1200,
        landed_mult=1.25, watts_load=1350, watts_idle=380, list_price=0.08 * 0.95,
        utilization=0.45, platform_fee=0.25, resale_pct_36m=0.05, life_months=18,
        note="Volta dropped by CUDA 13 / PyTorch 2.15 [10]"),
    Rig("4x RTX 3090", gpus=4, gpu_unit_price=1550, host_cost=1700, landed_mult=1.20,
        watts_load=1600, watts_idle=280, list_price=0.213 * 0.95, utilization=0.65,
        platform_fee=0.25, resale_pct_36m=0.30,
        note="host needs >=96 GB RAM (95% of VRAM rule) + x16 slots [10]"),
    Rig("4x RTX 4090", gpus=4, gpu_unit_price=3300, host_cost=2000, landed_mult=1.20,
        watts_load=2000, watts_idle=300, list_price=0.48 * 0.95, utilization=0.65,
        platform_fee=0.25, resale_pct_36m=0.35),
    Rig("4x RTX 5090", gpus=4, gpu_unit_price=5500, host_cost=2400, landed_mult=1.20,
        watts_load=2500, watts_idle=340, list_price=0.667 * 0.95, utilization=0.65,
        platform_fee=0.25, resale_pct_36m=0.40),
    Rig("4x A100 80GB PCIe on Vast", gpus=4, gpu_unit_price=11000, host_cost=2400,
        landed_mult=1.20, watts_load=1550, watts_idle=360, list_price=0.85 * 0.95,
        utilization=0.65, platform_fee=0.25, resale_pct_36m=0.30),
    Rig("4x A100 80GB PCIe on Akash/Lium", gpus=4, gpu_unit_price=11000, host_cost=2400,
        landed_mult=1.20, watts_load=1550, watts_idle=360, list_price=1.27,
        utilization=0.60, platform_fee=0.0, resale_pct_36m=0.30,
        note="Akash median $1.49 (no fee) / Lium ~$927/mo incl. emissions, cut 15-25% [04]"),
    Rig("4x H100 PCIe 80GB (Vast/Akash/Lium blend)", gpus=4, gpu_unit_price=25000, host_cost=3000,
        landed_mult=1.20, watts_load=1750, watts_idle=400, list_price=2.10,
        utilization=0.70, platform_fee=0.15, resale_pct_36m=0.25,
        note="used H100 PCIe ~$18-35k late 2026 (web search, ESTIMATE); Vast H100 SXM $2.30, Akash $2.56 [04][06]"),
]


def money(x: float) -> str:
    return f"-${-x:,.0f}" if x < 0 else f"${x:,.0f}"


def table(rows: list[dict], title: str) -> None:
    print(f"\n### {title}\n")
    print("| Rig | Site | Capex (box + site share) | Net/month (steady, yr 1) | Payback | 36-mo profit | 36-mo ROI |")
    print("|---|---|---:|---:|---:|---:|---:|")
    for r in rows:
        pb = f"{r['payback_months']} mo" if r["payback_months"] else "never (36 mo)"
        print(f"| {r['rig']} | {r['site']} | {money(r['capex'])} | {money(r['month4_net'])} | {pb} "
              f"| {money(r['profit_36m'])} | {r['roi_36m']*100:.0f}% |")


def main() -> None:
    all_rows = []
    base = [evaluate(r, s, "base") for r in RIGS for s in SITES]
    all_rows += base
    table(base, "Base case (prices -10% / -20% / -20% per year), all rigs x all sites")

    best_site = SITES[0]
    scen_rows = [evaluate(r, best_site, sc) for r in RIGS for sc in ("bull", "base", "bear")]
    all_rows += [x for x in scen_rows if x["scenario"] != "base"]
    print(f"\n### Price scenarios at the best site ({best_site.name})\n")
    print("| Rig | Bull payback | Base payback | Bear payback | Bull 36-mo profit | Base 36-mo profit | Bear 36-mo profit |")
    print("|---|---:|---:|---:|---:|---:|---:|")
    for r in RIGS:
        res = {sc: evaluate(r, best_site, sc) for sc in ("bull", "base", "bear")}
        pb = lambda x: f"{x['payback_months']} mo" if x["payback_months"] else "never"
        print(f"| {r.name} | {pb(res['bull'])} | {pb(res['base'])} | {pb(res['bear'])} | "
              f"{money(res['bull']['profit_36m'])} | {money(res['base']['profit_36m'])} | {money(res['bear']['profit_36m'])} |")

    # Sensitivity: what if the operator already has space + does the tech work (fixed costs -> $250/site)
    lean = replace(best_site, name=best_site.name + " — lean (own space, own labour)", fixed_monthly=250, site_capex=8000)

    print(f"\n### Maximum price per GPU you can pay (US-equivalent, before import) for a 24-month payback — base case\n")
    print(f"| Rig | Today's US used price | Max bid: {best_site.name}, staffed site | Max bid: lean site | Lean max bid as % of market |")
    print("|---|---:|---:|---:|---:|")
    for r in RIGS:
        if r.gpus == 0:
            continue
        b_std, b_lean = max_bid_per_gpu(r, best_site, 24), max_bid_per_gpu(r, lean, 24)
        show = lambda b: money(b) if b > 0 else "none (loses money even if free)"
        print(f"| {r.name} | {money(r.gpu_unit_price)} | {show(b_std)} | {show(b_lean)} | {max(b_lean, 0) / r.gpu_unit_price * 100:.0f}% |")
    lean_rows = [evaluate(r, lean, "base") for r in RIGS]
    all_rows += lean_rows
    table(lean_rows, "Sensitivity: lean operation in Quito (own premises & labour, UPS-only backup)")

    # Sensitivity: hardware bought at 60% of US used price (distressed lots / auctions)
    cheap_rows = []
    for r in RIGS:
        if r.gpus == 0:
            continue
        cheap = replace(r, name=r.name + " @60% of market", gpu_unit_price=r.gpu_unit_price * 0.6,
                        host_cost=r.host_cost * 0.6, landed_mult=1.0)
        cheap_rows.append(evaluate(cheap, lean, "base"))
    all_rows += cheap_rows
    table(cheap_rows, "Sensitivity: lean Quito + hardware sourced locally at 60% of US used price (no import)")

    if "--csv" in sys.argv:
        out = Path(__file__).with_name("results.csv")
        with out.open("w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(all_rows[0].keys()))
            w.writeheader()
            w.writerows(all_rows)
        print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
