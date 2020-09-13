import pandas as pd
import datetime
import pandas_datareader.data as web
from pandas import Series, DataFrame
import scipy


import yfinance as yf
import numpy as np
# from datetime import datetime
from datetime import timedelta

# multiple stockes at once

def get_list_price(sym_list):
    start = datetime.datetime(2010, 1, 1)
    end = datetime.datetime(2020, 8, 21)
    # df = web.DataReader("AAPL", 'yahoo', start, end)
    df = web.DataReader(sym_list, 'yahoo', start, end)
    return df


# one stock
def get_stock_prices(sym):
    return yf.Ticker(sym).history(period='1y')

def get_list_price_1(sym_list):
    all_data = {ticker: web.get_data_yahoo(ticker) for ticker in sym_list}
    price = pd.DataFrame({ticker: data['Adj Close'] for ticker, data in all_data.items()})
    volume = pd.DataFrame({ticker: data['Volume'] for ticker, data in all_data.items()})
    return(price)

print(get_list_price(["AAPL", "FB", "AMZN"]))