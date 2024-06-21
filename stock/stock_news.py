import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.style as style
import seaborn as sns
import yfinance as yf
import mplfinance as mpf

# use Yahoo Finance to download historical data for QQQ
# over the last 15 years, from 2006-01-01 to 2021-01-01
# qqq_daily = yf.download("QQQ", start="2024-01-01", end="2024-06-20")
# qqq_daily["Adj Close"].plot(title="QQQ Daily Adjusted Close", figsize=(5, 3))
# plt.show()

data = yf.download(["AMD", "NVDA", "TSM"], start='2024-04-06', end='2024-06-20')
print(data)
data.to_csv('stock_compare.csv')
# qqq = yf.Ticker("QQQ")
# qqq_hist_0406 = qqq.history(start='2024-04-06', end='2024-06-20')
# print((qqq_hist_0406.High + qqq_hist_0406.Low) / 2)