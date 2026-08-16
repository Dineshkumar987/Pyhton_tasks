from utilities import math_operations
from utilities import string_operations

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition =", math_operations.add(a, b))
print("Multiplication =", math_operations.multiply(a, b))

text = input("Enter a string: ")

print("Uppercase =", string_operations.to_upper(text))
print("Character Count =", string_operations.count_characters(text))