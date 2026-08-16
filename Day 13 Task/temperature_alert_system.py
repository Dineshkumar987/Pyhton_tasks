import numpy as np

temps = np.array([28, 32, 35, 31, 29, 40, 38])

hot_days = temps > 30

indices = np.where(hot_days)[0]

print("Temperatures above 30:", temps[hot_days])
print("Indices:", indices)