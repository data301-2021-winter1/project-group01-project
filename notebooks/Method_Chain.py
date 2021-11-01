import pandas as pd
import numpy as np


def load_process_covid(path):
    #load data
    rawDF = (
        pd.read_csv(path, encoding='latin')
        .dropna()
    )
    
    #process data/wrangling
    df_covid = (
        rawDF.drop(['peak', 'avg_peak_perc', 'gamename','avg'], axis = 1)
        .convert_dtypes()
        .sort_values('year')
        .dropna()
    )
    
    df_year = df_covid.loc[df_covid['year'] == 2019]
    df_year = df_year.loc [df_year['month'] == 'January ']     
    gainJan2019 = df_year['gain'].mean()

    df_year = df_covid.loc[df_covid['year'] == 2019]
    df_year = df_year.loc [df_year['month'] == 'February ']     
    gainFeb2019 = df_year['gain'].mean()

    df_year = df_covid.loc[df_covid['year'] == 2019]
    df_year = df_year.loc [df_year['month'] == 'March ']     
    gainMar2019 = df_year['gain'].mean()

    df_year = df_covid.loc[df_covid['year'] == 2020]
    df_year = df_year.loc [df_year['month'] == 'January ']     
    gainJan2020 = df_year['gain'].mean()

    df_year = df_covid.loc[df_covid['year'] == 2020]
    df_year = df_year.loc [df_year['month'] == 'February ']     
    gainFeb2020 = df_year['gain'].mean()

    df_year = df_covid.loc[df_covid['year'] == 2020]
    df_year = df_year.loc [df_year['month'] == 'March ']     
    gainMar2020 = df_year['gain'].mean()


    data = {'Month': ['January', 'February', 'March', 'January', 'February', 'March'], 'Year': [2019,2019,2019,2020,2020,2020], 'AvgGainPerGame': [gainJan2019, gainFeb2019, gainMar2019, gainJan2020, gainFeb2020, gainMar2020 ]}  

    df_covid_final = pd.DataFrame(data)
        
   
    return df_covid_final