students = {
    "Ravi": 85,
    "Sita": 90,
    "Rahul": 78
}

highest = max(students, key=students.get)

print("Student with highest marks:", highest)
print("Marks:", students[highest])