# Grocery List Manager

n = int(input("Enter number of grocery items: "))

with open("grocery.txt", "w") as file:
    for i in range(n):
        item = input(f"Enter item {i+1}: ")
        file.write(item + "\n")

print("Grocery items saved successfully.")