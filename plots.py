# You could extract the date from ticker_history[observation]
# It is a Pandas Series object, so here's how I'd do it:

import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# function getting data for the last x years with x weeks space
# from checking data and specific observation.
def stock_data(ticker, period, interval, observation):
    ticker = yf.Ticker(ticker)
    ticker_history = ticker.history(period, interval)
    print((ticker_history[observation]))
    sf = ticker_history[observation]
    df = pd.DataFrame({'Date': sf.index, 'Values': sf.values})

    x = df['Date'].tolist()
    y = df['Values'].tolist()

    plt.plot(x, y)
    plt.ylabel('Cena ($)')
    plt.xlabel('Datum', rotation=0)
    plt.show()

#^GSPC = S&P500

if __name__ == '__main__':
    stock_data('DOGE-USD', '5y', '1wk', 'Close')