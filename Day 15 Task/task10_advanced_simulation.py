import random
import math
import numpy as np
import pandas as pd


class Student:

    def __init__(self, name, marks):

        self.name = name
        self.marks = marks

    def get_grade(self):

        if self.marks >= 90:
            return "A"

        elif self.marks >= 75:
            return "B"

        elif self.marks >= 60:
            return "C"

        elif self.marks >= 40:
            return "D"

        else:
            return "Fail"


names = [
    "Dinesh",
    "Rahul",
    "Ravi",
    "Kiran",
    "Anil",
    "Suresh",
    "Arjun",
    "Vijay",
    "Ramesh",
    "Ajay"
]


try:

    # Generate random marks
    marks = np.array([
        random.randint(0, 100)
        for i in range(10)
    ])

    print("Random Marks:")
    print(marks)

    students = []

    # Create Student objects
    for i in range(10):

        student = Student(names[i], marks[i])

        students.append(student)

    # Create report
    report = []

    for student in students:

        grade = student.get_grade()

        report.append({
            "Name": student.name,
            "Marks": student.marks,
            "Grade": grade
        })

    # Convert report to DataFrame
    df = pd.DataFrame(report)

    print("\nExam Report:")
    print(df)

    # Calculate statistics
    average = np.mean(marks)

    standard_deviation = np.std(marks)

    print("\nAverage Marks:", average)

    print("Standard Deviation:", standard_deviation)

    # Save report to file
    with open("exam_report.txt", "w") as file:

        file.write("EXAM REPORT\n")
        file.write("====================\n")

        for student in students:

            file.write(
                student.name
                + " - "
                + str(student.marks)
                + " - "
                + student.get_grade()
                + "\n"
            )

        file.write("\nAverage: " + str(average))

        file.write(
            "\nStandard Deviation: "
            + str(standard_deviation)
        )

    print("\nReport saved successfully.")

except Exception as e:

    print("Error:", e)