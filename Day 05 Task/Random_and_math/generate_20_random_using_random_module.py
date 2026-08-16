import random
import math

numbers = []

for i in range(20):
    numbers.append(random.randint(1, 200))

print("Random Numbers:", numbers)

maximum = max(numbers)
minimum = min(numbers)

print("Maximum Value =", maximum)
print("Minimum Value =", minimum)
print("Square Root of Maximum =", math.sqrt(maximum))
print("Logarithm of Minimum =", math.log(minimum))