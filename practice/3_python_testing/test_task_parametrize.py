"""
Write a parametrized test for two functions.
The functions are used to find a number by ordinal in the Fibonacci sequence.
One of them has a bug.

Fibonacci sequence: https://en.wikipedia.org/wiki/Fibonacci_number

Task:
 1. Write a test with @pytest.mark.parametrize decorator.
 2. Find the buggy function and fix it.
"""


def fibonacci_1(n):
    a, b = 0, 1
    for _ in range(n-1):
        a, b = b, a + b
    return b


def fibonacci_2(n):
    fibo = [0, 1]
    for i in range(1, n+1):
        fibo.append(fibo[i-1] + fibo[i-2])
    return fibo[n]

import pytest
from test_task_parametrize import fibonacci_1, fibonacci_2

test_cases=[
    (0,0),
    (1,1),
    (2,1),
    (3,2),
    (4,3),
    (5,5),
    (6,8),
]

@pytest.mark.parametrize("n, expected",test_cases)
def test_fibonacci_function(n,expected):
    result_1=fibonacci_1(n)
    result_2=fibonacci_2(n)

    assert result_1==result_2==expected

if __name__=="__main":
    pytest.main()