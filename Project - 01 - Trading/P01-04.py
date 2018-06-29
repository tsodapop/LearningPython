import numpy as numpy
import pandas as pd
import pickle
from collections import Counter

def process_data_for_labels(ticker):
	hm_days = 5
	df = pd.read_csv('sp500_joined_closes.csv', index_col=0)
	tickers = df.columns.values.tolist()
	df.fillna(0, inplace=True)

	for i in range(1, hm_days+1):
		df['{}_{}d'.format(ticker, i)] = (df[ticker].shift(-i) - df[ticker]) / df[ticker]

	df.fillna(0, inplace=True)
	return tickers, df

def buy_sell_hold(*args):
	cols = [c for c in args]
	requirement = 0.02
	for col in cols:
		if col > requirement:
			return 1 #buy
		if col < -requirement:
			return -1 #sell
		return 0 #hold

def extract_featuresets(ticker):
	tickers, df = process_data_for_labels(ticker)

	df['{}_target'.format(ticker)] = list(map(buy_sell_hold, 
									df['{}_1d'.format(ticker)],
									df['{}_2d'.format(ticker)],
									df['{}_3d'.format(ticker)]
									)) 
	vals = df['{}_target'.format(ticker)].values.tolist()
	str_vals = [str(i) for i in vals]
	print('Data Spread:', Counter(str_vals))

	df.fillna(0, inplace=True)
	df = df.replace([numpy.inf, -numpy.inf], numpy.nan)
	df.dropna(inplace=True)

	df_vals = df[[ticker for ticker in tickers]].pct_change()
	df_vals = df_vals.replace([numpy.inf, -numpy.inf], 0)
	df_vals.fillna(0, inplace=True)

	X = df_vals.values
	y = df['{}_target'.format(ticker)].values

	return X, y, df


# process_data_for_labels('AMD')	
extract_featuresets('AMD')