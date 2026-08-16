roles = {
    "Dinesh": "admin",
    "Rahul": "user",
    "Ravi": "manager"
}


def access_control(required_role):

    def decorator(function):

        def wrapper(username):

            if username in roles:

                if roles[username] == required_role:
                    return function(username)

                else:
                    print("Access Denied")

            else:
                print("User not found")

        return wrapper

    return decorator


@access_control("admin")
def delete_data(username):
    print(username, "can delete data.")


@access_control("manager")
def view_reports(username):
    print(username, "can view reports.")


print("Delete Data:")
delete_data("Dinesh")
delete_data("Rahul")

print("\nView Reports:")
view_reports("Ravi")
view_reports("Dinesh")