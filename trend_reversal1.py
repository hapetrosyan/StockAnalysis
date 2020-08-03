
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
            data.loc[data.index[i], 'swings'] = row['High'] - pivot
            pivot, last_pivot_id = row['High'], i
            up_down = 1

    # Current trend is up
    elif up_down == 1:
        # If got higher than last pivot, update the swing
        if row['High'] > pivot:
            # Remove the last pivot, as it wasn't a real one
            data.loc[data.index[i], 'swings'] = \
                data.loc[data.index[last_pivot_id], 'swings'] \
                + (row['High'] - data.loc[data.index[last_pivot_id], 'High'])
            data.loc[data.index[last_pivot_id], 'swings'] = np.nan
            pivot, last_pivot_id = row['High'], i
        elif row['Low'] < pivot - diff:
            data.loc[data.index[i], 'swings'] = row['Low'] - pivot
            pivot, last_pivot_id = row['Low'], i
            # Change the trend indicator
            up_down = -1


    # Current trend is down
    elif up_down == -1:
        # If got higher than last pivot, update the swing
        if row['Low'] < pivot:
            # Remove the last pivot, as it wasn't a real one
            data.loc[data.index[i], 'swings'] = \
                data.loc[data.index[last_pivot_id], 'swings'] \
                + (row['Low'] - data.loc[data.index[last_pivot_id], 'Low'])
            data.loc[data.index[last_pivot_id], 'swings'] = np.nan
            pivot, last_pivot_id = row['Low'], i
        elif row['High'] > pivot - diff:
            data.loc[data.index[i], 'swings'] = row['High'] - pivot
            pivot, last_pivot_id = row['High'], i
            # Change the trend indicator
            up_down = 1

print (data)
