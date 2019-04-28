import os
import pandas
import pickle
from alpha_vantage.timeseries import TimeSeries
import time
import save_sp500_tickers


def get_data_from_alpha(reload=False):
    '''
    Gets stock data from Alpha Advantage
    Arguements
    '''

    if reload:
        tickers = save_sp500_tickers()
    else:
        with open('sp500tickers.pickle', mode='rb') as f:
            tickers = pickle.load(f)

    if not os.path.exists('stock_dfs'):
        os.makedirs('stock_dfs')
# TODO:  if reload_data else condition for getting stock prices
#       current else statement doesn't allow updating stocks each today
#       add ETFs and bonds like VOO
#       can add NYSE: to symbol to define which exchange
#       need to concert date/time to string and compare to slice/ammend data
#       need to fix ticker arguement in get_daily_adjusted to use str.replace method
    for idx, ticker in enumerate(tickers):
        print(idx, ":", ticker)
        if not os.path.exists('stock_dfs/{}.csv'.format(ticker.replace('.', '-'))):
            data, meta_data = TimeSeries(key='key.text', output_format='pandas').get_daily_adjusted(
                symbol=ticker.replace('.', '-'), outputsize='full')
           # TODO: merge monthly adjusted, weekly adjusted, and daily adjusted to each csv to get more data and highest resolution
            data.to_csv('stock_dfs/{}.csv'.format(ticker.replace('.', '-')))
            time.sleep(10)
        else:
            print('Already have {}'.format(ticker))


def combine_data():
    '''
    Combine S&P 500
    '''
    return
