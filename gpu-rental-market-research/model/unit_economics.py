#!/usr/bin/env python3
"""
Unit-economics model: used hardware bought in LATAM, rented on P2P GPU marketplaces.

Run:  python3 unit_economics.py            -> prints markdown tables
      python3 unit_economics.py --csv      -> also writes results.csv next to this file

All money in USD. Every input is an assumption sourced from the agent reports in
../agent-reports/ (see the ASSUMPTIONS comments). Change the numbers here, re-run.
"""
from __future__ import annotations

import csv
import sys
from dataclasses import dataclass, field
from pathlib import Path

HOURS_PER_MONTH = 730


@dataclass
class Rig:
    name: str
    gpus: int                 # number of GPUs in the box (0 = CPU-only)
    capex: float              # landed purchase cost of the whole box, USD (hardware + import + setup)
    watts_load: float         # wall power when rented (whole box)
    watts_idle: float         # wall power when idle
    price_per_gpu_hr: float   # customer-facing $/GPU-hr you can realistically list at (box price / gpus if CPU-only)
    utilization: float        # fraction of hours rented (0-1)
    platform_fee: float = 0.25          # marketplace take rate
    annual_price_decline: float = 0.20  # yearly drop of achievable rental price
    useful_life_months: int = 36
    resale_pct_end: float = 0.15        # resale value at end of life as % of capex
    extra_monthly: float = 0.0          # per-box share of internet, colo, maintenance, etc.
    note: str = ""


@dataclass
class Site:
    name: str
    usd_per_kwh: float
    pue: float                # cooling/overhead multiplier on IT power
    downtime: float           # fraction of hours lost to blackouts/outages (0-1)
    fixed_monthly: float      # site-level fixed costs (fiber, static IP, rent, part-time tech), USD
    note: str = ""


def month_cashflows(rig: Rig, site: Site, boxes_at_site: int = 1) -> list[float]:
    """Monthly net cash flow for one box over its useful life (excludes capex)."""
    flows = []
    monthly_decline = (1 - rig.annual_price_decline) ** (1 / 12)
    for m in range(rig.useful_life_months):
        price = rig.price_per_gpu_hr * (monthly_decline ** m)
        avail = 1 - site.downtime
        rented_h = HOURS_PER_MONTH * avail * rig.utilization
        idle_h = HOURS_PER_MONTH * avail * (1 - rig.utilization)
        gpus = max(rig.gpus, 1)
        revenue = rented_h * price * gpus * (1 - rig.platform_fee)
        kwh = (rented_h * rig.watts_load + idle_h * rig.watts_idle) / 1000 * site.pue
        power_cost = kwh * site.usd_per_kwh
        fixed = site.fixed_monthly / boxes_at_site + rig.extra_monthly
        flows.append(revenue - power_cost - fixed)
    return flows


def evaluate(rig: Rig, site: Site, boxes_at_site: int = 1) -> dict:
    flows = month_cashflows(rig, site, boxes_at_site)
    cum, payback = -rig.capex, None
    for i, f in enumerate(flows, start=1):
        cum += f
        if payback is None and cum >= 0:
            payback = i
    total = sum(flows) + rig.capex * rig.resale_pct_end
    roi = (total - rig.capex) / rig.capex if rig.capex else float("nan")
    return {
        "rig": rig.name,
        "site": site.name,
        "month1_net": flows[0],
        "avg_monthly_net": sum(flows) / len(flows),
        "payback_months": payback,
        "life_profit": total - rig.capex,
        "life_roi": roi,
    }


# ---------------------------------------------------------------------------
# ASSUMPTIONS — placeholders, replaced with researched values in the synthesis
# ---------------------------------------------------------------------------
SITES: list[Site] = []
RIGS: list[Rig] = []
BOXES_PER_SITE = 4


def fmt_money(x):
    return f"${x:,.0f}"


def main():
    rows = []
    for rig in RIGS:
        for site in SITES:
            rows.append(evaluate(rig, site, BOXES_PER_SITE))
    print("| Rig | Site | Month-1 net | Avg monthly net | Payback (months) | 3-yr profit | 3-yr ROI |")
    print("|---|---|---:|---:|---:|---:|---:|")
    for r in rows:
        pb = r["payback_months"] if r["payback_months"] is not None else "never"
        print(f"| {r['rig']} | {r['site']} | {fmt_money(r['month1_net'])} | {fmt_money(r['avg_monthly_net'])} "
              f"| {pb} | {fmt_money(r['life_profit'])} | {r['life_roi']*100:.0f}% |")
    if "--csv" in sys.argv:
        out = Path(__file__).with_name("results.csv")
        with out.open("w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)
        print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
