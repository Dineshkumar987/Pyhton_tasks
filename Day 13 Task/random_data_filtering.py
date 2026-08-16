import numpy as np

nums = np.random.randint(1, 100, 10)

filtered = nums[nums % 5 == 0]

sorted_result = np.sort(filtered)

print("Random numbers:", nums)
print("Values divisible by 5:", filtered)
print("Sorted result:", sorted_result)