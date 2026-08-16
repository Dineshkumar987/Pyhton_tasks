import numpy as np

arr = np.array([10, 20, 30, 40])

copy_arr = arr.copy()

arr[0] = 100

print("Original:", arr)
print("Copy:", copy_arr)