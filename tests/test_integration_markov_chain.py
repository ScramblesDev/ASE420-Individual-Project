import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.password_generator import generate_password

def test_markov_chain_integration():
    length = 10
    use_advanced = False
    strength = 'medium'
    pronounceable = True

    password = generate_password(length, use_advanced, strength, pronounceable)
    assert len(password) == length
    assert password.islower()
