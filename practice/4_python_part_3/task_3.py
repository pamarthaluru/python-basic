"""
Write a function which detects if entered string is http/https domain name with optional slash at the and
Restriction: use re module
Note that address may have several domain levels
    >>>is_http_domain('http://wikipedia.org')
    True
    >>>is_http_domain('https://ru.wikipedia.org/')
    True
    >>>is_http_domain('griddynamics.com')
    False
"""
import re


def is_http_domain(domain: str) -> bool:
    pattern=r'^(https?://)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/?$'

    if re.match(pattern,domain):
        return True
    else:
        return False


print(is_http_domain('http://wikipedia.org'))
print(is_http_domain('https://ru.wikipedia.org/'))

"""
write tests for is_http_domain function
"""

import unittest
from task_3 import is_http_domain

class TestIsHttpDomain(unittest.TestCase):
    def test_http_domain_with_slash(self):
        result=is_http_domain('http://wikipedia.org/')
        self.assertTrue(result)

    def test_https_domain_with_slash(self):
        result=is_http_domain('https://ru.wikipedia.org/')
        self.assertTrue(result)

    def test_http_domain_without_slash(self):
        result=is_http_domain('http://ggogle.com')
        self.assertTrue(result)

    def test_https_domain_without_slash(self):
        result=is_http_domain('https://example.org')
        self.assertTrue(result)

    def test_invalid_domain(self):
        result=is_http_domain('grid dynamics.com')
        self.assertFalse(result)
    
    def test_invalid_protocol(self):
        result=is_http_domain('ftp://example.com')
        self.assertFalse(result)

    def test_invalid_slash(self):
        result=is_http_domain('https://example.com//')
        self.assertFalse(result)

if __name__=="__main__":
    unittest.main()