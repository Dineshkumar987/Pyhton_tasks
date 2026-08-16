import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

temps = np.array([28, 30, 32, 31, 29])

temperature_series = pd.Series(temps)

print(temperature_series)

plt.plot(temperature_series, marker="o")

plt.title("Temperature Trend")
plt.xlabel("Day")
plt.ylabel("Temperature")

plt.grid()

plt.show()