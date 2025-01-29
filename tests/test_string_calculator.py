import pytest
from string_calculator import add

#Empty string returns 0 test case
def test_empty_string():
    assert add("")==0

#Test case for two numbers
def test_two_numbers():
    assert add("1,2")==3

#Test case for handling multiple numbers
def test_multiple_numbers():
    assert add("1,2,3,4")==10

#Test case for handling newlines as delimiters
def test_newline_delimiter():
    assert add("1\n2,3")==6

#Test case for supporting custom delimiters
def test_custom_delimiters():
    assert add("//;\n1;2")==3