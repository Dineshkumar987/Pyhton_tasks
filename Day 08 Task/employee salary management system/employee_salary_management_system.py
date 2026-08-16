# Employee Salary Management System

filename = "employees.txt"

# Read employee data from the file
employees = []

try:
    with open(filename, "r") as file:
        for line in file:
            data = line.strip().split()
            if len(data) == 2:
                name = data[0]
                salary = int(data[1])
                employees.append((name, salary))

    # Display all employee details
    print("Employee Details:")
    for emp in employees:
        print("Name:", emp[0], " Salary:", emp[1])

    # Find employee with the highest salary
    if employees:
        highest = max(employees, key=lambda x: x[1])
        print("\nEmployee with Highest Salary:")
        print("Name:", highest[0], " Salary:", highest[1])

except FileNotFoundError:
    print("File not found. A new file will be created.")

# Append a new employee record
name = input("\nEnter new employee name: ")
salary = int(input("Enter salary: "))

with open(filename, "a") as file:
    file.write(f"{name} {salary}\n")

print("New employee record added successfully.")