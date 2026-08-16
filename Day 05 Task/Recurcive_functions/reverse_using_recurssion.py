def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]

text = input("Enter a string: ")
print("Reversed string:", reverse_string(text))