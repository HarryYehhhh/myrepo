import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplfinance as mpf

import yfinance as yf

qqq_daily = yf.download(["AAPL", "NVDA", "TSM"], start='2024-04-06', end='2024-06-20')
qqq_daily["Adj Close"].plot(title="QQQ Daily Adjusted Close", figsize=(5, 3))
plt.show()