import os
import pickle
import datetime as dt

import numpy as np
import pandas as pd

from save_sp500_tickers import Save500

# ticker = 'A'
# last_updated = dt.datetime(2019-05-03)
# df = pd.read_csv('stock_dfs/{}.csv'.format(ticker),
#                  parse_dates=True, index_col=0, header=0)
# last_date = df[-1:1]
# print(last_date)
# if dt.date.weekday(dt.datetime.now()) < 5:
#     now = dt.datetime.now()
#     print('works')

# cur_date = dt.date.isoweekday(dt.date.now())
# if cur_date < 6 & cur_date.days:

print(type(dt.datetime.utcnow()))
print(type(dt.date.today()))
print(type(dt.datetime.date(dt.datetime.now())))
