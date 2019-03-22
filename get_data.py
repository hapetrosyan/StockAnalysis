
import pandas as pd
import numpy as np
import datetime
from pandas import ExcelWriter
from pandas import ExcelFile
import shutil
import os
from os import walk
import requests
import json

import misc_ops



class DataOps:
    @staticmethod
    def get_alphavantage_100_days_dict(symbol):
        mo = misc_ops.MiscOps()
        request_link = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+symbol+'&apikey=K2L959U20SZIKBDG'
        resp = requests.get(request_link)

        if resp.status_code != 200:
            # This means something went wrong.
            raise ApiError('GET /tasks/ {}'.format(resp.status_code))
        resp_json = resp.json() # ['Time Series (Daily)']
        # for todo_item in resp.json():
            # print('{} {}'.format(todo_item['id'], todo_item['login']))
            # print(todo_item)

        # resp_metadata = resp_json['Meta Data']
        try:
            resp_time_series = resp_json['Time Series (Daily)']
        except:
            resp_time_series = {}
        with open('result_'+symbol+'.json', 'w') as fp:
            json.dump(resp_json, fp)
        return(mo.format_alphavantage_dict(resp_time_series))

    @staticmethod
    def get_alphavantage_intraday_5_min_dict(symbol):
        mo = misc_ops.MiscOps()
        request_link = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='+symbol+'&interval=5min&apikey=K2L959U20SZIKBDG'
        resp = requests.get(request_link)

        if resp.status_code != 200:
            # This means something went wrong.
            raise ApiError('GET /tasks/ {}'.format(resp.status_code))
        resp_json = resp.json() # ['Time Series (Daily)']
        # for todo_item in resp.json():
            # print('{} {}'.format(todo_item['id'], todo_item['login']))
            # print(todo_item)

        # resp_metadata = resp_json['Meta Data']
        try:
            resp_time_series = resp_json['Time Series (5min)']
        except:
            resp_time_series = {}
        return(mo.format_alphavantage_dict(resp_time_series))


    @staticmethod
    def get_alphavantage_intraday_1_min_dict(symbol):
        mo = misc_ops.MiscOps()
        request_link = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='+symbol+'&interval=1min&apikey=K2L959U20SZIKBDG'
        resp = requests.get(request_link)

        if resp.status_code != 200:
            # This means something went wrong.
            raise ApiError('GET /tasks/ {}'.format(resp.status_code))
        resp_json = resp.json() # ['Time Series (Daily)']
        # for todo_item in resp.json():
            # print('{} {}'.format(todo_item['id'], todo_item['login']))
            # print(todo_item)

        # resp_metadata = resp_json['Meta Data']
        try:
            resp_time_series = resp_json['Time Series (1min)']
        except:
            resp_time_series = {}
        return(mo.format_alphavantage_dict(resp_time_series))

    @staticmethod
    def get_alphavantage_1_week_dict(symbol):
        mo = misc_ops.MiscOps()
        request_link = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol='+symbol+'&apikey=K2L959U20SZIKBDG'
        resp = requests.get(request_link)

        if resp.status_code != 200:
            # This means something went wrong.
            raise ApiError('GET /tasks/ {}'.format(resp.status_code))
        resp_json = resp.json() # ['Time Series (Daily)']
        # for todo_item in resp.json():
            # print('{} {}'.format(todo_item['id'], todo_item['login']))
            # print(todo_item)

        # resp_metadata = resp_json['Meta Data']
        try:
            resp_time_series = resp_json['Weekly Time Series']
        except:
            resp_time_series = {}
        return(mo.format_alphavantage_dict(resp_time_series))


    @staticmethod
    def get_all_symbols_list(df):
        return df['Symbol'].unique()