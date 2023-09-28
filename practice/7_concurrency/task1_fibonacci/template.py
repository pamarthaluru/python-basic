import os
from random import randint


OUTPUT_DIR = './output'
RESULT_FILE = './output/result.csv'


def fib(n: int):
    """Calculate a value in the Fibonacci sequence by ordinal number"""

    f0, f1 = 0, 1
    for _ in range(n-1):
        f0, f1 = f1, f0 + f1
    return f1


def func1(array: list):
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Calculate Fibonacci numbers for each ordinal number in the array
    results = []
    for ordinal in array:
        result = fib(ordinal)
        results.append((ordinal, result))

    # Write results to separate files
    for ordinal, value in results:
        with open(os.path.join(OUTPUT_DIR, f'file_{ordinal}.txt'), 'w') as file:
            file.write(str(value))
    


def func2(result_file: str):
    # Read values from files in the OUTPUT_DIR directory
    results = []
    for filename in os.listdir(OUTPUT_DIR):
        if filename.endswith('.txt'):
            ordinal = int(filename.split('_')[1].split('.')[0])
            with open(os.path.join(OUTPUT_DIR, filename), 'r') as file:
                value = int(file.read())
            results.append((ordinal, value))

    # Sort the results by ordinal number
    results.sort(key=lambda x: x[0])

    # Create a CSV file with the ordinal number and its value
    with open(result_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(results)
    pass


if __name__ == '__main__':
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    func1(array=[randint(1000, 100000) for _ in range(1000)])
    func2(result_file=RESULT_FILE)
