#recovery vs death analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_excel('Data/Covid_19_Analytics_Dataset.xlsx')
country_data=df.groupby('country')[['confirmed_cases','recovered','deaths']].sum()
country_data=country_data.reset_index()
country_data['recovery_rate']=(country_data['recovered']/country_data['confirmed_cases'])*100
country_data['death_rate']=(country_data['deaths']/country_data['confirmed_cases'])*100
print(country_data.head())
plt.figure(figsize=(10,6))
plt.scatter(country_data['recovery_rate'],country_data['death_rate'])
plt.title('Recovery rate vs death rate')
plt.xlabel('Recovery rate %')
plt.ylabel('Death rate %')
plt.show()
