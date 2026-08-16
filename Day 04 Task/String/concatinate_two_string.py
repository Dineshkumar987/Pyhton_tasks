str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

result = str1 + str2

print("Concatenated String:", result)
text = input("Enter the main string: ")
sub = input("Enter the substring: ")

if sub in text:
    print("Substring found.")
else:
    print("Substring not found.")