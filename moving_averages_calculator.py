# https://towardsdatascience.com/making-a-trade-call-using-simple-moving-average-sma-crossover-strategy-python-implementation-29963326da7a

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from datetime import date
import time
# df = pd.DataFrame({'data': ["2018-01-02", "2021-12-29", "2021-12-30"]})
# df["data"].apply(lambda x: datetime.datetime.strptime(x, '%Y-%m-%d').strftime('%b-%y'))

df = pd.read_excel(r'C:\Users\Barbara\Documents\Katoliški inštitut\Drugi letnik\Magistrska\Podatki\ZbraneVrednostiAdjClose2018-2021.xlsx')
print(df)

aapl = df['AAPL']
amzn = df['AMZN']
msft = df['MSFT']
btc = df['BTC-USD']
eth = df['ETH-USD']
doge = df['DOGE-USD']
sp500 = df['S&P 500']

instrument = sp500

# SMAs
# create 20 days simple moving average column
df['20_SMA'] = instrument.rolling(window = 20, min_periods = 1).mean()
# create 50 days simple moving average column
df['50_SMA'] = instrument.rolling(window = 50, min_periods = 1).mean()

df['SignalSMA'] = 0.0
df['SignalSMA'] = np.where(df['20_SMA'] > df['50_SMA'], 1.0, 0.0)

df['PositionSMA'] = df['SignalSMA'].diff()
# display first few rows
df.head()
print(df)

plt.figure(figsize = (20,10))
# plot close price, short-term and long-term moving averages
instrument.plot(color = 'k', label= 'instrument')
df['20_SMA'].plot(color = 'b',label = '20-day SMA')
df['50_SMA'].plot(color = 'g', label = '50-day SMA')
# plot 'buy' signals
plt.plot(df[df['PositionSMA'] == 1].index,
         df['20_SMA'][df['PositionSMA'] == 1],
         '^', markersize = 15, color = 'g', label = 'buy')
# plot 'sell' signals
plt.plot(df[df['PositionSMA'] == -1].index,
         df['20_SMA'][df['PositionSMA'] == -1],
         'v', markersize = 15, color = 'r', label = 'sell')
plt.ylabel('Cena v USD', fontsize = 15 )
plt.xlabel('Datum', fontsize = 15 )
plt.title('SMA Crossover', fontsize = 20)
plt.legend()
plt.grid()
# plt.show()



# EMAs
# Create 20 days exponential moving average column
df['20_EMA'] = instrument.ewm(span = 20, adjust = False).mean()
# Create 50 days exponential moving average column
df['50_EMA'] = instrument.ewm(span=50, adjust=False).mean()
# create a new column 'Signal' such that if 20-day EMA is greater   # than 50-day EMA then set Signal as 1 else 0

df['SignalEMA'] = 0.0
df['SignalEMA'] = np.where(df['20_EMA'] > df['50_EMA'], 1.0, 0.0)
# create a new column 'Position' which is a day-to-day difference of # the 'Signal' column
df['PositionEMA'] = df['SignalEMA'].diff()

print(df)

plt.figure(figsize = (20,10))
# plot close price, short-term and long-term moving averages
instrument.plot(color = 'k', lw = 1, label = 'Close Price')
df['20_EMA'].plot(color = 'b', lw = 1, label = '20-day EMA')
df['50_EMA'].plot(color = 'g', lw = 1, label = '50-day EMA')
# plot 'buy' and 'sell' signals
plt.plot(df[df['PositionEMA'] == 1].index,
         df['20_EMA'][df['PositionEMA'] == 1],
         '^', markersize = 15, color = 'g', label = 'buy')
plt.plot(df[df['PositionEMA'] == -1].index,
         df['20_EMA'][df['PositionEMA'] == -1],
         'v', markersize = 15, color = 'r', label = 'sell')
plt.ylabel('Cena v USD', fontsize = 15 )
plt.xlabel('Datum', fontsize = 15 )
plt.title('EMA Crossover', fontsize = 20)
plt.legend()
plt.grid()
# plt.show()

df.to_excel (r'C:\Users\Barbara\Documents\Katoliški inštitut\Drugi letnik\Magistrska\Izračuni\MA_Calculator_SP500.xlsx', header=True)