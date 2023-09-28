"""
Write function which executes custom operation from math module
for given arguments.
Restrition: math function could take 1 or 2 arguments
If given operation does not exists, raise OperationNotFoundException
Examples:
     >>> math_calculate('log', 1024, 2)
     10.0
     >>> math_calculate('ceil', 10.7)
     11
"""
import math

class OperationNotFoundException(Exception):
    pass

def math_calculate(function: str, *args):
    try:
        math_function=getattr(math,function)
    except AttributeError:
        raise OperationNotFoundException(f"Operation '{function} not found in the math module.")
    
    if len(args)==1:
        return math_function(args[0])
    elif len(args)==2:
        return math_function(args[0],args[1])
    else:
        raise ValueError("Math functions can take either 1 or 2 arguments.")
    ...
print(math_calculate('log', 1024, 2))
print(math_calculate('ceil', 10.7))

"""
Write tests for math_calculate function
"""

import unittest
import math
from task_2 import math_calculate, OperationNotFoundException
class TestMathCalculate(unittest.TestCase):
    def test_math_calculate_log(self):
        result=math_calculate('log',1024,2)
        self.assertEqual(result,10.0)

    def test_math_calculate_ceil(self):
        result=math_calculate('ceil',10.7)
        self.assertEqual(result,11)

    def test_math_calculate_sqrt(self):
        result=math_calculate('sqrt',16)
        self.assertEqual(result,4)

    def test_math_calculate_unknown_operation(self):
        with self.assertRaises(OperationNotFoundException):
            math_calculate('unknown_function',5)

    def test_math_calculate_invalid_arguments(self):
        with self.assertRaises(ValueError):
            math_calculate('ceil',10.7,2)

if __name__=="__main__":
    unittest.main()
