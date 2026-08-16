# Student Marks Management System

subjects = ("Math", "Science", "English")
students = set()
student_marks = {}

# Recursive function to calculate total marks
def total_marks(marks, index=0):
    if index == len(marks):
        return 0
    return marks[index] + total_marks(marks, index + 1)

# Function to add student
def add_student():
    try:
        name = input("Enter student name: ")

        marks = []
        for subject in subjects:
            mark = float(input(f"Enter marks for {subject}: "))
            marks.append(mark)

        if not isinstance(marks, list):
            raise TypeError

        students.add(name)
        student_marks[name] = marks
        print("Student added successfully.\n")

    except ValueError:
        print("Invalid input! Please enter numeric marks.\n")
    except TypeError:
        print("Marks data type error.\n")

# Function to display students
def display_students():
    if not student_marks:
        print("No student records found.\n")
    else:
        print("\nStudent Records:")
        for name, marks in student_marks.items():
            print(name, ":", marks)
        print()

# Function to calculate average
def calculate_average():
    try:
        name = input("Enter student name to calculate average: ")

        if name not in student_marks:
            raise NameError

        marks = student_marks[name]

        if not isinstance(marks, list):
            raise TypeError

        total = total_marks(marks)

        if len(marks) == 0:
            raise ZeroDivisionError

        average = total / len(marks)

        print("Total Marks:", total)
        print("Average Marks:", average)
        print()

    except NameError:
        print("Student name not found.\n")
    except ZeroDivisionError:
        print("Cannot divide by zero.\n")
    except TypeError:
        print("Marks data type error.\n")

# Main Menu
while True:
    print("1. Add Student")
    print("2. Display Students")
    print("3. Calculate Average")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        calculate_average()
    elif choice == "4":
        print("Program Exited.")
        break
    else:
        print("Invalid choice.\n")