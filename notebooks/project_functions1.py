import pandas as pd
import numpy as np
import datetime

def load_process_csgo(path):
    #load data
    df1 = (
        pd.read_csv(path, encoding='latin')
        .dropna()
    )
    #process data
    df2 = (
        df1.loc[df1['gamename'].str.startswith("Counter-Strike: Global Offensive")]
    #         df1
        .convert_dtypes()
        .assign(day='1')
    )
    df3 = (
        df2.assign(date = pd.to_datetime(df2['year'].astype(str)  + df2['month'] + df2['day'], format='%Y%B%d'))
        .drop(['year', 'month', 'day', 'peak', 'avg_peak_perc', 'gamename'], axis = 1)
        .sort_values('date')
        .assign(rolling_gain = df2['gain'].rolling(7, center=True).mean())
        .dropna()
    )
    df3 = df3[['date', 'avg', 'gain', 'rolling_gain']]
    return df3