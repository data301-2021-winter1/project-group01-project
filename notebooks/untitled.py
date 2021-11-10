import pandas as pd
import numpy as np

def load_csgo(path, path2):
    #load data
    df1 = (
        pd.read_csv(path, encoding = 'latin')
        .dropna()
    )
    df2 = (
        pd.read_csv(path, encoding = 'latin')
        .dropna()
    )
    
    #process data
    df1_sort = (
        df1.loc[df1['gamename'].str.startswith("Counter-Strike: Global Offensive")]
        .drop(['gamename','peak','avg_peak_perc'], axis = 1)
        .rename(columns={"year":"Year","month":"Month","avg":"Avg_players","gain":"Gain_players"})
        .replace(['January ','February ','March ','April ','May ','June ','July ','August ','September ','October ','November ','December '],['1','2','3','4','5','6','7','8','9','10','11','12'])
    )
    df1_sort['Month'] = df1_sort['Month'].astype('int64')
    
    df2_sort = (
        df2.loc[df1['Game'].str.startswith("Counter-Strike: Global Offensive")]
.drop(['Rank','Game','Hours_watched','Hours_Streamed','Peak_channels','Streamers','Avg_channels','Avg_viewer_ratio'], axis = 1)

    )
    #merge
    df3 = ( 
        pd.merge(df1_sort, df2_sort, how = "left", on = ["Month", "Year"])
        .dropna()
        .sort_values('Year')
    )
    