prices = [100, 200, 300, 400]

updated_prices = [
    price * 0.9 if price > 200 else price
    for price in prices
]

print("Updated prices:", updated_prices)