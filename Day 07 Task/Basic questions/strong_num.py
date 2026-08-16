num = int(input("Enter a number: "))
original = num
sum = 0

while num > 0:
    digit = num % 10
    fact = 1

    for i in range(1, digit + 1):
        fact *= i

    sum += fact
    num //= 10

if sum == original:
    print(original, "is a Strong number.")
else:
    print(original, "is not a Strong number.")