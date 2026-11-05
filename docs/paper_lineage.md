# Research lineage — MacroAnchor paper → inter-curve RV

This repo **evolves directly from** the parent working paper **“The Macro Anchor as a Short-Rate Central Tendency: Bond Risk Premia, Out-of-Sample Discipline, and a Specification Audit.”**

- **Parent research repository:** [MacroAnchor Bond Risk Premia](https://github.com/svr-L/macroanchor-bond-risk-premia)
- **Parent working paper (in parent repository):** [PDF](https://github.com/svr-L/macroanchor-bond-risk-premia/blob/main/paper/macroanchor_working_paper.pdf)
- **Separate within-curve research:** [MacroAnchor Curve Relative Value](https://github.com/svr-L/macroanchor-curve-relative-value)

> Note: the parent URL is inferred from the author-provided `macroanchor-bond-risk-premia-main.zip` archive name. Its current remote accessibility could not be independently checked. Verify the link when publishing.

## Inherited, frozen predictor

The parent paper models the moving macro anchor `theta_t = r*_t + trend_inflation_t` as the **physical-measure central tendency of the short rate**, rather than as a fair value for the long bond yield. The model derives a pure-expectations yield, and defines a model-implied residual/term-premium signal as `TP = observed government yield − model-implied pure-expectations yield`. A historically standardized, past-only country-level 10Y score `tp_z_past` is imported into the frozen V2.3 portfolio.

## What this repository adds (NOT a new parent-model fit)

1. A **cross-country / inter-curve** sovereign 10Y ranking across the usable developed-market panel.
2. Explicit **net-zero signed DV01** long/short construction (3 high-score countries versus 3 low-score countries, gross notional normalized to 1).
3. Proxy 12-month excess-return accounting, turnover/cost stresses and separate spanning vs global 10Y duration, yield-level and slope/carry controls.
4. An evidence audit that preserves results, sample lengths, manifest hashes and caveats, plus post-freeze exploratory CDS credit and Q-pricing diagnostics **kept outside the frozen headline**.

This does **not** demonstrate a new identification of the term premium from credit-free security prices; currency, sovereign-credit, funding and liquidity exposures remain. All P/Q-model modifications discussed later belong to a distinct research agenda, not a redefinition of the V2.3 predictor.
