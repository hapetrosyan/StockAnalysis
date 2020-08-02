
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ba_1y = yf.Ticker('BA').history(period='1y')
data = pd.read_csv('DataFiles/ba_1y.csv', index_col='Date', \
     usecols=['Date', 'Open', 'High', 'Low', 'Close'])
# data = ba_1y[['Open', 'High', 'Low', 'Close']]
data.loc[:, 'swings'] = np.nan
pivot = data.iloc[0, 0]
last_pivot_id = 0
up_down = 0
diff = .3

# print(data[:10])

for i in range(0, len(data)):
    row = data.iloc[i]

    print(row)

    # We don't have a trend yet
    if up_down == 0:
        if row['Low'] < pivot - diff:
            data.loc[data.index[i], 'swings'] = row['Low'] - pivot
            pivot, last_pivot_id = row['Low'], i
            up_down = -1
        elif row['High'] > pivot + diff:
            data.iloc[i]['swings'] = row['High'] - pivot
            pivot, last_pivot_id = row['High'], i
            up_down = 1
    print(row)
    print(data)
            
'''
    # Current trend is up
    elif up_down == 1:
        # If got higher than last pivot, update the swing
        if row.high > pivot:
            # Remove the last pivot, as it wasn't a real one
            data.ix[i, 'swings'] = data.ix[last_pivot_id, 'swings'] \
                + (row.high - data.ix[last_pivot_id, 'high'])
            data.ix[last_pivot_id, 'swings'] = np.nan
            pivot, last_pivot_id = row.high, i
        elif row.low < pivot - diff:
            data.ix[i, 'swings'] = row.low - pivot
            pivot, last_pivot_id = row.low, i
            # Change the trend indicator
            up_down = -1

    # Current trend is down
    elif up_down == -1:
            # If got lower than last pivot, update the swing
        if row.low < pivot:
            # Remove the last pivot, as it wasn't a real one
            data.ix[i, 'swings'] = data.ix[last_pivot_id, 'swings'] \
                + (row.low - data.ix[last_pivot_id, 'low'])
            data.ix[last_pivot_id, 'swings'] = np.nan
            pivot, last_pivot_id = row.low, i
        elif row.high > pivot - diff:
            data.ix[i, 'swings'] = row.high - pivot
            pivot, last_pivot_id = row.high, i
            # Change the trend indicator
            up_down = 1

print data
'''