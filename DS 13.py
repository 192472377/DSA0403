import pandas as pd

# Load stock data from CSV file
data = pd.read_csv("indexData.csv")   # Ensure file has 'Close' column

# Extract closing prices
closing_prices = data['Close']

# Calculate statistics
mean_price = closing_prices.mean()
std_dev = closing_prices.std()
price_range = closing_prices.max() - closing_prices.min()

# Display results
print("Mean Closing Price:", mean_price)
print("Standard Deviation:", std_dev)
print("Price Range:", price_range)
