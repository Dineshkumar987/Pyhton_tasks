student = input("Enter student name: ")

with open("attendance.txt", "a") as file:
    file.write(student + "\n")

print("\nAttendance Records:")

with open("attendance.txt", "r") as file:
    for line in file:
        print(line.strip())