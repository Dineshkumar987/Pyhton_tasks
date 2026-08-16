class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


m = Manager("Dinesh", 50000)
m.display()