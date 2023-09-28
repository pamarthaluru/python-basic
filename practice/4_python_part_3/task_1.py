"""
using datetime module find number of days from custom date to now
Custom date is a string with format "2021-12-24"
If entered string pattern does not match, raise a custom Exception
If entered date is from future, return negative value for number of days
    >>> calculate_days('2021-10-07')  # for this example today is 6 october 2021
    -1
    >>> calculate_days('2021-10-05')
    1
    >>> calculate_days('10-07-2021')
    WrongFormatException
"""
from datetime import datetime
class WrongFormatException(Exception):
    pass

def calculate_days(from_date: str) -> int:
    try:
        input_date=datetime.strptime(from_date,"%Y-%m-%d")
    except ValueError:
        raise WrongFormatException("Invalid date format. Use 'YYYY-MM-DD' format.")

    current_date=datetime.now()
    delta=current_date-input_date
    if input_date>current_date:
        return delta.days
    return delta.days

print(calculate_days('2023-09-19'))
print(calculate_days('2023-09-24'))


"""
Write tests for calculate_days function
Note that all tests should pass regardless of the day test was run
Tip: for mocking datetime.now() use https://pypi.org/project/pytest-freezegun/
"""


import pytest
from datetime import datetime
from calculate_days import calculate_days, WrongFormatException
from freezegun import freeze_time

@freeze_time("2023-09-23")
def test_calculate_days_past_date():
    result=calculate_days("2023-09-19")
    assert result==-4

@freeze_time("2023-09-23")
def test_calculate_future_date():
    result=calculate_days("2023-09-24")
    assert result==1

def test_calculate_days_wrong_format():
    with pytest.raises(WrongFormatException):
        calculate_days("10-07-2023")

if __name__=="__main__":
    pytest.main()