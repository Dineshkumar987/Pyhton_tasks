import numpy as np

ratings = np.array([2, 3, 4, 5, 1])

minimum = np.min(ratings)
maximum = np.max(ratings)

normalized = (ratings - minimum) / (maximum - minimum)

print("Original ratings:", ratings)
print("Normalized ratings:", normalized)