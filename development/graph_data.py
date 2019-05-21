import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
import numpy as np
import pandas as pd
import datetime as dt


def graph_data_subplot2grid(ticker):
    '''
    Graphs stock ticker data
    Arguments:
    ticker (string) = ticker to plot
    '''
    df = pd.read_csv('~/Projects/Finance/stock_dfs/{}.csv'.format(ticker),
                     parse_dates=True, index_col=0, header=0)

    # print(df.index)
    columns = df.columns
    print(columns)
    # print(df[columns[4]])
    # print(df['5. adjusted close'])
    # print(df.loc)
    # print(df.head())

    style.use('ggplot')

    # plt.ylabel()
    fig1 = plt.figure(1)
    ax1 = plt.subplot2grid((4, 1), (0, 0), rowspan=3, colspan=1)
    ax1.plot(df['5. adjusted close'], label=columns[4])
    plt.title('Ticker: {}'.format(ticker))
    ax1.format_xdata = mdates.DateFormatter('%Y-%m-%d')
    ax1.yaxis.set_ticks_position('right')
    ax1.yaxis.set_label_position('right')
    ax1.yaxis.set_units('$')
    print(ax1.xaxis.get_tick_space())
    plt.legend()

    ax2 = plt.subplot2grid((4, 1), (3, 0), rowspan=1, colspan=1)
    ax2.plot(df['6. volume'], label=columns[5])
    ax2.yaxis.set_ticks_position('right')

    # ax2.format_xdata = mdates.DateFormatter('%Y-%m-%d')
    # fig1.autofmt_xdate()
    # plt.legend()

    plt.show()
    return
