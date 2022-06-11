import pandas_datareader as web


stocks = []
f = open('symbols.txt', 'r')
for line in f:
    stocks.append(line.strip())


f.close()

web.DataReader(stocks, 'yahoo', start='2000-1-1', end='2020-05-05')\
    ['Adj Close'].to_csv('prices.csv')
web.DataReader(stocks, 'yahoo', start='2000-1-1', end='2020-05-05')\
    ['Volume'].to_csv('volume.csv')