import bs4 as bs
import datetime as dt
import os
import pandas as pd
import pandas_datareader.data as data
import pickle #serializes an object (in this case, the S&P 500)
import requests

def save_sp500_tickers():
	resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
	soup = bs.BeautifulSoup(resp.text,'lxml')
	table = soup.find('table',{'class':'wikitable sortable'})
	tickers = []

	for row in table.findAll('tr')[1:]:
		ticker = row.findAll('td')[0].text
		tickers.append(ticker)

	with open("sp500tickers.pickle","wb") as f:
		pickle.dump(tickers, f) 
	print(tickers)

	return tickers

save_sp500_tickers()

def get_data_from_yahoo(reload_sp500=False):
	if reload_sp500:
		tickers = save_sp500_tickers()
	else:
		with open("sp500tickers.pickle","rb") as f:
			tickers = pickle.load(f)
	if not os.path.exists('stock_dfs'):
		os.makedirs('stock_dfs')

	start = dt.datetime(2018,1,1)
	end = dt.datetime(2018,12,31)

	for ticker in tickers[:40]: #first 10 tickers of S&P500
		print(ticker)
		if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
			df = data.DataReader(ticker, 'morningstar', start, end)
			df.to_csv('stock_dfs/{}.csv'.format(ticker))
		else:
			print('Already have {}'.format(ticker))

get_data_from_yahoo()

def compile_data():
	with open("sp500tickers.pickle","rb") as f:
		tickers = pickle.load(f)

	main_df = pd.DataFrame()

	for count, ticker in enumerate(tickers[:40]):
		df = pd.read_csv('stock_dfs/{}.csv'.format(ticker))
		df.set_index('Date', inplace=True)

		df.rename(columns = {'Close': ticker}, inplace=True)
		df.drop(['Symbol','Open','High','Low','Volume'], 1, inplace=True)

		if main_df.empty:
			main_df = df
		else:
			main_df = main_df.join(df, how='outer')

		if count % 10 == 0:
			print(count)

	print(main_df.head())
	main_df.to_csv('sp500_joined_closes.csv')

compile_data()
