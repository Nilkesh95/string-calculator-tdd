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

#Test case for handling negative numbers
def test_negative_numbers():
    with pytest.raises(ValueError,match="negatives not allowed: -1,-3"):
        add("1,-1,2,-3")

#Test case for ignoring numbers>1000
def test_ignore_large_numbers():
    assert add("2,1001")==2

#Test case for supporting multi-charcter delimiters
def test_multi_char_delimiters():
    assert add("//[***]\n1***2***3")==6