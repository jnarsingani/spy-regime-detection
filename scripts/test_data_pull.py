import yfinance as spy_source

data = spy_source.download("SPY", start = "2000-01-01", auto_adjust= False)
print(data.shape)
print(data.head())
print(data.tail())