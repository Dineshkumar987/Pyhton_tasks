students = {
    "Ravi": 85,
    "Sita": 90,
    "Rahul": 78
}

lowest = min(students, key=students.get)

print("Student with lowest marks:", lowest)
print("Marks:", students[lowest])