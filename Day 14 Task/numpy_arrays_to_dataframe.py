import numpy as np
import pandas as pd

names = np.array(["A", "B", "C"])
marks = np.array([80, 90, 70])

df = pd.DataFrame({
    "Name": names,
    "Marks": marks
})

print("Student Data:")
print(df)

result = df[df["Marks"] > 75]

print("\nStudents with marks above 75:")
print(result)