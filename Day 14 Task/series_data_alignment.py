import pandas as pd

S1 = pd.Series([10, 20, 30], index=["a", "b", "c"])
S2 = pd.Series([5, 15, 25], index=["b", "c", "d"])

result = S1 + S2

print("After addition:")
print(result)

result = result.fillna(0)

print("\nAfter replacing NaN with 0:")
print(result)

print("\nFinal total:", result.sum())