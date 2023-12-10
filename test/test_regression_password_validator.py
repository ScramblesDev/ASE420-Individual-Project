import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.password_validator import validate_password_strength

def test_password_validator_regression():
    password = "ValidPass123!"
    assert validate_password_strength(password, len(password), True)

    invalid_password = "invalid"
    assert not validate_password_strength(invalid_password, len(invalid_password), True)