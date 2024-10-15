#optional installations:
#!pip install yfinance --upgrade --no-cache-dir
#!pip3 install pandas_datareader
#!pip3 install pandas --upgrade

# better display
from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))

# ___library_import_statements___
import pandas as pd

# for pandas_datareader, otherwise it might have issues, sometimes there is some version mismatch
pd.core.common.is_list_like = pd.api.types.is_list_like

import pandas_datareader.data as web
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import time

#newest yahoo API
import yfinance as yahoo_finance


def f_plot_selected(df, columns, start_index, end_index):
    """Plot the desired columns over index values in the given range."""
    # takes a dataframe, columns (list) that we want to print and range of rows
    # note: df.ix is deprecated now
    f_plot_data(df.loc[start_index:end_index])
    # use df.loc not df.iloc since we use datetime as index


def f_get_data(symbols, dates, start_time, today):
    """Read stock data (adjusted close) for given symbols from yahoo finance"""
    df = pd.DataFrame(index=dates)
    print(df.head())

    if 'AAPL' not in symbols:  # add AAPL for reference, if absent
        symbols.insert(0, 'AAPL')

    for symbol in symbols:
        # yahoo gives only daily historical data, more granular data stream is hard to get for free
        connected = False
        while not connected:
            try:
                ticker_df = web.get_data_yahoo(symbol, start=start_time, end=today)
                connected = True
                print('connected to yahoo')
            except Exception as e:
                print("type error, something is wrong: " + str(e))
                time.sleep(10)
                pass

                # reset index from dates to index numbers
        # print(ticker_df.head(2))
        #       Date        High
        # 2017-01-03  128.190002
        # 2017-01-04  130.169998
        ticker_df = ticker_df.reset_index()
        # print(ticker_df.head(2))
        #         Date        High
        # 0 2017-01-03  128.190002
        # 1 2017-01-04  130.169998
        ticker_df.set_index('Date', inplace=True, drop=False)

        df_temp = ticker_df[['Date', 'Adj Close']]
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp[symbol])

        if symbol == 'AAPL':  # drop dates AAPL did not trade
            df = df.dropna(subset=["AAPL"])

    return df


def f_normalize_data(df):
    """normalizes stock data in respect to price in day 1,
    this way price on the first day starts at 1$ for any given stock"""
    # return df/df.ix[0,:]      # deprecated option
    return df / df.iloc[0, :]  # use df.iloc not df.loc since index is number


def f_plot_data(df, title="Stock prices"):
    """Plot stock prices with a custom title and meaningful axis labels."""

    ax = df.plot(title=title, fontsize=12, figsize=(20, 10))
    ax.set_xlabel("Datum")
    ax.set_ylabel("Cena")

    # plt.figure(figsize=(20, 10), dpi= 120, facecolor='w', edgecolor='k')
    plt.title('Relativna sprememba cene')
    plt.legend(loc='upper left', fontsize=12)
    plt.tight_layout()
    plt.style.use('bmh')
    plt.grid(True)
    plt.show()


def f_run():
    # Define a date range
    start_time = datetime.datetime(2018, 1, 1)
    # end_time = datetime.datetime(2018, 6, 20)
    today = datetime.datetime.now().date().isoformat()
    dates = pd.date_range(start_time, today)

    # Choose stock symbols to read
    symbols = ['AAPL', 'AMZN', 'MSFT', 'BTC-USD', 'ETH-USD']
    # AAPL will be added in f_get_data() function automatically

    # Get stock data
    df = f_get_data(symbols, dates, start_time, today)
    df = f_normalize_data(df)

    # Slice and plot
    f_plot_selected(df, ['AAPL', 'AMZN', 'MSFT', 'BTC-USD', 'ETH-USD'], start_time, today)

if __name__ == "__main__":
    f_run()

