import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

names = ["A", "B", "C", "D"]
marks = np.array([70, 85, 60, 90])

df = pd.DataFrame({
    "Name": names,
    "Marks": marks
})

print(df)

plt.bar(df["Name"], df["Marks"])

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks")

plt.show()