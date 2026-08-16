num = int(input("Enter a number: "))
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if reverse == original:
    print(original, "is a Palindrome number.")
else:
    print(original, "is not a Palindrome number.")