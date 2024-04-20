import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Read
df_INTC=pd.read_csv('INTC.csv')  
print("INTC:\n",df_INTC,type(df_INTC))       
df_NVDA=pd.read_csv('NVDA.csv')
print("NVDA:\n",df_NVDA,type(df_NVDA))
#convert date to datetime
df_INTC['Date']=pd.to_datetime(df_INTC['Date'])
df_NVDA['Date']=pd.to_datetime(df_NVDA['Date'])
# missing data
df_INTC['Adj Close'].fillna(method='ffill', inplace=True) 
df_NVDA['Adj Close'].fillna(method='ffill', inplace=True)

# Calculating basic statistics 
print(df_INTC.describe())
print(df_NVDA.describe())

#trends of INTC Date and Closing price
plt.figure(figsize=(10,6))
plt.plot(df_INTC['Date'],df_INTC['Adj Close'],label='INTC')
plt.title('Adj Closing Price Over Time-INTC')
plt.xlabel('Date')
plt.ylabel('Adj Close')
plt.legend()
plt.show()
# Trends of INTC Date and volume
plt.figure(figsize=(10,6))
plt.plot(df_INTC['Date'],df_INTC['Volume'],label='INTC')
plt.title('Volume Over Time-INTC')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.legend()
plt.show()

# #  Trends for NVDA Date and closing price
# plt.figure(figsize=(10,6))
# plt.plot(df_NVDA['Date'],df_NVDA['Adj Close'],label='NVDA')
# plt.title('Adj Closing Price Over Time-NVDA')
# plt.xlabel('Date')
# plt.ylabel('Adj Close')
# plt.legend()
# plt.show()
# # Trends for NVDA Date and volume
# plt.figure(figsize=(10,6))
# plt.plot(df_NVDA['Date'],df_NVDA['Volume'],label='NVDA')
# plt.title('Volume Over Time-NVDA')
# plt.xlabel('Date')
# plt.ylabel('Volume')
# plt.legend()
# plt.show()

# Merge
merged_1=pd.merge(df_INTC, df_NVDA,on='Date')
print("merged on date:\n",merged_1)
df=merged_1

# Extract columes
print("df.columns:\n",df_INTC.columns)
print("df.columns:\n",df_NVDA.columns)

# # Create new columns to calculate total volume traded and average adjusted closing price
df['Total Volume'] = df(Index['Volume']+Index['Volume'])
# df['Avg Adj Close'] = (df['Adj Close_NVDA'] + df['Adj Close_INTC']) / 2

