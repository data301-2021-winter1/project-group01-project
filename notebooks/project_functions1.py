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
    #         df1
        .convert_dtypes()
        .assign(day='1')
    )
    df3 = (
        df2.assign(date = pd.to_datetime(df2['year'].astype(str)  + df2['month'] + df2['day'], format='%Y%B%d').dt.date)
        .drop(['year', 'month', 'day', 'peak', 'avg_peak_perc', 'gamename'], axis = 1)
        .sort_values('date')
        .assign(rolling_gain = df2['gain'].rolling(7, center=True).mean())
        .dropna()
        .assign(release_Dates='')
    )
    print(df3.dtypes)

    for x, y in my_dict.items():
        for z in y:
            df3.loc[df3['date'] == pd.to_datetime(z, format='%Y%m%d'), 'release_Dates'] += (x+"/")

    df3 = df3[['date', 'avg', 'gain', 'rolling_gain', 'release_Dates']]
    return df3