def read_logs(filename):

    with open(filename, "r") as file:

        for line in file:
            yield line.strip()


error_count = {}

try:

    for log in read_logs("logs.txt"):

        if "ERROR" in log:

            print("Error:", log)

            message = log.replace("ERROR ", "")

            if message in error_count:
                error_count[message] += 1
            else:
                error_count[message] = 1

    print("\nError Count:")

    for error, count in error_count.items():
        print(error, ":", count)

except FileNotFoundError:

    print("logs.txt file not found.")