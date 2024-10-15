# https://handsoffinvesting.com/calculate-and-analyze-rsi-using-python/

import pandas as pd

df = pd.read_excel(r'C:\Users\Barbara\Documents\Katoliški inštitut\Drugi letnik\Magistrska\Podatki\ZbraneVrednostiAdjClose2018-2021.xlsx', header=0).set_index(['Datum'])
# print(df)

aapl = df['AAPL']
amzn = df['AMZN']
msft = df['MSFT']
btc = df['BTC-USD']
eth = df['ETH-USD']
doge = df['DOGE-USD']
sp500 = df['S&P 500']

instrument = doge

# print(df.head())
# print(df.info())

# Calculate Price Differences
df['diff'] = instrument.diff(1)

# Calculate Avg. Gains/Losses
df['gain'] = df['diff'].clip(lower=0).round(2)
df['loss'] = df['diff'].clip(upper=0).abs().round(2)

# Window Length
window_length = 14

# Get initial Averages
df['avg_gain'] = df['gain'].rolling(window=window_length, min_periods=window_length).mean()[:window_length+1]
df['avg_loss'] = df['loss'].rolling(window=window_length, min_periods=window_length).mean()[:window_length+1]

# View first SMA value
# print(df.iloc[window_length-1: window_length+2])

# Get WMS averages
# Average Gains
for i, row in enumerate(df['avg_gain'].iloc[window_length+1:]):
    df['avg_gain'].iloc[i + window_length + 1] =\
        (df['avg_gain'].iloc[i + window_length] *
         (window_length - 1) +
         df['gain'].iloc[i + window_length + 1])\
        / window_length
# Average Losses
for i, row in enumerate(df['avg_loss'].iloc[window_length+1:]):
    df['avg_loss'].iloc[i + window_length + 1] =\
        (df['avg_loss'].iloc[i + window_length] *
         (window_length - 1) +
         df['loss'].iloc[i + window_length + 1])\
        / window_length
# View initial results
# print(df[window_length-1:window_length+5])

# Calculate RS Values
df['rs'] = df['avg_gain'] / df['avg_loss']

# Calculate RSI
df['rsi'] = 100 - (100 / (1.0 + df['rs']))
# View Result
print(df)

df.to_excel (r'C:\Users\Barbara\Documents\Katoliški inštitut\Drugi letnik\Magistrska\Izračuni\RSI\RSI_Calculator_DOGE.xlsx', header=True)

