#daily trend analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_excel('Data/Covid_19_Analytics_Dataset.xlsx')
daily_cases=df.groupby('date')['confirmed_cases'].sum()  
daily_cases=daily_cases.reset_index()
print(daily_cases.head())

#charts
plt.figure(figsize=(12,6))
plt.plot(daily_cases['date'],daily_cases['confirmed_cases'])
plt.title('Daily COVID confirmed cases trend')
plt.xlabel('Date')
plt.ylabel('confirmed_cases')
plt.xticks(rotation=45)
plt.show()
