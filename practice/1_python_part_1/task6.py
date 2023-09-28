"""
Write function which receives filename and reads file line by line and returns min and mix integer from file.
Restriction: filename always valid, each line of file contains valid integer value
Examples:
    # file contains following lines:
        10
        -2
        0
        34
    >>> get_min_max('filename')
    (-2, 34)

Hint:
To read file line-by-line you can use this:
with open(filename) as opened_file:
    for line in opened_file:
        ...
"""
from typing import Tuple


def get_min_max(filename: str) -> Tuple[int, int]:
    with open(filename) as opened_file:
        min_value=float('inf')
        max_value=float('-inf')

        for line in opened_file:
            num=int(line.strip())
            min_value=min(min_value, num)
            max_value=max(max_value, num)

        return (min_value, max_value)
    
filename='/Users/pamarthaluru/PYTHON-BASIC/practice/1_python_part_1/example.txt'
min_max=get_min_max(filename)
print(min_max)
