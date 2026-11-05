# Research log — hard separation of frozen evidence from exploration

## Frozen as of V2.3

- Parent predictor: MacroAnchor 10Y `tp_z_past`; no new signal definition.
- Primary: top-3/bottom-3 each month, gross notional normalized 1, explicitly net DV01 = 0.
- Top-2/bottom-2: sensitivity only. Continuous: second pre-specified rule.
- Monthly formation, 12-month forward horizon, NW(12) inference and non-overlap calendar diagnostics.
- Global duration + identical-constructor yield-level and slope/carry spanning.
- Results preserved in `results/` (from actually executed notebook) and `evidence/`.

## Not yet done / not represented as results

- Top-1/bottom-1; credit-neutral or rating-matched trade; CDS-cleaned yields.
- Geographic additions beyond original panel; conditional tenor breadth.
- Real historical base-currency FX hedges, futures/IRS implementation, swap spread attribution.
- State-dependent credit transition model or multi-factor MacroAnchor.
- Same-sample reduced-model spanning comparison, full real-time macro data vintage.

## Distinct projects

- Cross-country G10 10Y strategy and US cross-tenor Curve RV are two **economic strategies**, not parallel branches of a single result.
- Cross-tenor experiments had extensive strategy searches before V6. Even a frozen V6 trial should not be described as independent confirmatory validation. Keep it in a separate private archive or clearly marked exploratory public research, with its nulls/limitations intact.
- The sparse curve allocation project is directional asset allocation and stays independent too.

## Later exploratory notebooks (clearly segregated)

See [`exploratory/README.md`](../exploratory/README.md). These are *not* part of the frozen results or evidence, and 2023-only six-leg CDS-Q comparison provides insufficient breadth to confirm improvement.
