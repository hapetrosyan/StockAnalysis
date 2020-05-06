import pandas as pd
import numpy as np
import datetime as dt
import math
import warnings

warnings.filterwarnings("ignore")

prices = pd.read_csv('prices.csv', index_col='Date', parse_dates=True)
volumechanges = pd.read_csv('volume.csv', index_col='Date', parse_dates=True).pct_change()*100

today = dt.date(2000, 1, 15)
simend = dt.date(2020, 5, 5)
tickers = []
transactionid = 0
money = 1000000
portfolio = {}
activelog = []
transactionlog = []

def getprice(date, ticker):
    global prices
    return prices.loc[date][ticker]