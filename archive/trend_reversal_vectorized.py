
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ba_1y = yf.Ticker('BA').history(period='1y')
# amzn_1y = yf.Ticker('AMZN').history(period='1y')
# amzn_1y.to_csv('DataFiles/amzn_1y.csv')

data = pd.read_csv('../DataFiles/amzn_1y.csv', index_col='Date', \
     usecols=['Date', 'Open', 'High', 'Low', 'Close'])

print(data)


