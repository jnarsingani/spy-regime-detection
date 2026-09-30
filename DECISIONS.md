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

## Scope and Limitations: Reactive detection, not event prediction
Date: 2026-09-29

**Context**
Market volatility regime shifts are often triggered by real-world events
(rate decisions, geopolitical shocks, earnings surprises, corporate
failures) that are not knowable in advance from price data alone. It is
important to be precise about what this project can and cannot claim.

**Scope statement**
This project detects regime shifts as they manifest in price and return
data. It does not predict the underlying events that cause those shifts,
and it makes no claim to anticipate news, policy decisions, or other
unannounced real-world triggers before they occur.

**Rationale**
The system has no access to any information beyond historical price data
(and derived quantities such as returns and realized volatility). It
cannot see news, earnings calendars, or macroeconomic releases. When an
unannounced event occurs, its effects appear in the data almost
immediately, as unusual price moves and a spike in realized volatility.
The system's job is to recognize that reaction pattern and flag it as
early as possible after it starts appearing, not to foresee the event
itself before it happens.

This mirrors the explicit scope of the quickest change-point detection
literature (CUSUM, Shiryaev-Roberts) and the ECTS/ECOTS literature: both
fields are built around minimizing the delay between "the change begins
manifesting in observable data" and "the system detects it," not
predicting the cause of the change in advance. This is a well-established,
legitimate research problem in its own right, not a workaround for a
missing capability.

**What this means practically**
- The system is a fast-reaction tool, analogous to a smoke detector: it
  notices the effects of a shock quickly, it does not predict the shock.
- Event-driven or NLP-based forecasting (news sentiment, economic
  calendars, earnings surprise models) is explicitly out of scope for this
  project and would require a fundamentally different data source and
  model design.
- This scope should be stated plainly in any write-up, portfolio
  presentation, or PhD application material referencing this project, to
  avoid overclaiming predictive power the system does not have.