import pandas as pd

# Load your CSV file
df = pd.read_csv('cumul_ohlc.csv')

df['close'] = pd.to_numeric(df['close'], errors='coerce')

# Bollinger Band parameters
bb_length = 20
bb_sd_mult = 2

df['BB MID'] = df['close'].rolling(window=bb_length).mean()
df['SD'] = df['close'].rolling(window=bb_length).std()

# Construct Bollinger Bands
# Calculate upper and lower bands
df['BB UP Band'] = df['BB MID'] + bb_sd_mult * df['SD']
df['BB DOWN Band'] = df['BB MID'] - bb_sd_mult * df['SD']

# Optional: Save to a new CSV file
df.to_csv('bollinger_bands_from_avg.csv', index=False)

print(df[['DateTime', 'close', 'BB MID', 'BB UP Band', 'BB DOWN Band']])


import matplotlib.pyplot as plt

plot_df = df

plt.figure(figsize=(14, 6))
plt.plot(plot_df['close'], label='Avg Price', color='blue')
plt.plot(plot_df['BB MID'], label='BB MID', color='black', linestyle='--')
plt.plot(plot_df['BB UP Band'], label='Upper Band', color='green')
plt.plot(plot_df['BB DOWN Band'], label='Lower Band', color='red')
plt.fill_between(plot_df.index, plot_df['BB DOWN Band'], plot_df['BB UP Band'], color='gray', alpha=0.2)

plt.title('Bollinger Bands (20-period, 2×SD) on Avg(Close)')
plt.xlabel('Index')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
