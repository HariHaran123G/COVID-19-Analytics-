#Recovery rate analysis
import pandas as pd
import numpy as np
import matplotlib as plt

df=pd.read_excel('Data/Covid_19_Analytics_Dataset.xlsx')
df['revovery_rate']=np.where(df['confirmed_cases']>0,(df['recovered']/df['confirmed_cases'])*100,0)
country_recovery=df.groupby('country')['recovery_rate'].mean()
country_recovery=country_recovery.reset_index()
top_recovery=country_recovery.sort_values(by='recovery_rate',ascending=false)

#top 10 countries
plt.barh(top10['country'], top10['recovery_rate'])
plt.title('Top 10 Countries by recovery rate')
plt.xlabel('Recovery rate%')
plt.ylabel('Country')
plt.show()

