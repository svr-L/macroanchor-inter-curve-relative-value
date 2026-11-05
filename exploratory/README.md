# Exploratory follow-ups — NOT V2.3 evidence

The two notebooks here are separate **post-V2.3** research designs. They do **not** modify the frozen V2.3 signal, source notebook, or aggregate tables. They are deliberately stored under `exploratory/`, not merged into the headline performance.

- **V3.2** — historical 5Y sovereign CDS bucket / nearest-CDS diagnostics. Starts with one Colab upload selecting the frozen `g10_panel_model_objects.csv` and **multiple original Investing.com CDS CSVs** together; accepts filenames renamed by Colab (`(4)` suffix). Rating and OAS input optional; bucket tests do **not** establish true sovereign CS01 neutrality. Originally executed as V3.1, which produced 190 return-bearing months of CDS-bucket positions, mean 12m gross proxy return 0.493% and NW(12) t=1.22, but failed to produce a meaningful six-leg common-sample benchmark (only nine formation months). This is **descriptive and inconclusive**.
- **V4.1** — idealized CDS-implied **Q** hazard and recovery-of-par defaultable zero-coupon pricing inversion (not `TP − CDS`); 5Y-to-10Y constant hazard extrapolation, same forward-return construction. On the historic CDS overlap, the strict six-leg comparison formed only **nine months**, all April–December 2023; no reliable t-statistic or outperformance inference is possible. This is **not a validated rates-only term premium**, CDS hedge, or identified P-world default intensity.

**Data constraints:** Canada is observed only 2012–2023 in the supplied CDS history. Swiss CDS begin in 2023. Japanese CDS are present but the usable MacroAnchor panel ends earlier; source-specific gaps limit simultaneous six-leg breadth. No backfill after the last observed quote is permitted.

**Research design rules:** changes in CDS threshold, universe, recovery and 5Y–10Y extrapolation are *new experiments*; don't use historical V2.3 performance to claim they were pre-registered. Raw CDS CSVs and nonpublic MacroAnchor country panel are not redistributed.

Run the Colab notebooks using **Run all**; their first code cell requests all files together. Their outputs are stripped in the repository to avoid confusing fresh runs with previous outcomes. This public package has not been re-executed on the private full panel.
