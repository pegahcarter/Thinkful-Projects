import os
import sys
import time
import ccxt
import numpy as np
import pandas as pd

# pull epoch dates used for market caps
market_cap = pd.read_csv('../data/historical market cap.csv')
dates_epoch = market_cap['date']
date_range = [time.strftime('%m/%d/%Y', time.localtime(day)) for day in dates_epoch]

# Use coins listed on Bittrex
primary_exchange = ccxt.bittrex({'options': {'adjustForTimeDifference': True}})
market = primary_exchange.load_markets()
tickers = list(market.keys())

coins = set()
[[coins.add(coin) for coin in ticker.split('/') if coin != 'BTC'] for ticker in tickers]
coins = list(coins)

# Since we can't pull BTC/BTC, use BTC/USDT ticker.  Otherwise, use coin/BTC as ticker
tickers = [coin + '/BTC' for coin in coins]
coins.insert(0, 'BTC')
tickers.insert(0, 'BTC/USDT')

df = pd.DataFrame(index=[list(dates_epoch)])

for ticker in tickers:
	# Pull information if ticker exists
	try:
		data = np.array(primary_exchange.fetch_ohlcv(ticker, '1d'))[:, :2]
	except:
		continue

	coin_prices = [price \
				   for day, price in data \
				   if time.strftime('%m/%d/%Y', time.localtime(day/1000)) in date_range]

	# Only add coin if it has price data for the whole time frame
	if len(coin_prices) == len(date_range):
		df[ticker[:ticker.find('/')]] = coin_prices

# Since all coins are in BTC denomination, multiply by BTC price to get $ price
df[1:] *= df[0]
df.to_csv('C:/Users/18047/Documents/Project/Final Capstone/data/historical prices.csv')
