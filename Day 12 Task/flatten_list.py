data = [[1, 2, 3], [4, 5], [6]]

flattened = [num for sublist in data for num in sublist]

print("Flattened:", flattened)