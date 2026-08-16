import numpy as np

# List of marks
marks = [45, 67, 89, 56, 72]

# Convert list to NumPy array
marks_array = np.array(marks)

# Add 5 grace marks
updated_marks = marks_array + 5

# Print updated marks
print("Updated Marks:", updated_marks)