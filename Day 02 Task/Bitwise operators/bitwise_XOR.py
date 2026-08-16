# Left Shift and Right Shift

num = int(input("Enter a number: "))
shift = int(input("Enter number of shift positions: "))

left = num << shift
right = num >> shift

print("Left Shift:", left)
print("Right Shift:", right)