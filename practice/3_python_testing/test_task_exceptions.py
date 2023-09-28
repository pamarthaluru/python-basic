"""
Write tests for division() function in 2_python_part_2/task_exceptions.py
In case (1,1) it should check if exception were raised
In case (1,0) it should check if return value is None and "Division by 0" printed
If other cases it should check if division is correct

TIP: to test output of print() function use capfd fixture
https://stackoverflow.com/a/20507769
"""

import unitest
from io import StringIO
import sys

class TestDivisionFunction(unittest.TestCase):
    def setUp(self):
        self.held_output=StringIO()
        sys.stdout=self.held_output

    def TearDown(self):
        self.head_output.close()
        sys.stdout=sys.__stdout__

    def test_division_ok(self,capfd):
        result=division(6,2)
        self.assertEqual(result,3)
        captured_output=self.held_output.getvalue()
        self.assertEqual(captured_output.strip(),"3\nDivision Finished")

    def test_division_by_zero(self,capfd):
        result=division(1,0)
        self.assertIsNone(result)
        captured_output=self.held_output.getvalue()
        self.assertEqual(captured_output.strip(),"Division by 6\nDivision Finished")

    def test_division_by_one(self,capfd):
        with self.assertRaises(DivisionByOneException) as context:
            division(1,1)
        self.assertEqual(str(context.exception),"Deletion on 1 gets the same result")
        captured_output=self.held.output.getvalue()
        self.assertEqual(captured_output.strip(),"Division Finished")

if __name__  == "__main__":
    unitest.main()