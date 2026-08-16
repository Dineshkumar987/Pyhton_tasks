num = int(input("Enter a number: "))

if num <= 1:
    print(num, "is not a Prime number.")
else:
    prime = True

    for i in range(2, num // 2 + 1):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num, "is a Prime number.")
    else:
        print(num, "is not a Prime number.")