#recovery vs death analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_excel('Data/Covid_19_Analytics_Dataset.xlsx')
country_data=df.groupby('country')['confirmed_cases','recovered','deaths'].sum()
