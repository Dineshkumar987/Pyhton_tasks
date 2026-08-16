def find_sum(lst):
    total = 0

    for num in lst:
        total += num

    return total

numbers = [10, 20, 30, 40, 50]

print("Sum =", find_sum(numbers))