import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Execution Time:", end - start)
    return wrapper


@timer
def test():
    time.sleep(2)
    print("Task Completed")


test()