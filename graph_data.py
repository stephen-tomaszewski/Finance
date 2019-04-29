import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import pandas as pd
import datetime as dt

ticker = 'A'
df = pd.read_csv('stock_dfs/{}.csv'.format(ticker), parse_dates=True, index_col=0, header=0)

# print(df.index)
columns = df.columns
print(columns)
# print(df[columns[4]])
# print(df['5. adjusted close'])
# print(df.loc)
# print(df.head())

style.use('ggplot')

# plt.ylabel()
fig = plt.figure(1)
ax1 = plt.subplot2grid((4, 1), (0, 0), rowspan=3, colspan=1)
ax1.plot(df['5. adjusted close'], label=columns[4])
# TODO:
#       Need to plot both plots.
# everything after this is plotted
fig = plt.figure(2)
ax2 = plt.subplot2grid((4, 1), (3, 0), rowspan=1, colspan=1)
ax2.plot(df['6. volume'], label=columns[5])
plt.xlabel("Date")
plt.title('Ticker: {}'.format(ticker))
plt.legend()
plt.show()
