items = []

print("Available items:")
print("Apple - 50")
print("Milk - 40")
print("Bread - 30")
print("Rice - 60")

print("\nType 'done' when finished.")

while True:
    item = input("Enter item: ")

    if item.lower() == "done":
        break

    items.append(item.lower())

# Remove duplicate items
unique_items = set(items)

prices = {
    "apple": 50,
    "milk": 40,
    "bread": 30,
    "rice": 60
}

total = 0

try:

    for item in unique_items:

        if item in prices:
            total += prices[item]
        else:
            print("Invalid item:", item)

    print("\nShopping Cart:")
    print(unique_items)

    print("Total Cost:", total)

except Exception as e:
    print("Error:", e)