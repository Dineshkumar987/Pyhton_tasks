import numpy as np

# Original list
data = [12, 7, 25, 3, 18, 10]

# Convert to NumPy array
array = np.array(data)

# Sort array
sorted_array = np.sort(array)

# Split into two equal parts
part1, part2 = np.split(sorted_array, 2)

# Sum of each part
sum1 = np.sum(part1)
sum2 = np.sum(part2)

print("Sorted Array:", sorted_array)
print("First Part:", part1)
print("Second Part:", part2)
print("Sum of First Part:", sum1)
print("Sum of Second Part:", sum2)