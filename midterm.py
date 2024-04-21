import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

# Task 1: Data Loading and Cleaning
# Read CSV files into separate pandas DataFrames
nvda_df = pd.read_csv('NVDA.csv')
intc_df = pd.read_csv('INTC.csv')

# Handle missing values and duplicates
nvda_df.dropna(inplace=True)
nvda_df.drop_duplicates(inplace=True)
intc_df.dropna(inplace=True)
intc_df.drop_duplicates(inplace=True)

# Convert 'Date' column to datetime format
nvda_df['Date'] = pd.to_datetime(nvda_df['Date'], format='%m/%d/%Y')
intc_df['Date'] = pd.to_datetime(intc_df['Date'], format='%m/%d/%Y')

# Set 'Date' column as index
nvda_df.set_index('Date', inplace=True)
intc_df.set_index('Date', inplace=True)

# Task 2: Exploratory Data Analysis (EDA)
# Visualize trend of adjusted closing prices and volume
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(nvda_df.index, nvda_df['NVDA Adj Close'], label='NVDA')
plt.plot(intc_df.index, intc_df['INTC Adj Close'], label='INTC')
plt.xlabel('Date')
plt.ylabel('Adjusted Closing Price')
plt.title('Adjusted Closing Prices Over Time')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(nvda_df.index, nvda_df['NVDA Volume'], label='NVDA')
plt.plot(intc_df.index, intc_df['INTC Volume'], label='INTC')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.title('Volume Traded Over Time')
plt.legend()

# Format date ticks as 'year-month-day'
plt.gca().xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))

plt.tight_layout()
plt.show()

# Task 3: Data Manipulation and Aggregation
# Merge DataFrames on 'Date' column
merged_df = pd.merge(nvda_df, intc_df, left_index=True, right_index=True, suffixes=('_NVDA', '_INTC'))

# Create new columns for total volume traded and average adjusted closing price
merged_df['Total Volume'] = merged_df['NVDA Volume'] + merged_df['INTC Volume']
merged_df['Avg Adj Close'] = (merged_df['NVDA Adj Close'] + merged_df['INTC Adj Close']) / 2

# Aggregate data to calculate monthly average adjusted closing prices and total volume traded
monthly_data = merged_df.resample('M').agg({'Avg Adj Close': 'mean', 'Total Volume': 'sum'})

# Task 4: Advanced Analysis with Numpy and Pandas
# Compute correlation matrix between adjusted closing prices
correlation_matrix = merged_df[['NVDA Adj Close', 'INTC Adj Close']].corr()

# Calculate rolling statistics
merged_df['NVDA Adj Close Rolling Mean'] = merged_df['NVDA Adj Close'].rolling(window=5).mean()
merged_df['NVDA Adj Close Rolling Std'] = merged_df['NVDA Adj Close'].rolling(window=5).std()

# Print results
print("NVDA Basic Statistics:")
print(nvda_df.describe())
print("\nINTC Basic Statistics:")
print(intc_df.describe())
print("\nCorrelation Matrix:")
print(correlation_matrix)
print("\nMonthly Aggregated Data:")
print(monthly_data)

# Extra Features
# Extra Task 1: Calculate returns over time for each company and visualize them in a chart
nvda_df['NVDA Returns'] = nvda_df['NVDA Adj Close'].pct_change()
intc_df['INTC Returns'] = intc_df['INTC Adj Close'].pct_change()

plt.figure(figsize=(10, 5))
plt.plot(nvda_df.index, nvda_df['NVDA Returns'], label='NVDA Returns')
plt.plot(intc_df.index, intc_df['INTC Returns'], label='INTC Returns')
plt.xlabel('Date')
plt.ylabel('Returns')
plt.title('Returns Over Time')
plt.legend()
plt.show()

# Extra Task 2: Identify and print top 5 dates with highest trading volume
top_volume_dates = merged_df.nlargest(5, 'Total Volume').index
print("Top 5 Dates with Highest Trading Volume:")
print(top_volume_dates)

# Extra Task 3: Volatility Analysis
# Calculate standard deviation of returns
nvda_volatility = nvda_df['NVDA Returns'].std()
intc_volatility = intc_df['INTC Returns'].std()

print("Volatility (Standard Deviation of Returns):")
print("NVDA Volatility:", nvda_volatility)
print("INTC Volatility:", intc_volatility)