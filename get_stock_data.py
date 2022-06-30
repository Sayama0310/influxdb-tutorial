import yfinance as yf

data = yf.download("MSFT", start="2021-01-01", end="2021-10-30")
print(data.to_csv())

