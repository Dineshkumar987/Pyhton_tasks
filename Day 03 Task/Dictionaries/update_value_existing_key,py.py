students = {
    "Ravi": 85,
    "Sita": 90,
    "Rahul": 78
}

name = input("Enter student name: ")

if name in students:
    print("Key exists.")
else:
    print("Key does not exist.")