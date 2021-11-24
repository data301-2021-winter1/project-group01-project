import pandas as pd
import numpy as np
# import datetime

def load_process_csgo(path, my_dict):
    #load data
    df1 = (
        pd.read_csv(path, encoding='latin')
        .dropna()
    )
    #process data
    df2 = (
        df1.loc[df1['gamename'].str.startswith("Counter-Strike: Global Offensive")]
        .convert_dtypes()
        .assign(day='1')
    )
    df3 = (
        df2.assign(date = pd.to_datetime(df2['year'].astype(str)  + df2['month'] + df2['day'], format='%Y%B%d').dt.date)
        .drop(['year', 'month', 'day', 'peak', 'avg_peak_perc', 'gamename'], axis = 1)
        .sort_values('date', ignore_index = True)
        
    )
    df4 = (
        df3.assign(rolling_avg = df3['avg'].rolling(7, center=True).mean())
        .assign(rolling_gain = df3['gain'].rolling(4).mean())
        .dropna()
        .assign(release_Dates='No Releases')
        .reset_index()
    )
    #load in markers
    for x, y in my_dict.items():
        for z in y:
            df4.loc[df4['date'] == pd.to_datetime(z, format='%Y%m%d'), 'release_Dates'] = (x)

    df4 = df4[['date', 'avg', 'rolling_avg', 'gain', 'rolling_gain', 'release_Dates']]
    return df4