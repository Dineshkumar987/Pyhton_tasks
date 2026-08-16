import numpy as np
import pandas as pd

# Student names
names = [
    "Dinesh",
    "Rahul",
    "Ravi",
    "Kiran",
    "Anil",
    "Suresh",
    "Arjun",
    "Vijay",
    "Ramesh",
    "Ajay"
]

# Generate random marks
marks = np.random.randint(20, 101, 10)

# Create Pandas DataFrame
df = pd.DataFrame({
    "Name": names,
    "Marks": marks
})

print("Student Data:")
print(df)

# Filter passing students
passing_students = df[df["Marks"] >= 40]

print("\nPassing Students:")
print(passing_students)

# Calculate mean
mean_marks = np.mean(marks)

print("\nMean Marks:", mean_marks)

# Print results using loop
print("\nStudent Results:")

for index, row in df.iterrows():

    if row["Marks"] >= 40:
        print(row["Name"], "-", row["Marks"], "- Pass")
    else:
        print(row["Name"], "-", row["Marks"], "- Fail")