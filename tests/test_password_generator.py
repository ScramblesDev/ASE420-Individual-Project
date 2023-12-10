import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from services.password_generator import generate_password, generate_random_password, generate_high_strength_password

# if the generated password has the correct length
def test_generate_password_length():
    length = 10
    password = generate_password(length, False, 'medium', False)
    assert len(password) == length

# if the custom characters are used
def test_generate_password_custom_chars():
    custom_chars = 'abcd1234'
    length = 10
    password = generate_password(length, False, 'medium', False, custom_chars)
    assert all(char in custom_chars for char in password)

# for the low strength
def test_generate_random_password_low_strength():
    length = 10
    characters = 'abcd1234'
    password = generate_random_password(length, characters, 'low')
    assert len(password) == length
    assert all(char in characters for char in password)

# for the high strength
def test_generate_random_password_high_strength():
    length = 10
    characters = 'abcd1234'
    password = generate_random_password(length, characters, 'high')
    assert len(password) == length
    assert all(char in characters for char in password)

# tests that no consecutive characters are the same in high strength password
def test_generate_high_strength_password_no_repetition():
    length = 10
    characters = 'abcd1234'
    password = generate_high_strength_password(characters, length)
    assert len(password) == length
    for i in range(len(password) - 1):
        assert password[i] != password[i + 1]