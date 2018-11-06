import pandas as pd
import numpy as np
import sys
import random
import matplotlib.pyplot as plt
import ccxt
import os
import seaborn as sns
from sklearn import neighbors
import time
%matplotlib inline

df = pd.read_csv('../data/historical_prices.csv')

df['date'] = pd.to_datetime(df['date'], unit='ms')

knn = neighbors.KNeighborsRegressor(n_neighbors=10)
x = pd.DataFrame(df['BTC'])
y = df['ETH']
knn.fit(x, y)

# Prediction line
T = np.arange(min(df['BTC']), max(df['BTC']), 0.1)[:, np.newaxis]

y_ = knn.predict(T)
plt.scatter(x, y, c='k', label='data')
plt.plot(T, y_, c='g', label='prediction')
plt.legend()
plt.show()

# -------------------------------------------------------------------------
# basic chart of price data - average time frame between data points is 2:29 min
exchange = ccxt.bittrex()

btc = np.array(exchange.fetch_ohlcv("BTC/USDT", "5m"))[:, :2]



exchange = ccxt.binance({'rateLimit': 10000,'enableRateLimit': True})
start_date = exchange.parse8601('2018-11-01 00:00:00')
data = []

msec = 1000
minute = 60 * msec

now = exchange.milliseconds()

while start_date < now:
	candles = exchange.fetch_ohlcv('BTC/USDT', '1m', start_date)
	first = candles[0][0]
	last = candles[-1][0]
	start_date += len(candles) * minute
	data += candles


df = pd.DataFrame(np.array(data)[:, :2], columns=["date", "price"])
df['date'] = pd.to_datetime(df['date'], unit='ms')

# Chart of price data
plt.plot(df['date'], df['price'])
plt.xticks(rotation=45)
plt.show()
# ------------------------------------------------------------------------------
# x = daily price
# y = rolling average
# 0 or 1 attributed to points
#
# Let's say that if a moving average is above price, we expect price to go down
# if moving average is below price, we expect price to go up
# Analyze the same # of periods following, see if there's a majority
# 1 = majority are what we expect, 0 = majority is not what we expect

rolling_15 = df['price'].rolling(window=15).mean()
rolling_60 = df['price'].rolling(window=60).mean()
ewma_15 = df['price'].ewm(span=15).mean()
ewma_60 = df['price'].ewm(span=60).mean()


avg_df = pd.DataFrame(
	{'date': df['date'],
	 'price': df['price'],
	 'rolling_15': rolling_15,
	 'rolling_60': rolling_60,
	 'ewma_15': ewma_15,
	 'ewma_60': ewma_60
	})

avg_df = avg_df.dropna().reset_index(drop=True)

predictions = []
for i in range(0,len(avg_df)-15):
	ewma = avg_df['ewma_15'][i]
	price = avg_df['price'][i]

	results = 0
	for x in range(1,16):
		if ewma < avg_df['price'][i + x]:
			results -= 1
		else:
			results += 1

	if ewma < price:
		if results >= 3:
			predictions.append(1)
		else:
			predictions.append(0)
	else:
		if results <= -3:
			predictions.append(1)
		else:
			predictions.append(0)

avg_df['outcome'] = 0

for i, result in enumerate(predictions):
	avg_df.loc[avg_df['outcome'], i] = result


avg_df['outcome'] = predictions
avg_df = avg_df.dropna().reset_index(drop=True)





















test = avg_df[:250]
plt.plot(test['date'], test['price'], linewidth=0.5, color='black')
plt.plot(test['date'], test['rolling_15'], linewidth=0.5, color='blue')
plt.plot(test['date'], test['ewma_15'], linewidth=0.5, color='red')
plt.xticks(rotation=45)
plt.show()

# ------------------------------------------------------------------------------
# Future predictions - doesn't work
# split into training and testing data
from sklearn.preprocessing import MinMaxScaler

prices = df.loc[:, 'price'].values

train = prices[:len(prices)//2]
test = prices[len(prices)//2:]

# Scale data to be between 0 and 1
scaler = MinMaxScaler(feature_range=(0,1))

train = train.reshape(-1,1)
test = test.reshape(-1,1)

train = scaler.fit_transform(train).reshape(-1)
test = scaler.fit_transform(test).reshape(-1)


# Exponential moving average
window_size = 100

decay = 0.5
running_mean = 0.0

run_avg_x = []
mse_errors = []
run_avg_predictions = [running_mean]

for i in range(1,len(train)):
	running_mean = running_mean * decay + (1 - decay) * train[i-1]
	run_avg_predictions.append(running_mean)
	mse_errors.append((run_avg_predictions[-1] - train[i]) ** 2)
	run_avg_x.append(df['date'][len(df)-1] + i * date_interval)

plt.figure(figsize = (8, 6))
plt.plot(df['date'], df['price'], color='orange', label='True')
plt.plot(x=np.array(run_avg_x), y=np.array(run_avg_predictions), color='blue', label='Predicted')
plt.xticks(rotation=45)
plt.show()

run_avg_x
