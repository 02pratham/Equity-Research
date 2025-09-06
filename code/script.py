import pandas as pd
import requests

# Download the stock price history data
csv_url = "https://perplexity.ai/rest/finance/history/RELIANCE.NS/csv?start_date=2023-01-01&end_date=2025-09-01"
response = requests.get(csv_url)
price_data = pd.read_csv(pd.io.common.StringIO(response.text))

# Display basic info about the data
print("Stock Price Data Shape:", price_data.shape)
print("\nColumns:", price_data.columns.tolist())
print("\nFirst few rows:")
print(price_data.head())
print("\nLast few rows:")
print(price_data.tail())
print("\nData Types:")
print(price_data.dtypes)

# Convert date column to datetime
price_data['date'] = pd.to_datetime(price_data['date'])
print("\nDate range:", price_data['date'].min(), "to", price_data['date'].max())

# Calculate basic statistics
print("\nPrice Statistics:")
print(f"Current Price (latest close): ₹{price_data['close'].iloc[-1]:.2f}")
print(f"52-week high: ₹{price_data['high'].max():.2f}")
print(f"52-week low: ₹{price_data['low'].min():.2f}")
print(f"Average close price: ₹{price_data['close'].mean():.2f}")
print(f"Average daily volume: {price_data['volume'].mean():,.0f}")