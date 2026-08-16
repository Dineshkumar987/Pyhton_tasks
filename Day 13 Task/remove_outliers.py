import numpy as np

values = np.array([10, 12, 15, 18, 100, 14, 13])

mean = np.mean(values)
standard_deviation = np.std(values)

lower_limit = mean - 2 * standard_deviation
upper_limit = mean + 2 * standard_deviation

filtered_values = values[
    (values >= lower_limit) & (values <= upper_limit)
]

print("Mean:", mean)
print("Standard deviation:", standard_deviation)
print("Values without outliers:", filtered_values)