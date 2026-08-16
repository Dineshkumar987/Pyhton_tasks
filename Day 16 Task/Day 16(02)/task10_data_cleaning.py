import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = np.array([
    100,
    np.nan,
    200,
    150,
    np.nan,
    300
])

# Convert to Pandas Series
series = pd.Series(data)

print("Original Data:")
print(series)

# Calculate mean
mean_value = series.mean()

print("\nMean:", mean_value)

# Replace NaN with mean
cleaned_data = series.fillna(mean_value)

print("\nCleaned Data:")
print(cleaned_data)

# Filter values greater than average
above_average = cleaned_data[cleaned_data > mean_value]

print("\nValues Above Average:")
print(above_average)

# Create figure
plt.figure(figsize=(10, 5))

# Line graph
plt.subplot(1, 2, 1)

plt.plot(
    cleaned_data,
    marker="o"
)

plt.title("Cleaned Data")
plt.xlabel("Index")
plt.ylabel("Value")
plt.grid()

# Bar chart
plt.subplot(1, 2, 2)

plt.bar(
    above_average.index,
    above_average.values
)

plt.title("Values Above Average")
plt.xlabel("Index")
plt.ylabel("Value")

plt.tight_layout()

plt.show()