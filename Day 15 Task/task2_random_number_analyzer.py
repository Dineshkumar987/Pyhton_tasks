import random

numbers = []

# Generate 10 random numbers
for i in range(10):
    numbers.append(random.randint(1, 20))

print("Random Numbers:")
print(numbers)

even = 0
odd = 0

# Count even and odd numbers
for number in numbers:
    if number % 2 == 0:
        even += 1
    else:
        odd += 1

print("\nEven Numbers:", even)
print("Odd Numbers:", odd)

# Remove duplicates
unique_numbers = set(numbers)

print("\nNumbers after removing duplicates:")
print(unique_numbers)