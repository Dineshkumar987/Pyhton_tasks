import calculator

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Choose Operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Result =", calculator.addition(a, b))
elif choice == 2:
    print("Result =", calculator.subtraction(a, b))
elif choice == 3:
    print("Result =", calculator.multiplication(a, b))
elif choice == 4:
    print("Result =", calculator.division(a, b))
else:
    print("Invalid Choice")