import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(r'C:\Users\Barbara\Documents\Katoliški inštitut\Drugi letnik\Magistrska\Podatki\ZbraneVrednostiAdjClose2018-2021.xlsx')
# print(df)

aapl = df['AAPL']
amzn = df['AMZN']
msft = df['MSFT']
btc = df['BTC-USD']
eth = df['ETH-USD']
doge = df['DOGE-USD']
sp500 = df['S&P 500']

instrument = sp500

# Create 12 days exponential moving average column
df['12_EMA'] = instrument.ewm(span = 12, adjust = False).mean()
# Create 26 days exponential moving average column
df['26_EMA'] = instrument.ewm(span=26, adjust=False).mean()
# Calculate MACD
exp1 = instrument.ewm(span=12, adjust=False).mean()
exp2 = instrument.ewm(span=26, adjust=False).mean()
macd = exp1 - exp2
df['MACD'] = macd
# Create signal line
df['Signal Line'] = macd.ewm(span=9, adjust=False).mean()


df.to_excel (r'C:\Users\Barbara\Documents\Katoliški inštitut\Drugi letnik\Magistrska\Izračuni\MACD\MACD_Calculator_SP500.xlsx', header=True)



# If we were to use YFinance data

# import datetime as dt
# import pandas_datareader as pdr
# ticker = pdr.get_data_yahoo("AAPL", start="2018-01-01", end="2022-01-01")['Adj Close']
# print(ticker)

# exp1 = ticker.ewm(span=12, adjust=False).mean()
# exp2 = ticker.ewm(span=26, adjust=False).mean()
# macd = exp1 - exp2
# exp3 = macd.ewm(span=9, adjust=False).mean()