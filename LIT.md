# Literature Review — SPY Volatility Regime Detection

This log tracks the papers and articles that shaped this project's research
direction, organized by the role each one played. See DECISIONS.md for how
these findings translated into actual project decisions.

## Core papers behind the ECTS/ECOTS framing

- Early Classification of Time Series: A Survey and Benchmark (Nov 2025)
  https://arxiv.org/abs/2406.18332
  Reviewed ~50 core papers. Finance is never mentioned as an ECTS
  application domain anywhere in the paper.

- Open challenges for Machine Learning based Early Decision-Making research (2022)
  https://arxiv.org/pdf/2204.13111
  Lays out the field's unresolved problems.

- ml_edm package: a Python toolkit for Machine Learning based Early Decision Making
  https://arxiv.org/pdf/2408.12925
  The open-source library behind ECTS/ML-EDM.

- Early Classification of Time Series in Non-Stationary Cost Regimes (Jan 2026)
  https://arxiv.org/abs/2602.00918
  Cost of lateness is not fixed. Flagged as largely unexplored. Maps
  directly onto market crisis vs. calm-period stakes.

- Confidence-Guided Learning Process for Continuous Classification of Time Series
  https://arxiv.org/pdf/2208.06883
  CCTS, the no-fixed-endpoint, repeated-decisions extension that fits
  markets better than vanilla ECTS.

## Classical quickest-detection lineage (the honest correction)

- Real-time financial surveillance via quickest change-point detection methods
  https://arxiv.org/html/1509.01570
  Confirms the classical CUSUM/Shiryaev-Roberts approach already has real
  financial applications.

- Numerical Comparison of Cusum and Shiryaev-Roberts Procedures for
  Detecting Changes in Distributions
  https://arxiv.org/pdf/0908.4119
  Technical comparison of the two classical methods used as the benchmark
  baseline for this project.

- The mirror of history: How to statistically identify stock market
  bubble bursts (2022)
  https://www.sciencedirect.com/science/article/abs/pii/S0167268122003481
  CUSUM applied to bubble-burst detection.

## Methodological rigor add-on

- Confronting Machine Learning With Financial Research
  https://arxiv.org/pdf/2103.00366
  Flags backtest overfitting and multiple testing bias as a widespread,
  under-corrected problem in financial ML.

## Background / context (established methodology, not novel)

- Early warning of regime switching in a financial time series: A
  heteroskedastic network model (PLOS One)
  https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0333734

- A Hybrid FIGARCH-LSTM Early Warning System for Volatility Regime
  Transitions in a Frontier Market: Evidence from Kenya
  https://doi.org/10.3390/jrfm19090689

## Final novelty claim (as recorded in DECISIONS.md)

The classical statistical approach to quickest change-point detection
(CUSUM, Shiryaev-Roberts) is well-established in finance. The modern,
flexible ML-based ECOTS/CCTS framework has not been applied to financial
volatility regime detection. This project benchmarks the modern approach
against the classical methods as the legitimate academic baseline.