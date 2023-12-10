import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from services.password_validator import validate_password_strength

# for custom characters
def test_validate_strength_with_custom_chars():
    password = "abc123"
    custom_chars = "abc123"
    assert validate_password_strength(password, len(password), False, custom_chars)

# for passwords without custom characters
def test_validate_strength_without_custom_chars_basic():
    password = "abcdefgh"
    assert validate_password_strength(password, len(password), False)

# for strength validation
def test_validate_strength_without_custom_chars_advanced():
    password = "Abc1#efg"
    assert validate_password_strength(password, len(password), True)

# for passwords shorter than the length it needs to be
def test_validate_strength_fail_short_length():
    password = "short"
    assert not validate_password_strength(password, 10, False)

# for uppercase letters in advanced mode
def test_validate_strength_fail_no_uppercase():
    password = "abc1#efg"
    assert not validate_password_strength(password, len(password), True)

# for lack of digits in advanced mode
def test_validate_strength_fail_no_digit():
    password = "Abc#defg"
    assert not validate_password_strength(password, len(password), True)

# for lack of special characters in advanced mode
def test_validate_strength_fail_no_special_char():
    password = "Abc1defg"
    assert not validate_password_strength(password, len(password), True)