import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = np.array([100, 200, 150, 300])
products = ["A", "B", "C", "D"]

df = pd.DataFrame({
    "Product": products,
    "Sales": sales
})

print(df)

# Create one figure
plt.figure(figsize=(12, 8))

# Line graph
plt.subplot(2, 2, 1)

plt.plot(
    df["Product"],
    df["Sales"],
    marker="o"
)

plt.title("Sales Trend")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.grid()

# Bar chart
plt.subplot(2, 2, 2)

plt.bar(
    df["Product"],
    df["Sales"]
)

plt.title("Sales Comparison")
plt.xlabel("Product")
plt.ylabel("Sales")

# Pie chart
plt.subplot(2, 2, 3)

plt.pie(
    df["Sales"],
    labels=df["Product"],
    autopct="%1.1f%%"
)

plt.title("Sales Distribution")

plt.tight_layout()

plt.show()