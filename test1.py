
import sys
import data_ops
import stocksymbol as s
import matplotlib.pyplot as plt


amzn = s.StockSymbol('AMZN')
# df_5_min = amzn.alphavantage_intraday_5_min_df
df_1_min = amzn.alphavantage_intraday_1_min_df

# pd = amzn.price_difference

print(df_1_min[[
     'datetime'
    ,'open'
    ,'high'
    ,'low'
    ,'close'
    ,'volume'
    ,'ccp'
]])