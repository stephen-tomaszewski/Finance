import sqlite3
import pandas as pd
import pickle
from alpha_vantage.timeseries import TimeSeries

conn = sqlite3.connect('stocks.db')
c = conn.cursor()


def make_table():
    c.execute('''CREATE TABLE IF NOT EXISTS stocks(
            id INTEGER PRIMARY KEY,
            symbol TEXT UNIQUE,
            company TEXT UNIQUE)
            ''')


# # save the cahnges
conn.commit()

# # close the connection
# conn.close()

    return


def insert_data():
        with open('sp500tickers.pickle', mode='rb') as f:
            tickers = pickle.load(f)
            for ticker in tickers:
                df, meta_data = TimeSeries(key='key.text', output_format='pandas').get_daily_adjusted(
                    symbol=ticker.replace('.', '-'), outputsize='full')
                df.rename(columns=lambda x: x.lstrip(
                    '123456789.').strip().replace(' ', '_'), inplace=True)

    return

make_table()
