import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as data
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates

style.use('ggplot')

start = dt.datetime(2018,1,1)
end = dt.datetime.now()

df = data.DataReader('NVDA', 'morningstar',start,end)
df.reset_index(inplace = True) #Creates a new index and pushes Date & Symbol to columns
df.set_index('Date',inplace = True) #Sets the index to be Date
df = df.drop('Symbol',axis = 1) #remove the Symbol column

df_ohlc = df['Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()
df_ohlc.reset_index(inplace=True)
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

# print(df_ohlc.head())
 
ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
ax1.xaxis_date()

candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)
plt.show()
