"""
Write function which receives list of integers. Calculate power of each integer and
subtract difference between original previous value and it's power. For first value subtract nothing.
Restriction:
Examples:
    >>> calculate_power_with_difference([1, 2, 3])
    [1, 4, 7]  # because [1^2, 2^2 - (1^2 - 1), 3^2 - (2^2 - 2)]
"""
from typing import List


def calculate_power_with_difference(ints: List[int]) -> List[int]:
    result=[]
    prev_value=0
    num1=0
    

    for num in ints:
        
        power=num**2
        result.append(power-(prev_value-num1))
        prev_value=power
        num1=num

    return result

input_list=[1,2,3]
print(calculate_power_with_difference(input_list))
