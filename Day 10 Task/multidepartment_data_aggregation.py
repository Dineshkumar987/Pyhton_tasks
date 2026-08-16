import numpy as np

branch_a = np.array([
    [10, 20],
    [30, 40]
])

branch_b = np.array([
    [5, 15],
    [25, 35]
])

# Combine matrices
combined = branch_a + branch_b

# Total employees
total = np.sum(combined)

print("Combined Matrix:")
print(combined)

print("Total Employees:", total)