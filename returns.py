import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader as web

apple = web.get_data_yahoo("DOGE-USD",
                            start = "2018-01-01",
                            end = "2022-01-01")

print(apple.head())

apple_daily_returns = apple['Adj Close'].pct_change()
apple_monthly_returns = apple['Adj Close'].resample('M').ffill().pct_change()
print(apple_daily_returns.head())
print(apple_monthly_returns.head())

fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
ax1.plot(apple_daily_returns)
ax1.set_xlabel("Datum")
ax1.set_ylabel("Odstotek")
# ax1.set_title("Dnevni donosi za Apple, Inc.")
plt.show()

fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
ax1.plot(apple_monthly_returns)
ax1.set_xlabel("Datum")
ax1.set_ylabel("Odstotek")
# ax1.set_title("Mesečni donosi za Apple, Inc.")
plt.show()

fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
apple_daily_returns.plot.hist(bins = 60)
ax1.set_xlabel("Dnevni donosi %")
ax1.set_ylabel("Odstotki")
# ax1.set_title("Dnevni donosi za Apple, Inc.")
ax1.text(-0.35,200,"Najnižji\ndonosi")
ax1.text(0.25,200,"Najvišji\ndonosi")
plt.show()