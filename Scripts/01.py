#Highest-cases
#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df=pd.read_excel('Data/Covid_19_Analytics_Dataset.xlsx')

print(df.head())
print(df.columns)
country_cases=df.groupby('country')['confirmed_cases'].sum()
country_cases=country_cases.reset_index()
highest=country_cases.sort_values(by='confirmed_cases',ascending=False)
print(highest.head(10))

#matplotlib
top10=highest.head(10)
plt.bar(top10['country'],top10['confirmed_cases'])
plt.title('Top 10 countries confirmed covid cases')
plt.xlabel('country')
plt.ylabel('confirmed_cases')
plt.xticks(rotation=45)
plt.show()

