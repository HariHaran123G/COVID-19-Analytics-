#fatality rate analysis
import pandas as pd
import numpy as ny
import matplotlib as plt

df=pd.read_excel('Data/Covid_19_Analytics_Dataset.xlsx')
country_data=df.groupby('country').[['deaths','confirmed_cases']].sum()
country_data=country_data.reset_index()
country_data['fatality_rate']=(country_data['deaths']/country_data['confirmed_cases'])*100
highest_fatality=country_data.sort_values(by='fatality_rate',ascending=false)
top10=highest_fatality.head(10)
print(top10)

#chart
plt.figure(figsize=(12,6))
plt.bar(top10['country'],top10['fatality_rate'])
plt.title('Top 10 countries COVID Fatality rate')
plt.xlabel('Country')
plt.ylabel('Fatality rate(%)')
plt.xticks(rotation=45)
plt.show()
