import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

marks = np.array([45, 67, 89, 56, 72, 91, 38])
students = ["A", "B", "C", "D", "E", "F", "G"]

df = pd.DataFrame({
    "Student": students,
    "Marks": marks
})

print(df)

pass_count = np.sum(marks > 50)
fail_count = np.sum(marks <= 50)

fig, axes = plt.subplots(2, 3, figsize=(15, 9))

# Line graph
axes[0, 0].plot(df["Student"], df["Marks"], marker="o")
axes[0, 0].set_title("Marks Trend")
axes[0, 0].set_xlabel("Students")
axes[0, 0].set_ylabel("Marks")

# Bar chart
axes[0, 1].bar(df["Student"], df["Marks"])
axes[0, 1].set_title("Student vs Marks")
axes[0, 1].set_xlabel("Students")
axes[0, 1].set_ylabel("Marks")

# Pie chart
axes[0, 2].pie(
    [pass_count, fail_count],
    labels=["Pass", "Fail"],
    autopct="%1.1f%%"
)
axes[0, 2].set_title("Pass vs Fail")

# Histogram
axes[1, 0].hist(marks, bins=5)
axes[1, 0].set_title("Marks Distribution")
axes[1, 0].set_xlabel("Marks")
axes[1, 0].set_ylabel("Frequency")

# Scatter plot
index = np.arange(len(marks))

axes[1, 1].scatter(index, marks)
axes[1, 1].set_title("Index vs Marks")
axes[1, 1].set_xlabel("Index")
axes[1, 1].set_ylabel("Marks")

axes[1, 2].axis("off")

plt.tight_layout()
plt.show()