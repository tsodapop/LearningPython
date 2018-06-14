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

print(df.tail(7)) #Gives the last 7 days from the date range specified

df['High'].plot()
plt.legend()
plt.show()

'''------------------------------------------------------------------------------------------------------'''
'''
Things Learned:
6/14
1. reset_index and set_index allow you to choose which column you want as the actual index
2.inplace = True is to update the variable df in place, meaning we don't have to do df = ... again 
3. tail() gives you the number of Dates you want to be shown
'''