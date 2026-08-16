import numpy as np

data = np.random.random(8)

print("Original data:", data)

normalized = data * 100

print("Normalized data:", normalized)

filtered = normalized[normalized > 50]

print("Values greater than 50:", filtered)

sorted_values = np.sort(filtered)

print("Sorted values:", sorted_values)