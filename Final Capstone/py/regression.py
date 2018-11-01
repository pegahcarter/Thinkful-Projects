import pandas as pd
import numpy as np
import sys
import random
import matplotlib.pyplot as plt
import ccxt
import os
import seaborn as sns
from sklearn import neighbors
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

df = pd.read_csv('../data/summary.csv')
df.head()
hodl = df['HODL']
bin_size = (hodl.max() - hodl.min()) / 10
categories = list(range(1,11))

categories = {}
for i in range(1,11):
	categories[i] = hodl.min() + (i - 1)*bin_size

def find_bin(num):
	for key, val in categories.items():
		if num > val:
			return key
