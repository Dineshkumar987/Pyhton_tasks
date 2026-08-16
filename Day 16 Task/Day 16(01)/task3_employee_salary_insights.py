import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])
departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]

df = pd.DataFrame({
    "Department": departments,
    "Salary": salaries
})

print(df)

# Department-wise total salary
department_salary = df.groupby("Department")["Salary"].sum()

# Department-wise employee count
department_count = df["Department"].value_counts()

fig, axes = plt.subplots(2, 3, figsize=(15, 9))

# Line graph
axes[0, 0].plot(df.index, df["Salary"], marker="o")
axes[0, 0].set_title("Salary Trend")
axes[0, 0].set_xlabel("Employee Index")
axes[0, 0].set_ylabel("Salary")

# Bar chart
axes[0, 1].bar(
    department_salary.index,
    department_salary.values
)
axes[0, 1].set_title("Department-wise Salary")
axes[0, 1].set_xlabel("Department")
axes[0, 1].set_ylabel("Total Salary")

# Pie chart
axes[0, 2].pie(
    department_count.values,
    labels=department_count.index,
    autopct="%1.1f%%"
)
axes[0, 2].set_title("Department Distribution")

# Histogram
axes[1, 0].hist(salaries, bins=5)
axes[1, 0].set_title("Salary Distribution")
axes[1, 0].set_xlabel("Salary")
axes[1, 0].set_ylabel("Frequency")

# Scatter plot
axes[1, 1].scatter(df.index, df["Salary"])
axes[1, 1].set_title("Employee Index vs Salary")
axes[1, 1].set_xlabel("Employee Index")
axes[1, 1].set_ylabel("Salary")

axes[1, 2].axis("off")

plt.tight_layout()
plt.show()