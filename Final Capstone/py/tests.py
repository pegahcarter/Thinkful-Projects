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
	path = 'C:/Users/Carter/Documents/' # note: add rest of path

historical_data = pd.read_csv(path + 'historical prices.csv')
hodl_df = pd.read_csv(path + 'hodl.csv')
rebalanced_df = pd.read_csv(path + 'rebalanced.csv')
summary_df = pd.read_csv(path + 'summary.csv')

start_date, end_date = historical_data['date'][0], historical_data['date'][len(historical_data)-1]
start_date = time.strftime('%m/%d/%Y', time.gmtime(start_date))
end_date = time.strftime('%m/%d/%Y', time.gmtime(end_date))
