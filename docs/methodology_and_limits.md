# Methodology and interpretation — V2.3 frozen

## Economic target

The parent MacroAnchor system constructs a country-level expected term-premium proxy from a **macro anchor as a central tendency for the short rate**, rather than treating the macro anchor as a directly fair long yield. The source notebook computes a past-only standardized `tp_z_past` for country selection. The domestic 10Y formation return is represented by a **12-month duration-approximated excess-return proxy**, schematically:

`rx_{i,t,t+12} ~= y10_{i,t} - D10_{i,t} * (y10_{i,t+12}-y10_{i,t}) - r3m_{i,t}`

This construction does not use historical fixed-income securities, futures/IRS marks, explicit roll-down from the entire curve or historical FX hedging.

## Portfolio construction

1. Each formation month, retain countries with observed input, signal, duration proxy and forward-return data.
2. **Headline:** sort `tp_z_past`, select 3 lowest and 3 highest; set equal *DV01* targets, signs opposite. Convert desired DV01 positions to notionals by division by individual durations. Rescale to gross notional 1. DV01 sums to zero by construction, but cash notional and higher-order curve factors are not hedged.
3. **Top 2 / bottom 2** is a sensitivity (not a newly selected headline); **continuous-score** is a second pre-specified implementation.
4. Ranks and weights use information dated at formation time; performance uses 12-month *forward* outcome.

## Inference and attribution

- NW(12) t-statistics account approximately for 12-month overlapping observations. Twelve calendar-month tracks are examined separately to avoid counting every overlapping formation as an independent year. Their signs/Sharpe are descriptive, not 12 independent strategy replications.
- The first spanning benchmark is an equal-notional cross-country average of local sovereign 10Y excess-return proxies (global duration factor).
- In the full spanning, the two additional covariates are **DV01-neutral top3/bottom3** trades with identical construction but ranking on past-only standardized **10Y yield-level** or **10Y slope**. They are yield/carry controls, not a comprehensive bond-factor model.
- The full spanning shrinks from n=363 to **n=243**. A truly clean incremental-comparison would additionally rerun the reduced model on that same common sample (a *proposed* future audit, not a frozen result).
- Alpha intercepts are on 12-month returns; `alpha_ann` is a variable label and does not come from multiplying monthly returns by 12.

## Risks & boundaries

1. **Not a 10Y zero-beta bond portfolio in every risk sense:** net DV01 is neutral under a simplified duration proxy, but nonlinear/global curve, country funding, spread, safe-haven, sovereign-credit, cross-currency and liquidity exposures can remain.
2. **Credit:** short-horizon low realized default probability does *not* rule out mark-to-market credit spread volatility. No CDS decomposition, rating-neutral optimization or bond-level credit separation was implemented in V2.3.
3. **FX:** local excess returns over local funding are not an observed historical base-currency FX-hedged P&L. The FX-drag grid is illustrative, not empirically priced forward/cross-currency basis.
4. **Cost proxy:** annual turnover from changes in target notionals and fixed bp cost assumptions; actual executable bid-ask, carry, financing, capital usage and margin requirements remain unknown.
5. **Signal data:** archival FRED/OECD time series may include revisions; the original macro-anchor initialization has backfill conventions for early periods. This is not an ALFRED full-vintage exercise.
6. **Research selection:** pre-specification of this *portfolio* does not erase the fact that the *parent signal* was discovered/researched on overlapping historical capital-markets data. Report evidence as a strong research candidate, not independent external validation.

## Prioritization (proposals only)

- **Priority 1:** credit attribution and stability audit; compare common-sample spanning, not a new portfolio headline.
- **Priority 2:** country breadth expansion subject to liquidity/credit eligibility fixed ex ante.
- **Priority 3:** tenor reliability at formation time, then forwards/IRS implementation and model-implied convergence horizons.
- **Conditional:** credit state/transition models and multi-factor affine extensions after baseline false-positive risks are quantified.

These proposals are not implemented in the historical evidence included here.
