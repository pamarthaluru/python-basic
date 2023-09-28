"""
Create virtual environment and install Faker package only for this venv.
Write command line tool which will receive int as a first argument and one or more named arguments
 and generates defined number of dicts separated by new line.
Exec format:
`$python task_4.py NUMBER --FIELD=PROVIDER [--FIELD=PROVIDER...]`
where:
NUMBER - positive number of generated instances
FIELD - key used in generated dict
PROVIDER - name of Faker provider
Example:
`$python task_4.py 2 --fake-address=address --some_name=name`
{"some_name": "Chad Baird", "fake-address": "62323 Hobbs Green\nMaryshire, WY 48636"}
{"some_name": "Courtney Duncan", "fake-address": "8107 Nicole Orchard Suite 762\nJosephchester, WI 05981"}
"""

import argparse


def print_name_address(args: argparse.Namespace) -> None:
    fake=Faker()
    number=args.number
    fields=args.fields

    for _ in range(number):
        data={field:getattr(fake,field)() for field in fields}
        print(data)

if __name__=="__main__":
    parser=argparse.ArgumentParser(description="Generate dictionaries with Faker data")
    parser.add_argument("number",type=int,help="Number of dictionaries to generate")
    parser.add_argument("-f","--fields",nargs="+",help="list of fields to include in dictionaries",required=True)
    args=parser.parse_args()

    print_name_address(args)

"""
Write test for print_name_address function
Use Mock for mocking args argument https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock
Example:
    >>> m = Mock()
    >>> m.method.return_value = 123
    >>> m.method()
    123
"""

import unittest
from unittest.mock import patch
from task_4 import print_name_address

class TestPrintNameAddress(unittest.TestCase):
    @patch("builtins.print")
    def test_print_name_address(self,mock_print):
        args=argparse.Namespace(number=2,fields=["name","address"])
        print_name_address(args)
        self.assertEqual(mock_print.count,2)

if __name__=="__main__":
    unittest.main()
