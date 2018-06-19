import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as data

style.use('ggplot')

start = dt.datetime(2018,1,1)
end = dt.datetime.now()

df = data.DataReader('NVDA', 'morningstar',start,end)
df.reset_index(inplace = True) #Creates a new index and pushes Date & Symbol to columns
df.set_index('Date',inplace = True) #Sets the index to be Date
df = df.drop('Symbol',axis = 1) #remove the Symbol column

# print(df.tail(7)) #Gives the last 7 days from the date range specified

df['100MovingAvg'] = df['Close'].rolling(window=10, min_periods=0).mean()
print(df.head())

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)

ax1.plot(df.index, df['Close'])
ax1.plot(df.index, df['100MovingAvg'])
ax2.bar(df.index, df['Volume'])

plt.show()

