import pandas as pd
import numpy as np
import datetime

def load_csgo(path, path_second):
    # load data
    df1 = (
        pd.read_csv(path, encoding = 'latin')
        .dropna()
        .assign(day='1')
    )
    df2 = (
        pd.read_csv(path_second, encoding = 'latin')
        .dropna()
        .assign(day='1')
    )
    
    # process data
    # df1 sort
    df1_sort = (
        df1.loc[df1['gamename'].str.startswith("Counter-Strike: Global Offensive")]
        .drop(['gamename','peak','avg_peak_perc'], axis = 1)
        .rename(columns={"year":"Year","month":"Month","avg":"Avg_players","gain":"Gain_players"})
        
#         .replace(['January ','February ','March ','April ','May ','June ','July ','August ','September ','October ','November ','December '],['1','2','3','4','5','6','7','8','9','10','11','12'])
    )
    df1_sortdate = (
        df1_sort.assign(date = pd.to_datetime(df1_sort['Year'].astype(str) + df1_sort['Month'] + df1_sort['day'], format = '%Y%B%d'))
        .drop(['Year','Month','day'], axis = 1)
    )
#     df1_sort['Month'] = df1_sort['Month'].astype('int64')
    
    
    df2_sort = (
        df2.loc[df2['Game'].str.startswith("Counter-Strike: Global Offensive")]
.drop(['Rank','Game','Hours_watched','Hours_Streamed','Peak_channels','Streamers','Avg_channels','Avg_viewer_ratio'], axis = 1)
#         .replace(['1','2','3','4','5','6','7','8','9','10','11','12'],['January ','February ','March ','April ','May ','June ','July ','August ','September ','October ','November ','December '])

    )
    df2_sortdate = (
        df2_sort.assign(date = pd.to_datetime(df2_sort['Year'].astype(str) + df2_sort['Month'].astype(str) + df2_sort['day'], format = '%Y%m%d'))
        .drop(['Year','Month','day'], axis = 1)
    )

    # merge

    df3 = ( 
        pd.merge(df1_sortdate, df2_sortdate, how = "left", on = ['date'])
        .dropna()
#         .sort_values('Year')
    )
    df3 = df3[['date','Avg_players','Gain_players','Peak_viewers','Avg_viewers']]

    return df3
    