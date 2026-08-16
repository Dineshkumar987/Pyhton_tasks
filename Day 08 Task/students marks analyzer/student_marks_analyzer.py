# Student Marks File Analyzer

with open("marks.txt", "r") as file:
    total = 0
    count = 0

    print("Student Records:")

    for line in file:
        name, marks = line.split()

        marks = int(marks)

        print(name, ":", marks)

        total += marks
        count += 1

    average = total / count

    print("Average Marks:", average)