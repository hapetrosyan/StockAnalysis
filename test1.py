
import sys
import data_ops
import stocksymbol as s

amzn = s.StockSymbol('AMZN')
df_5_min = amzn.alphavantage_intraday_5_min_df
# pd = amzn.price_difference

print(df_5_min[[
     'datetime'
    ,'open'
    ,'high'
    ,'low'
    ,'close'
    ,'volume'
    ,'ccp'
]])