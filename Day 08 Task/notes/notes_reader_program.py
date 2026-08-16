# Notes Reader Program

try:
    with open("notes.txt", "r") as file:
        content = file.read()

    print("Notes:")
    print(content)

except FileNotFoundError:
    print("notes.txt file not found.")