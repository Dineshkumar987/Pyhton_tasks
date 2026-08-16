import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = np.array([100, 150, 200, 180, 220, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

df = pd.DataFrame({
    "Month": months,
    "Sales": sales
})

print(df)

fig, axes = plt.subplots(2, 3, figsize=(15, 9))

# Line graph
axes[0, 0].plot(df["Month"], df["Sales"], marker="o")
axes[0, 0].set_title("Sales Trend")
axes[0, 0].set_xlabel("Month")
axes[0, 0].set_ylabel("Sales")

# Bar chart
axes[0, 1].bar(df["Month"], df["Sales"])
axes[0, 1].set_title("Month-wise Sales")
axes[0, 1].set_xlabel("Month")
axes[0, 1].set_ylabel("Sales")

# Pie chart
axes[0, 2].pie(
    df["Sales"],
    labels=df["Month"],
    autopct="%1.1f%%"
)
axes[0, 2].set_title("Monthly Sales Contribution")

# Histogram
axes[1, 0].hist(df["Sales"], bins=5)
axes[1, 0].set_title("Sales Frequency")
axes[1, 0].set_xlabel("Sales")
axes[1, 0].set_ylabel("Frequency")

# Scatter plot
index = np.arange(len(sales))

axes[1, 1].scatter(index, sales)
axes[1, 1].set_title("Month Index vs Sales")
axes[1, 1].set_xlabel("Month Index")
axes[1, 1].set_ylabel("Sales")

axes[1, 2].axis("off")

plt.tight_layout()
plt.show()