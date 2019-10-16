
import sys
import data_ops
import stocksymbol as s
import matplotlib.pyplot as plt
do = data_ops.DataOps()

# amzn = s.StockSymbol('AMZN')
# fb = s.StockSymbol('FB')

all_symbols = do.get_symbols_list()

all_symbols_info = {}

for symbol in all_symbols:
    if symbol['price'] > 100:
        all_symbols_info[symbol['symbol']] = s.StockSymbol(symbol['symbol'])


print(
    all_symbols_info
)