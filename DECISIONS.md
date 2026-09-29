## Decision: Use Adjusted Close (not raw Close) as the price series
Date: 2026-09-28

**Context**
SPY pays quarterly dividends and has had occasional stock splits historically.
Both are scheduled, known-in-advance corporate actions, not sentiment-driven
market moves. The project's core research question is detecting genuine
volatility regime shifts, so the price series used for return calculations
needs to reflect actual market-driven price changes only.

**Decision**
Use Adjusted Close (yfinance `Adj Close` column) as the price series for all
return and volatility calculations going forward. Raw Close will still be
pulled and cached alongside it for reference, but will not be used as model
input.

**Rationale**
Raw Close includes mechanical drops on ex-dividend dates and artificial
jumps/drops around stock splits. These are predictable, scheduled, and
priced in in advance, they are not the market reacting to new information
or shifting risk perception. Feeding raw Close into a regime-detection model
would introduce four small "false volatility" events per year (one per
dividend), every year, which the model would have no way to distinguish
from genuine volatility. This is noise unrelated to the phenomenon being
studied, not a tradeoff between two valid signals.

Note: this does not mean dividends have zero effect on the company's value,
a company that pays out cash is genuinely worth incrementally less. The
distinction is that this reduction is known and mechanical, not a reflection
of market sentiment or risk, which is what volatility regime detection is
meant to capture.

**Alternative considered**
Use raw Close and manually flag/exclude known dividend and split dates.
Rejected: yfinance's Adj Close already performs this adjustment correctly
and consistently across the full historical series, so manually flagging
dates would duplicate existing, tested logic and introduce more room for
error.

**Data caching**
Raw pull cached at `data/raw/spy_ohlc.parquet` (Parquet, via pyarrow) rather
than re-querying yfinance's API on every script run. Parquet preserves the
datetime index and column dtypes, unlike CSV.