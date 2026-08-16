import pandas as pd

df = pd.DataFrame({
    "A": [10, 20, 30],
    "B": [5, 15, 25]
}, index=["x", "y", "z"])

# Select row y
print("Row y:")
print(df.loc["y"])

# Delete row x
df = df.drop("x")

print("\nUpdated DataFrame:")
print(df)