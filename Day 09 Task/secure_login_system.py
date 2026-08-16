logged_in = True

def login_required(func):
    def wrapper():
        if logged_in:
            func()
        else:
            print("Please Login")
    return wrapper


@login_required
def dashboard():
    print("Welcome to Dashboard")


dashboard()