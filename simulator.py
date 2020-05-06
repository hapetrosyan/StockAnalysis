import pandas_datareader as web


stocks = []
f = open('symbols.txt', 'r')
for line in f:
    stocks.append(line.strip())


f.close()

print(stocks)