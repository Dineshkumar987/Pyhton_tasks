import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

scores = np.array([40, 60, 80, 30, 90])

df = pd.DataFrame({
    "Score": scores
})

# Categorize scores
df["Result"] = np.where(
    df["Score"] > 50,
    "Pass",
    "Fail"
)

print(df)

# Count Pass and Fail
result_count = df["Result"].value_counts()

print("\nResult Count:")
print(result_count)

plt.pie(
    result_count,
    labels=result_count.index,
    autopct="%1.1f%%"
)

plt.title("Pass vs Fail")

plt.show()