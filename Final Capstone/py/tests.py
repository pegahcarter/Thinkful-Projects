'''
Wrangle your data. Get it into the notebook in the best form possible for your analysis and model building.

Explore your data. Make visualizations and conduct statistical analyses to explain
what’s happening with your data, why it’s interesting, and what features you intend
to take advantage of for your modeling.

Build a modeling pipeline. Your model should be build in a coherent pipeline of
linked stages that is efficient and easy to implement.

Evaluate your models. You should have built multiple models, which you should thoroughly
evaluate and compare via a robust analysis of residuals and failures.

Present and thoroughly explain your product. Describe your model in detail: why
you chose it, why it works, what problem it solves, how it will run in a production
like environment. What would you need to do to maintain it going forward?
'''
import pandas as pd
import numpy as np
import sys
import time
import matplotlib.pyplot as plt
import ccxt
import os
import statistics
from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
%matplotlib inline

try:
	path = 'C:/Users/18047/Documents/Project/Final Capstone/data/'
	historical_data = pd.read_csv(path + "historical prices.csv")
except:
	path = 'C:/Users/Carter/Documents/GitHub/Thinkful__Projects/Final Capstone/data/'

historical_data = pd.read_csv(path + 'historical prices.csv')

hodl_df = pd.read_csv(path + 'hodl.csv')
rebalanced_df = pd.read_csv(path + 'rebalanced.csv')

# list of coins used in each portfolio simulation
coins = historical_data.columns[1:].tolist()
cols = hodl_df.columns[1:]
coin_lists = [i.split('-') for i in cols]

# End prices
summary_df = pd.read_csv(path + 'summary.csv')
end_price_HODL = np.array(summary_df['end_price_HODL'] - summary_df['taxes_HODL'])
end_price_rebalanced = np.array(summary_df['end_price_rebalanced'] - summary_df['taxes_rebalanced'])
performance = list((end_price_rebalanced - end_price_HODL) / end_price_HODL)

# Dataframe to compare coin impact on outperforming HODL
df = pd.DataFrame(columns=coins)
df['beat market'] = performance
df['beat market'] = df['beat market'] > 0
df.fillna(False, inplace=True)

# Fill Dataframe with coins used for each simulation
for i in range(len(coin_lists)):
	for coin in coin_lists[i]:
		df.loc[i, coin] = True

# Feature importance analysis
tree = RandomForestClassifier()
X = df[coins]
Y = df['beat market']
tree.fit(X, Y)

feature_importance = tree.feature_importances_
feature_importance = 100 * (feature_importance / max(feature_importance))
temp = feature_importance.tolist()

# Take only top 10 features
top_feats = sorted(feature_importance,reverse=True)[:10]
sorted_features = np.array([temp.index(feat) for feat in top_feats])
pos = np.arange(sorted_features.shape[0]) + .5
plt.barh(pos, feature_importance[sorted_features], align='center')
plt.yticks(pos, X.columns[sorted_features])
plt.show()

diffs, coin_coeff = {}, {}

dates_used = list(hodl_df[hodl_df.columns[0]])
historical_data = historical_data.loc[historical_data['date'].isin(dates_used)]

for coin in coins:
	coin_data = np.array(historical_data[coin])

	diffs[coin] = (coin_data.max() - coin_data.min()) / coin_data.min()
	coin_coeff[coin] = (coin_data.std() / coin_data.mean())

sorted_diffs = sorted(diffs.items(), reverse=True, key=lambda x: x[1])
sorted_coin_coeff = sorted(coin_coeff.items(), reverse=True, key=lambda x: x[1])

sorted_diffs[:10]
sorted_coin_coeff[:10]




















# Date range used for simulations
start_date, end_date = historical_data['date'][0], historical_data['date'][len(historical_data)-1]
start_date = time.strftime('%m/%d/%Y', time.gmtime(start_date))
end_date = time.strftime('%m/%d/%Y', time.gmtime(end_date))
