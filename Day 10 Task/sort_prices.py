import numpy as np

# Product prices
prices = [499, 299, 799, 199, 599]

# Convert to NumPy array
price_array = np.array(prices)

# Sort prices
sorted_prices = np.sort(price_array)

print("Sorted Prices:", sorted_prices)