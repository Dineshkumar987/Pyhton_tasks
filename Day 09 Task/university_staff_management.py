class Staff:
    def __init__(self, name):
        self.name = name


class Professor(Staff):
    def display(self):
        print("Professor:", self.name)


class LabAssistant(Staff):
    def display(self):
        print("Lab Assistant:", self.name)


class Administrator(Staff):
    def display(self):
        print("Administrator:", self.name)


Professor("Dr.Dinesh").display()
LabAssistant("Ravi").display()
Administrator("Anita").display()