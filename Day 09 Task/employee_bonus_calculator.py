def bonus(func):
    def wrapper(self):
        self.salary += 5000
        func(self)
    return wrapper


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @bonus
    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


e = Employee("Rahul", 40000)
e.display()