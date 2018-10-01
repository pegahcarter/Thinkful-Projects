# Final Capstone Proposal

#### By: Carter Carlson

---

### Introduction
The cryptocurrency market is highly volatile and [recent studies](https://www.sifrdata.com/cryptocurrency-correlation-matrix/)
show that the majority of cryptocurrencies have a strong positive correlation
with one another.  A popular investment strategy for cryptocurrency enthusiasts is
to [HODL](https://bitcointalk.org/index.php?topic=375643.0) (Hold On for Dear Life),
which was created when a Bitcoin fan misspelled "hold" several times in a drunken
blog rant.  And while many people in the crypto community swear to HODL, taking
investment advice from someone on the internet drunk on whiskey is probably not
the best idea.  In this analysis, I will compare two different investment strategies
for cryptocurrency (HODL and rebalancing), so hold on, and we will see how the
HODL strategy actually performs.

With the cryptocurrency market valued at several hundred billion dollars, it has
transformed from the "currency of the dark web" in which people use Bitcoin to buy
drugs and illegal services, to a financial medium that banks are considering to
use for anything from faciliting cross-border payments to including in exchange-traded
funds.  That being said, it's possible that in the future cryptocurrency investments
are as commonplace as 401k's.  This solution is aimed at maximizing returns for
the average investor that does not have access to the financial instruments offered
to high net-worth individuals.

---
### Analysis Details
* 1,000 random baskets of 5 coins selected from a group of 30 coins
* Simulate overall HODL performance over a one-year time frame
* With the same baskets, simulate daily rebalancing
	1. Take historical price of coins by day
	2. Calculate dollar value of each coin holding, and weight of coin in portfolio
	3. Sell % of coin above average weight to purchase coins below average weight
	4. Repeat step 3 until the basket of coins have equal weight
	5. Go to the next day, and start from step 1

After the simulations, we will be able to determine if a rebalanced portfolio, on
average, outperforms or underperforms their HODL counterpart.

---
### Techniques Used in Analysis
* Data aggregation/cleansing
* Data visualization
* Data standardization
* Machine Learning analysis
* Feature engineering
* Time series analysis

---
### Data Sources

#### Total market cap historical prices
I was unable to find a website that provided an API to pull historical market cap
prices, so I had to manually download a [CSV file](https://coin.dance/stats/marketcaphistorical).
The date range used for this analysis is 1/1/2017 - 9/15/2018.


#### Coin historical prices
Coin prices were pulled by using the API for Binance with the [CCXT Python library](https://github.com/ccxt/ccxt).  

---

### Challenges
Most cryptocurrencies were developed in the last few years, so there is not a lot
of historical data available.  Also, the overall cryptocurrency market value has
had more positive movements than negative movements, so our analysis will be slightly
skewed compared to analyzing a time frame with an even number of positive and
negative movements. To combat skewness, we will take all one-year starting and
ending market cap differences, calculate the median difference, and use that time
frame as the basis for our analysis.
