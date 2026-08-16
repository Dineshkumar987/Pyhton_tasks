try:

    with open("logs.txt", "a") as file:

        while True:

            action = input("Enter user action: ")

            if action.lower() == "exit":
                break

            file.write(action + "\n")

    print("Logs saved successfully.")

except FileNotFoundError:
    print("File not found.")

except PermissionError:
    print("Permission denied.")

except Exception as e:
    print("Error:", e)