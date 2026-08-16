import numpy as np

# Create 2D array
temperature = np.array([
    [30, 32, 31],
    [29, 33, 34]
])

# Print array
print("Temperature Data:")
print(temperature)

# Total temperature
total = np.sum(temperature)
print("Total Temperature:", total)