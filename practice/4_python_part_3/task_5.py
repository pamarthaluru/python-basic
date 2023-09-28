"""
Write a function that makes a request to some url
using urllib. Return status code and decoded response data in utf-8
Examples:
     >>> make_request('https://www.google.com')
     200, 'response data'
"""
from urllib.request import urlopen
from typing import Tuple


def make_request(url: str) -> Tuple[int, str]:
    try:
        response=urlopen(url)
        status_code=response.status
        data=response.read().decode('utf-8')
        return status_code, data
    except Exception as e:
        return 500,str(e)

"""
Write test for make_request function
Use Mock for mocking request with urlopen https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock
Example:
    >>> m = Mock()
    >>> m.method.return_value = 200
    >>> m.method2.return_value = b'some text'
    >>> m.method()
    200
    >>> m.method2()
    b'some text'
"""

import unittest
from unittest.mock import patch
from task_5 import make_request
class TestMakeRequest(unittest.TestCase):
    @patch("urlib.request.urlopen")
    def test_make_request_success(self,mock_urlopen):
        mock_response=unittest.mock.Mock()
        mock_response.status=200
        mock_response.read.return_value=b'response data'
        mock_urlopen.return_value=mock_response

        status_code,data=make.request('https://www.google.com')
        self.assertEqual(status_code,200)
        self.asserEqual(data,'response data')

    @patch("urlib.request.urlopen")
    def test_make_request_error(self,mock_urlopen):
        mock.urlopen.side_effect=Exception("Requuest error")
        status_code,data =make_request('https://www.invalid-url.com')
        self.assertEqual(status_code,500)
        self.assertIn('Request error',data)

if __name__=="__main__":
    unittest.main()


