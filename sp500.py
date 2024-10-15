import pandas as pd
import numpy as np
import yfinance as yf
import statistics
import numpy as np
import scipy.stats as st
import scipy
from scipy.stats import sem

d = yf.download("^GSPC", start="2018-01-01", end="2022-01-01",group_by="ticker")

sp500 = yf.Ticker("^GSPC")

print(sp500.history(start="2018-01-01", end="2022-01-01"))

d.to_excel (r'C:\Users\Barbara\Documents\Katoliški inštitut\Drugi letnik\Magistrska\Python\export_sp500.xlsx', header=True)