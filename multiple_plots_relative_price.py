import pandas as pd
import pandas_datareader.data as web
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import time
import yfinance


def f_plot_selected(df, columns, start_index, end_index):
    """Plot the desired columns over index values in the given range."""
    # takes a dataframe, columns (list) that we want to print and range of rows
    f_plot_data(df.loc[start_index:end_index])
    # use df.loc not df.iloc since we use datetime as index


def f_get_data(symbols, dates, start_time, today):
    """Read stock data (adjusted close) for given symbols from yahoo finance"""
    df = pd.DataFrame(index=dates)
    print(df.head())

    if 'BTC-USD' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'BTC-USD')

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

        if symbol == 'BTC-USD':  # drop dates SPY did not trade
            df = df.dropna(subset=["BTC-USD"])

    return df


def f_normalize_data(df):
    """normalizes stock data in respect to price in day 1,
    this way price on the first day starts at 1$ for any given stock"""
    # return df/df.ix[0,:]      # deprecated option
    return df / df.iloc[0, :]  # use df.iloc not df.loc since index is number


def f_plot_data(df, title=""):
    """Plot stock prices with a custom title and meaningful axis labels."""

    ax = df.plot(title=title, fontsize=12, figsize=(10, 10))
    # ax.set_xlabel("Datum")
    ax.set_ylabel("Relativna cena")

    plt.figure(figsize=(10, 10), dpi= 120, facecolor='w', edgecolor='k')
    # plt.title('Relativna sprememba v ceni')
    plt.legend(loc='upper left', fontsize=12)
    plt.tight_layout()
    plt.style.use('bmh')
    plt.grid(True)
    plt.show()


def f_run():
    # Define a date range
    start_time = datetime.datetime(2018, 1, 1)
    end_time = datetime.datetime(2021, 12, 31)
    today = datetime.datetime.now().date().isoformat()
    dates = pd.date_range(start_time, today)

    # Choose stock symbols to read
    symbols = ['DOGE-USD']
    # SPY will be added in f_get_data() function automatically

    # Get stock data
    df = f_get_data(symbols, dates, start_time, end_time)
    df = f_normalize_data(df)

    # Slice and plot
    f_plot_selected(df, ['DOGE-USD'], start_time, today)

if __name__ == "__main__":
        f_run()