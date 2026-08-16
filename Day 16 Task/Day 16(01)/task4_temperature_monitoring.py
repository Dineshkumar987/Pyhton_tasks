import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

temps = np.array([28, 30, 32, 35, 33, 31, 29])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

df = pd.DataFrame({
    "Day": days,
    "Temperature": temps
})

print(df)

high_count = np.sum(temps > 30)
low_count = np.sum(temps <= 30)

fig, axes = plt.subplots(2, 3, figsize=(15, 9))

# Line graph
axes[0, 0].plot(
    df["Day"],
    df["Temperature"],
    marker="o"
)
axes[0, 0].set_title("Daily Temperature Trend")
axes[0, 0].set_xlabel("Day")
axes[0, 0].set_ylabel("Temperature")

# Bar chart
axes[0, 1].bar(
    df["Day"],
    df["Temperature"]
)
axes[0, 1].set_title("Day-wise Temperature")
axes[0, 1].set_xlabel("Day")
axes[0, 1].set_ylabel("Temperature")

# Pie chart
axes[0, 2].pie(
    [high_count, low_count],
    labels=["High (>30)", "Low (<=30)"],
    autopct="%1.1f%%"
)
axes[0, 2].set_title("High vs Low Temperature")

# Histogram
axes[1, 0].hist(temps, bins=5)
axes[1, 0].set_title("Temperature Frequency")
axes[1, 0].set_xlabel("Temperature")
axes[1, 0].set_ylabel("Frequency")

# Scatter plot
index = np.arange(len(temps))

axes[1, 1].scatter(index, temps)
axes[1, 1].set_title("Day Index vs Temperature")
axes[1, 1].set_xlabel("Day Index")
axes[1, 1].set_ylabel("Temperature")

axes[1, 2].axis("off")

plt.tight_layout()
plt.show()