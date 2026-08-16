import pandas as pd

df = pd.DataFrame({
    "Name": ["A", "B", "C", "D"],
    "Marks": [50, 80, 30, 90]
})

# Create Status column
df["Status"] = df["Marks"].apply(
    lambda x: "Fail" if x < 50 else "Pass"
)

print("Complete DataFrame:")
print(df)

# Filter passed students
passed = df[df["Status"] == "Pass"]

print("\nPassed Students:")
print(passed)

# Average marks
average = passed["Marks"].mean()

print("\nAverage marks of passed students:", average)