import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.password_generator import generate_password

def test_generate_password_regression():
    length = 10
    use_advanced = True
    strength = 'medium'
    pronounceable = False

    password = generate_password(length, use_advanced, strength, pronounceable)

    assert len(password) == length
    assert any(char.isdigit() for char in password)