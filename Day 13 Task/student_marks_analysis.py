import numpy as np

marks = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [50, 65, 70],
    [90, 95, 85],
    [40, 55, 60]
])

total_marks = np.sum(marks, axis=1)

class_average = np.mean(total_marks)

students_above_average = total_marks[total_marks > class_average]

print("Total marks:", total_marks)
print("Class average:", class_average)
print("Students above average:", students_above_average)