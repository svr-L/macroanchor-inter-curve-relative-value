# Figure provenance and interpretation

All plots in `figures/` are generated **from the saved V2.3 aggregate tables** in `results/`; none are simulated, backfilled or digitized from screenshots.

Regenerate: `python scripts/plot_results.py` (requires pandas, matplotlib and numpy).

| Figure | Exact source | What it does *not* show |
|---|---|---|
| `performance.png` | `results/performance.csv` | An investable annual return, Sharpe or equity curve; figures are means of **overlapping forward 12-month** gross proxy returns. |
| `subperiods.png` | `results/subperiods.csv` | Statistically independent regime alpha; samples and conditions differ. |
| `cost_sensitivity.png` | `results/cost_fx_stress_zero_drag.csv` | Executable market transaction costs, actual FX forward spreads or basis; the grid is model-based. |
| `country_exposure.png` | `results/country_exposure.csv` | Countries' realized P&L contributions; values are average **absolute target notional weights**. |
| `factor_spanning.png` | `results/spanning.csv` | A fair nested factor test on a common sample: n=363 for global-only, n=243 for fuller controls. |

V2.3 source evidence: `evidence/v2_3_executed_snapshot.ipynb` and `results/manifest.json`, including frozen input-panel SHA-256. The detailed 363-month return vector is not included because the original underlying country panel is not redistributed. It would be incorrect to reconstruct a wealth curve from the overlapping forward 12-month means.
