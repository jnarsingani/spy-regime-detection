# Decision log
Every structural choice gets logged here before it becomes code.

## Decision 1: Asset universe, granularity, and forcast horizon
- **Decision:** SPY only, daily OHLC, 1-day/5-day/22-day forecast horizons
- **Alternatives considered:** multi-asset basket (rejected: adds cross-asset complexity before single-asset pipeline is proven); intraday data (rejected: unnecessary complexity at chosen horizons)
- **What would make us revisit:** if MVP pipeline proves out cleanly, add a second ticker using the same pipeline as a validation step, not a redesign