import yfinance as yf
import numpy as np
import pandas as pd
import seaborn as sns
import pandas_datareader.data as web
from datetime import datetime
import matplotlib.pyplot as plt

# Get the data for the stocks
spy = yf.download('SPY','2018-01-01','2022-01-01')
aapl = yf.download('AAPL','2018-01-01','2022-01-01')
amzn = yf.download('AMZN','2018-01-01','2022-01-01')
msft = yf.download('MSFT','2018-01-01','2022-01-01')
btc = yf.download('BTC-USD','2018-01-01','2022-01-01')
eth = yf.download('ETH-USD','2018-01-01','2022-01-01')
doge = yf.download('DOGE-USD','2018-01-01','2022-01-01')

spy_adj_close = spy['Adj Close']
aapl_adj_close = aapl['Adj Close']
amzn_adj_close = amzn['Adj Close']
msft_adj_close = msft['Adj Close']
btc_adj_close = btc['Adj Close']
eth_adj_close = eth['Adj Close']
doge_adj_close = doge['Adj Close']

# Plot the close price of a single stock
# aapl['Adj Close'].plot()
# plt.ylabel('Cena ($)')
# plt.xlabel('', rotation=0)
# plt.show()

# Plot multiple stocks on one graph

# create new dataframe with just closing price for each stock
df_stocks = pd.DataFrame({'SPY': spy['Adj Close'], 'AAPL': aapl['Adj Close'], 'AMZN': amzn['Adj Close'],
                   'MSFT': msft['Adj Close']})

df_crypto = pd.DataFrame({'BTC-USD': btc['Adj Close'],
                   'ETH-USD': eth['Adj Close'], 'DOGE-USD': doge['Adj Close']})


df_stocks.plot(figsize=(10,4))
plt.ylabel('Cena')
# plt.show()

df_crypto.plot(figsize=(10,4))
plt.ylabel('Cena')
# plt.show()

returnfstart = df_stocks.apply(lambda x: x / x[0])
returnfstart.plot(figsize=(10,4)).axhline(1, lw=1, color='black')
plt.xlabel('')
plt.ylabel('Relativni donosi')
plt.show()

returnfstart = df_crypto.apply(lambda x: x / x[0])
returnfstart.plot(figsize=(10,4)).axhline(1, lw=1, color='black')
plt.xlabel('')
plt.ylabel('Relativni donosi')
plt.show()