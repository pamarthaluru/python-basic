"""
Write tests for a read_numbers function.
It should check successful and failed cases
for example:
Test if user inputs: 1, 2, 3, 4
Test if user inputs: 1, 2, Text

Tip: for passing custom values to the input() function
Use unittest.mock patch function
https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch

TIP: for testing builtin input() function create another function which return input() and mock returned value
"""
import unittest
from unittest.mock import patch

class TestReadNumbersFunction(unittest.TestCase):
    @patch('builtins.input',side_effects=["1","2","3","4"])
    def test_read_numbers_without_text_input():
        result=read_numbers()
        self.assertEqual(result,[1,2,3,4])

    @patch('builtins.input',side_effects=["1","2","Text"])
    def test_read_numbers_with_text_input():
        with self.assertRaises(ValueError):
            read_numbers()

if __name__=="__main__":
    unittest.main()

