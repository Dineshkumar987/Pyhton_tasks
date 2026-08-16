import numpy as np

data = np.array([5, 10, 15, 20, 25, 30])

# Split into 3 equal parts
split_data = np.split(data, 3)

print("Split Arrays:")
for part in split_data:
    print(part)