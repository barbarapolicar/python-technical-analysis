import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import pandas_datareader as web

apple = web.get_data_yahoo("AAPL",
                            start = "2018-01-01",
                            end = "2022-01-01")

# print(apple.head())

apple_daily_returns = apple['Adj Close'].pct_change()
# print(apple_daily_returns.head())


def variance(apple_daily_returns, ddof=0):
     n = len(apple)
     mean = sum(apple_daily_returns) / n
     return sum((x - mean) ** 2 for x in apple_daily_returns) / (n - ddof)

def stdev(apple_daily_returns):
    var = variance(apple_daily_returns)
    std_dev = math.sqrt(var)
    return std_dev


