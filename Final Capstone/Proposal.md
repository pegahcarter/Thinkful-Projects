# Final Capstone Proposal
#### By: Carter Carlson
---
## Introduction

The cryptocurrency market is highly volatile and [recent studies](https://www.sifrdata.com/cryptocurrency-correlation-matrix/) show that the majority of cryptocurrencies have a strong positive correlation with one another.  A popular investment strategy for cryptocurrency enthusiasts is to [HODL](https://bitcointalk.org/index.php?topic=375643.0) (Hold On for Dear Life), which was created when a Bitcoin fan misspelled "hold" several times in a drunken blog rant.  And while many people in the crypto community swear to HODL, taking investment advice from someone on the internet drunk on whiskey is probably not the best idea.  In this analysis I am going to compare two different investment strategies for cryptocurrency (HODL and rebalancing), so hold on, and we will see how the HODL strategy actually performs.

With the cryptocurrency market valued at several hundred billion dollars, it has transformed from the "currency of the dark web" in which people use Bitcoin to buy drugs and illegal services, to a financial medium that banks are considering to use for anything from faciliting cross-border payments to exchange-traded funds.  That being said, it's possible that in the future cryptocurrency investments are as commonplace as 401k's.  This solution is aimed at maximizing returns for the average investor that does not have access to the financial instruments offered to high net-worth individuals.

## Data Sources

#### Total market cap historical prices
I was unable to find a website that provided an API to pull historical market cap prices, so I had to manually download a [CSV file](https://coin.dance/stats/marketcaphistorical).  The date range used for this analysis is 1/1/2017 - 9/15/2018.


#### Coin historical prices
Coin prices were pulled by using the API for Binance in the [CCXT Python library](https://github.com/ccxt/ccxt).  


## Techniques Used in Analysis
* Data aggregation/cleansing
* Data visualization
* Data standardization
* Machine Learning algorithms
* Feature engineering
* Time series analysis


## Challenges
Most cryptocurrencies were developed in the last few years, so there is not a lot of historical data available.  Also, the cryptocurrency market has been consistently increasing with very few time frames that don't end up net positive, so our analysis will be skewed compared to analyzing stock markets that have both overperformed and underperformed over time.  To combat skewness, instead of picking a year time frame where the ending market cap is lowest compared to the starting market cap, we will take all starting and ending market cap differences, and use the time frame with the median difference as our basis for analysis.
