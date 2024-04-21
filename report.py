import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV files
nvda_df = pd.read_csv('NVDA.csv')
intc_df = pd.read_csv('INTC.csv')

# Convert 'Date' column to datetime format
nvda_df['Date'] = pd.to_datetime(nvda_df['Date'], format='%m/%d/%Y')
intc_df['Date'] = pd.to_datetime(intc_df['Date'], format='%m/%d/%Y')

# Set 'Date' column as index
nvda_df.set_index('Date', inplace=True)
intc_df.set_index('Date', inplace=True)

# Plot adjusted closing prices over time
plt.figure(figsize=(12, 6))
plt.plot(nvda_df.index, nvda_df['NVDA Adj Close'], label='NVDA')
plt.plot(intc_df.index, intc_df['INTC Adj Close'], label='INTC')
plt.xlabel('Date')
plt.ylabel('Adjusted Closing Price')
plt.title('Adjusted Closing Prices Over Time')
plt.legend()
plt.show()

# Plot trading volume over time
plt.figure(figsize=(12, 6))
plt.plot(nvda_df.index, nvda_df['NVDA Volume'], label='NVDA')
plt.plot(intc_df.index, intc_df['INTC Volume'], label='INTC')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.title('Volume Traded Over Time')
plt.legend()
plt.show()

# Calculate correlation between NVDA and INTC
correlation = nvda_df['NVDA Adj Close'].corr(intc_df['INTC Adj Close'])
print("Correlation between NVDA and INTC:", correlation)

# Plot correlation heatmap
sns.heatmap(nvda_df.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()
