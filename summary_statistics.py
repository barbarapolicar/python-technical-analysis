import pandas as pd
import numpy as np
import yfinance as yf
import statistics
import numpy as np
import scipy.stats as st
import scipy
from scipy.stats import sem

# import data
d = yf.download("^GSPC AAPL AMZN MSFT BTC-USD ETH-USD DOGE-USD", start="2018-01-01", end="2022-01-01",group_by="ticker")
# print(d)

# print names of columns
# print(d.columns)

# define dataframe, exclude weekends & holidays from the dates
df = pd.DataFrame(d)
exclude_nas = df.dropna()
# print(exclude_nas.columns)

# change multi-index to single index
exclude_nas.columns = ["_".join(a) for a in exclude_nas.columns.to_flat_index()]
exclude_nas
# print(exclude_nas)

# The date is currently only the index number. Let's change it into a column:
df['Date'] = df.index
# print(df)

# print stock info (using exclude_nas for crypto to exclude weekends & holidays
aapl= yf.Ticker("aapl")
amzn = yf.Ticker("amzn")
msft = yf.Ticker("msft")
btc = exclude_nas["BTC-USD_Adj Close"]
eth = exclude_nas["ETH-USD_Adj Close"]
doge = exclude_nas["DOGE-USD_Adj Close"]

# stock statistics (aapl, amzn, msft):
# print adjusted close prices: change the ticker name before "history"!
historical = msft.history(start="2018-01-01", end="2022-01-01")
adj_close = historical["Close"]
# print(adj_close)

# variable: define, which instrument you wish to analyze
# instrument = adj_close
instrument = btc

# crypto statistics (btc, eth, doge):
# do not add the ticker name before history, but simply change the definition of the "instrument" term

# summary statistics
print(instrument.describe())

# median
median = "The median is " + str(instrument.median())
print(median)

# mode -> not exactly correct, use the Excel formula instead
mode = "The mode is " + str(statistics.mode(instrument))
# print(mode)

# standard error of mean
sem = "The standard error of the mean is " + str(sem(instrument))
print(sem)

# variance
variance = "The variance is " + str(statistics.variance(instrument))
print(variance)

# kurtosis (sploščenost)
kurtosis = "The kurtosis is " + str(scipy.stats.kurtosis(instrument))
print(kurtosis)

# asymmetry coefficient
asymmetry = "The asymmetry coefficient is " + str(scipy.stats.skew(instrument))
print(asymmetry)

# confidence interval
interval = st.t.interval(alpha=0.95, df=len(instrument)-1, loc=np.mean(instrument), scale=st.sem(instrument))
print(interval)

# export data to Excel

# df.to_excel (r'C:\Users\Barbara\Documents\Katoliški inštitut\Drugi letnik\Magistrska\Python\export_dataframe_1.xlsx', header=True)
# adj_close_aapl.to_excel (r'C:\Users\Barbara\Documents\Katoliški inštitut\Drugi letnik\Magistrska\Python\export_aapl_adj_close.xlsx', header=True)
# summary_aapl.to_excel (r'C:\Users\Barbara\Documents\Katoliški inštitut\Drugi letnik\Magistrska\Python\export_aapl_summary.xlsx', header=True)
# d.to_excel (r'C:\Users\Barbara\Documents\Katoliški inštitut\Drugi letnik\Magistrska\Python\export_all_instruments.xlsx', header=True)
# exclude_nas.to_excel (r'C:\Users\Barbara\Documents\Katoliški inštitut\Drugi letnik\Magistrska\Python\exclude_nas.xlsx', header=True)