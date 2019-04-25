import os
import pandas
import pickle
from alpha_vantage.timeseries import TimeSeries
import time

def merge_data(reload=False):
    '''
    Gets stock data from Alpha Advantage API
    Arguements
    '''

    if reload:
        tickers = save_sp500_tickers
    else:
        with open('sp500tickers.pickle', mode='rb') as f:
            tickers = pickle.load(f)

    if not os.path.exists('stock_dfs'):
        os.makedirs('stock_dfs')
# TODO:  if reload_data else condition for getting stock prices
#       current else statement doesn't allow updating stocks each today
    # symbol = TimeSeries(key='3F90HP4TSABAS5Q6').get_symbol_search(keywords='Berkshire')
    # print(symbol)
    # BF-B equals brown-forman
    # data, meta_data = TimeSeries(key='3F90HP4TSABAS5Q6', output_format='pandas').get_daily_adjusted(symbol='BF-B', outputsize='full')
    # print(data.tail())

    for ticker in tickers:
        print(ticker)
        ticker = ticker.replace('.', '-')
        if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
            print(ticker)
            data, meta_data = TimeSeries(key='key.text', output_format='pandas').get_daily_adjusted(symbol=ticker, outputsize='full')
            data.to_csv('stock_dfs/{}.csv'.format(ticker))
        else:
            print('Already have {}'.format(ticker))


    return
