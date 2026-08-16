# Check voting eligibility

age = int(input("Enter your age: "))

if age >= 18 and age <= 100:
    print("Eligible for voting")
else:
    print("Not eligible for voting")