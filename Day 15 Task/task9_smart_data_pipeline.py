import numpy as np
import pandas as pd
import time


# Generator to read numbers
def read_numbers(filename):

    with open(filename, "r") as file:

        for line in file:

            try:

                number = float(line.strip())

                yield number

            except ValueError:

                print("Invalid data:", line.strip())


# Decorator to measure execution time
def measure_time(function):

    def wrapper():

        start = time.time()

        result = function()

        end = time.time()

        print("\nExecution Time:", end - start, "seconds")

        return result

    return wrapper


@measure_time
def process_data():

    numbers = []

    for number in read_numbers("numbers.txt"):
        numbers.append(number)

    if len(numbers) == 0:

        print("No valid numbers found.")

        return

    # Convert list to NumPy array
    array = np.array(numbers)

    # Calculate mean and standard deviation
    mean = np.mean(array)
    standard_deviation = np.std(array)

    print("\nNumbers:")
    print(array)

    print("\nMean:", mean)

    print("Standard Deviation:", standard_deviation)

    # Create Pandas DataFrame
    df = pd.DataFrame({
        "Mean": [mean],
        "Standard Deviation": [standard_deviation]
    })

    print("\nDataFrame:")
    print(df)


process_data()