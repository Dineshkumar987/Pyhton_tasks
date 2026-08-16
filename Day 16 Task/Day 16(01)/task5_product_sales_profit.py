import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = np.array([200, 300, 250, 400, 350])
profit = np.array([50, 70, 60, 90, 80])
products = ["A", "B", "C", "D", "E"]

df = pd.DataFrame({
    "Product": products,
    "Sales": sales,
    "Profit": profit
})

print(df)

fig, axes = plt.subplots(2, 3, figsize=(15, 9))

# Line graph
axes[0, 0].plot(
    df["Product"],
    df["Sales"],
    marker="o"
)
axes[0, 0].set_title("Sales Trend")
axes[0, 0].set_xlabel("Product")
axes[0, 0].set_ylabel("Sales")

# Bar chart
axes[0, 1].bar(
    df["Product"],
    df["Sales"]
)
axes[0, 1].set_title("Product vs Sales")
axes[0, 1].set_xlabel("Product")
axes[0, 1].set_ylabel("Sales")

# Pie chart
axes[0, 2].pie(
    df["Sales"],
    labels=df["Product"],
    autopct="%1.1f%%"
)
axes[0, 2].set_title("Sales Contribution")

# Histogram
axes[1, 0].hist(
    df["Profit"],
    bins=5
)
axes[1, 0].set_title("Profit Distribution")
axes[1, 0].set_xlabel("Profit")
axes[1, 0].set_ylabel("Frequency")

# Scatter plot
axes[1, 1].scatter(
    df["Sales"],
    df["Profit"]
)
axes[1, 1].set_title("Sales vs Profit")
axes[1, 1].set_xlabel("Sales")
axes[1, 1].set_ylabel("Profit")

axes[1, 2].axis("off")

plt.tight_layout()
plt.show()