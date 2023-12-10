import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.password_generator import generate_password
from src.password_validator import validate_password_strength

def test_password_generator_integration():
    length = 12
    use_advanced = True
    strength = 'high'
    pronounceable = False

    password = generate_password(length, use_advanced, strength, pronounceable)
    is_valid = validate_password_strength(password, length, use_advanced)

    print(f"Generated password: {password}")

    assert len(password) == length
    assert is_valid, "Password validation failed, possibly due to not meeting character type criteria"

