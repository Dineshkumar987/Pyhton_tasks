class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)
        print()

# Creating objects
s1 = Student("Dinesh", 101, 85)
s2 = Student("Murari", 102, 90)
s3 = Student("Shiva", 103, 78)

# Display details
s1.display()
s2.display()
s3.display()