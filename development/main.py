# standard libaries
import os
import requests
import pickle
import time
import sqlite3
import datetime as dt
# third party packages
import pandas as pd
from bs4 import BeautifulSoup
from alpha_vantage.timeseries import TimeSeries
# local packages


'''
Doing stuff.
'''


def Save500():
    '''
    Pulls list of S&P 500 companies and ticker symbols from wikipedia.
    Arguements:
    Returns:
    '''
    source = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = BeautifulSoup(source.text, 'lxml')

    tickers = []
    companies = []
    sectors = []
    table = soup.find('table', attrs={'class': 'wikitable sortable', 'id': 'constituents'})

    # iterates through rows in table skipping header
    for row in table.find_all('tr')[1:]:
        ticker = row.find_all('td')[0].text
        if ticker.find('.'):
            ticker = ticker.replace('.', '-').strip()
        company = row.find_all('td')[1].text
        sector = row.find_all('td')[3].text
        tickers.append(ticker)
        companies.append(company)
        sectors.append(sector)
        combined = list(zip(tickers, companies, sectors))

    with open('sp500tickers.pickle', mode='wb') as f:
        pickle.dump(tickers, f)
    with open('sp500companies.pickle', mode='wb') as f:
        pickle.dump(companies, f)
    with open('sp500sectors.pickle', mode='wb') as f:
        pickle.dump(sectors, f)

    return None


def GetData(reload=False):
    '''
    Gets stock data from Alpha Advantage
    Arguements
    '''

    if reload:
        tickers = Save500()
    else:
        with open('sp500tickers.pickle', mode='rb') as f:
            tickers = pickle.load(f)

    # if not os.path.exists('stock_dfs'):
    #     os.makedirs('stock_dfs')
# TODO:  if reload_data else condition for getting stock prices
#       current else statement doesn't allow updating stocks each today
#       add ETFs and bonds like VOO
#       add interest rate
#       can add NYSE: to symbol to define which exchange
#       need to concert date/time to string and compare to slice/ammend data
#       need to fix ticker arguement in get_daily_adjusted to use str.replace method

    for count, ticker in enumerate(tickers):
        print(count, ":", ticker)
        if not os.path.exists('stock_dfs/{}.csv'.format(ticker.replace('.', '-'))):
            df, meta_data = TimeSeries(key='key.text', output_format='pandas').get_daily_adjusted(
                symbol=ticker.replace('.', '-'), outputsize='full')
            df.rename(columns=lambda x: x.lstrip(
                '123456789.').strip().replace(' ', '_'), inplace=True)
            df.to_csv('stock_dfs/{}.csv'.format(ticker.replace('.', '-')))
            time.sleep(10)
        else:
            print('Already have {}'.format(ticker))
    return None


def RenameColumns():
    '''
    Convert column headers of Alpha Vantage data
    '''
#   TODO:
#       use pandas to read sql from database instead of csv files
    with open('sp500tickers.pickle', mode='rb') as f:
        tickers = pickle.load(f)

    for ticker in tickers:
        print(ticker)
        df = pd.read_csv(
            'stock_dfs/{}.csv'.format(ticker.replace('.', '-')), parse_dates=True, index_col=0)
        df.rename(columns=lambda x: x.lstrip(
            '123456789.').strip().replace(' ', '_'), inplace=True)
        # need to reload stock data or delete second column in current data
        df.to_csv('stock_dfs/{}.csv'.format(ticker.replace('.', '-')))
    return None


def MakeTable():
    conn = sqlite3.connect('stocks.db')
    c = conn.cursor()
    c.execute(
        '''CREATE TABLE IF NOT EXISTS stocks(
            id INTEGER PRIMARY KEY,
            ticker TEXT UNIQUE,
            company TEXT UNIQUE,
            sector TEXT UNIQUE)
            ''')

# save the changes
    conn.commit()

# close the connection
    conn.close()
    return


def UpdateTable():

    with open('sp500tickers.pickle', mode='rb') as f:
        tickers = tuple(pickle.load(f))
    with open('sp500companies.pickle', mode='rb') as f:
        companies = tuple(pickle.load(f))
    with open('sp500sectors.pickle', mode='rb') as f:
        sectors = tuple(pickle.load(f))
        print(type(sectors))
        conn = sqlite3.connect('stocks.db')
        c = conn.cursor()
# need to convert input data into a string format to store in database
    for i in tickers:
        c.execute("INSERT INTO stocks (ticker, company, sector) VALUES (?, ?, ?)",
                  (tickers, companies, sectors))

    # save the changes
    conn.commit()

    # close the connection
    conn.close()

    return None


def InsertData():
    with open('sp500tickers.pickle', mode='rb') as f:
        tickers = pickle.load(f)
    for count, ticker in enumerate(tickers):
        df, meta_data = TimeSeries(key='key.text', output_format='pandas').get_daily_adjusted(
            symbol=ticker.replace('.', '-'), outputsize='full')
        # df.rename(columns=lambda x: x.lstrip(
        #     '123456789.').strip().replace(' ', '_'), inplace=True)

    return None


# MakeTable()
Save500()
UpdateTable()
