import os
import pandas as pd 

def symbol_to_path(symbol, base_dir = 'data'):
	return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def dates_creator():
	start_date = '2013-01-01'
	end_date = '2013-12-31'
	dates = pd.date_range(start_date, end_date)
	return dates

def get_data(symbols, dates):
	df = pd.DataFrame(index = dates)
	if 'SPY' not in symbols: # adding SPY as the main reference
		symbols.insert(0, 'SPY')
	for symbol in symbols:
		df_temp = pd.read_csv(symbol_to_path(symbol),
			index_col = 'Date',
			parse_dates = True,
			usecols = ['Date', 'Adj Close'],
			na_values = ['nan'])
		df_temp = df_temp.rename(columns = {'Adj Close': symbol})
		df = df.join(df_temp)
	
		if symbol == 'SPY':
			df = df.dropna(subset = ['SPY'])

	print(df)

symbols = ['AAPL', 'SPY' , 'IBM', 'GOOG', 'TSLA']

if __name__ == "__main__":
	dates = dates_creator()
	get_data(symbols, dates)