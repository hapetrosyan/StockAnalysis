import pandas as pd
import misc_ops as mo
import data_ops


class StockSymbol:
    def __init__(self, symbol, df='', period_start='', period_end=''):
        do = data_ops.DataOps()
        self.symbol = symbol

        self.alphavantage_100_days_dict = do.get_alphavantage_100_days_dict(self.symbol)
        self.alphavantage_intraday_5_min_dict = do.get_alphavantage_intraday_5_min_dict(self.symbol)
        # self.alphavantage_intraday_1_min_dict = do.get_alphavantage_intraday_1_min_dict(self.symbol)
        # self.alphavantage_1_week_dict = do.get_alphavantage_1_week_dict(self.symbol)
        # self.company_profile_dict = do.get_company_profile_dict(self.symbol)
        # self.company_annual_income_dict = do.get_company_annual_income_dict(self.symbol)
        # self.company_quarterly_income_dict = do.get_company_quarterly_income_dict(self.symbol)

        self.alphavantage_intraday_5_min_df = self.__get_alphavantage_df_from_dict(self.alphavantage_intraday_5_min_dict)
        # self.alphavantage_intraday_1_min_df = self.__get_alphavantage_df_from_dict(self.alphavantage_intraday_1_min_dict)
        self.alphavantage_100_days_df = self.__get_alphavantage_df_from_dict(self.alphavantage_100_days_dict)
        # self.alphavantage_1_week_df = self.__get_alphavantage_df_from_dict(self.alphavantage_1_week_dict)

        # self.ccp_sum_20_100 = self.get_last_n_ccp_sum(n = 20, period = '100_days')
        # self.ccp_sum_10_100 = self.get_last_n_ccp_sum(n = 10, period = '100_days')
        # self.ccp_sum_100_1_min = self.get_last_n_ccp_sum(n=100, period='1_min')
        # self.ccp_sum_50_1_min = self.get_last_n_ccp_sum(n=50, period='1_min')
        # self.ccp_sum_20_1_min = self.get_last_n_ccp_sum(n=20, period='1_min')
        # self.ccp_sum_10_1_min = self.get_last_n_ccp_sum(n=10, period='1_min')
        # self.ccp_sum_5_1_min = self.get_last_n_ccp_sum(n=5, period='1_min')
        # self.price_difference = self.__get_premarket_price_difference()

        '''
        # self.hist_price_df = df
        # self.period_start = period_start
        # self.period_end = period_end
        # self.symbol_hist_price_df = df[df['Symbol'] == symbol][['Date', 'Price']].sort_values(by=['Date'])
        # self.symbol_series_1w = pd.Series([])
        # self.symbol_rolling_sum_1w = 0
        # self.period_start_1w = mo.MiscOps.add_days_to_string_date(self.period_end, -7)
        # self.symbol_series_1m = pd.Series([])
        # self.symbol_rolling_sum_1m = 0
        # self.period_start_1m = mo.MiscOps.add_days_to_string_date(self.period_end, -30)
        # """ calculating rolling sum for the last 1 week """
        # if ((mo.MiscOps.get_date_from_string(period_end) - mo.MiscOps.get_date_from_string(period_start)).days >= 7):
        #     self.symbol_series_1w = self.get_symbol_series(self.hist_price_df, self.symbol, self.period_start_1w, self.period_end)
        #     self.symbol_rolling_sum_1w = self.get_symbol_rolling_sum(self.symbol_series_1w)
        # """ calculating rolling sum for the last 1 month """
        # if ((mo.MiscOps.get_date_from_string(period_end) - mo.MiscOps.get_date_from_string(period_start)).days >= 30):
        #     self.symbol_series_1m = self.get_symbol_series(self.hist_price_df, self.symbol, self.period_start_1m, self.period_end)
        #     self.symbol_rolling_sum_1m = self.get_symbol_rolling_sum(self.symbol_series_1m)
        # self.symbol_series = self.get_symbol_series(self.hist_price_df, self.symbol, self.period_start, self.period_end)
        # self.symbol_rolling_sum = self.get_symbol_rolling_sum(self.symbol_series)
        '''

    @staticmethod
    def get_symbol_series(df, symbol, period_start, period_end):
        symbol_series = df[df.Symbol == symbol] \
            [df.Date >= period_start] \
            [df.Date <= period_end] \
            [['Date', 'Price']]

        return symbol_series

    @staticmethod
    def get_symbol_rolling_sum(symbol_series):
        ts = pd.Series(symbol_series['Price'].values, index=symbol_series['Date'])
        ts.sort_index(inplace=True)
        pc = ts.pct_change(1)
        return (pc.sum())

    @staticmethod
    def __get_alphavantage_df_from_dict(alphavantage_dict):
        alphavantage_df = pd.DataFrame(columns=['datetime', 'open', 'high', 'low', 'close', 'ccp', 'volume'])
        i = 0
        prev_close = 0
        for k, v in alphavantage_dict.items():
            ccp = 0
            if i > 0 and prev_close != 0:
                ccp = (v['close'] - prev_close) / prev_close
            else:
                ccp = 0
            alphavantage_df = alphavantage_df.append(
                {'datetime': k, 'open': v['open'], 'high': v['high'], 'low': v['low'], 'close': v['close'], 'ccp': ccp,
                 'volume': v['volume']}, ignore_index=True)
            prev_close = v['close']
            i = i + 1
        return alphavantage_df

    def get_last_n_ccp_sum(self, period='1_min', n=20):
        if period == '1_min':
            df = self.alphavantage_intraday_1_min_df
        elif period == '5_min':
            df = self.alphavantage_intraday_5_min_df
        elif period == '100_days':
            df = self.alphavantage_100_days_df
        elif period == '1_week':
            df = self.alphavantage_1_week_df
        else:
            return 0
            exit()
        return sum(df['ccp'][-n:])

    '''
    replace current df with premarket dataframe
    get better logic for price difference
    '''
    def __get_premarket_price_difference(self):
        return (self.alphavantage_intraday_1_min_df.close.max() - self.alphavantage_intraday_1_min_df.close.min()) / self.alphavantage_intraday_1_min_df.close.max()
