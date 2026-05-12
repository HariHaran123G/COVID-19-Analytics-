#fatality rate analysis
import pandas as pd
import numpy as ny
import matplotlib as plt

df=pd.read_excel('Data/Covid_19_Analytics_Dataset.xlsx')
country_data=df.groupby('country').['deaths','confirmed_cases'].sum()
country_data=country_data.reset_index()
