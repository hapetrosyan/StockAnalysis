
import sys
import data_ops
import stocksymbol as s

# amzn = s.StockSymbol('AMZN')

do = data_ops.DataOps()

print(do.get_nasdaq_symbols_list())