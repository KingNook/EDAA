import pandas as pd
import numpy as np

import datetime as dt
from dateutil.relativedelta import relativedelta

def parse_dt(date_string):

    date = dt.datetime.strptime(date_string, r'%m-%d %H:%M')
    date = date + relativedelta(year = 2025)

    return date

decay_times_path = './data/decay_times.txt'
data_path = './data/october_RAW.csv'

## parsing timestamps
timestamps = open(decay_times_path).read().split('\n')
timestamps = [i.split(', ') for i in timestamps]
timestamps = [[parse_dt(date) for date in timestamp] for timestamp in timestamps]

## reading data
data = pd.read_csv(data_path, parse_dates=['UTC Date/Time'])
data['UTC Date/Time'] = data['UTC Date/Time'].dt.tz_localize(None)
data['UTC Date/Time'] = data['UTC Date/Time'].dt.round(freq='min')

## 
decay_data = [
    data[(data['UTC Date/Time'] > ts[0]) & (data['UTC Date/Time'] < ts[1])] for ts in timestamps
]

