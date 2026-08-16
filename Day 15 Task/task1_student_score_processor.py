import math

# Student names and marks
students = [
    ("Dinesh", 75),
    ("Rahul", 45),
    ("Ravi", 65),
    ("Kiran", 30),
    ("Anil", 80)
]

# Convert list of tuples into dictionary
student_dict = dict(students)

print("Student Dictionary:")
print(student_dict)

# Find students scoring above 50
above_50 = []

for name, marks in student_dict.items():
    if marks > 50:
        above_50.append(name)

print("\nStudents scoring above 50:")
print(above_50)

# Calculate average
total = sum(student_dict.values())
average = total / len(student_dict)

print("\nAverage Marks:")
print(math.floor(average * 100) / 100)

# Store results in a text file
with open("student_results.txt", "w") as file:
    file.write("Student Results\n")
    file.write(str(student_dict) + "\n")
    file.write("Students above 50: " + str(above_50) + "\n")
    file.write("Average: " + str(average))

print("\nResults saved to student_results.txt")