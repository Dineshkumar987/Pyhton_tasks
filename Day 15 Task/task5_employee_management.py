class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


employees = {}

while True:

    print("\n1. Add Employee")
    print("2. Display Employees")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter employee name: ")

        try:

            salary = float(input("Enter salary: "))

            employee = Employee(name, salary)

            employees[name] = employee

            print("Employee added successfully.")

        except ValueError:
            print("Invalid salary. Please enter a number.")

    elif choice == "2":

        if len(employees) == 0:
            print("No employees found.")

        else:

            print("\nEmployee Details:")

            for name, employee in employees.items():
                employee.display()
                print("----------------")

    elif choice == "3":

        break

    else:

        print("Invalid choice.")


# Save employee data to file
try:

    with open("employees.txt", "w") as file:

        for name, employee in employees.items():

            file.write(
                "Name: " + employee.name +
                ", Salary: " + str(employee.salary) + "\n"
            )

    print("Employee data saved successfully.")

except Exception as e:

    print("File error:", e)