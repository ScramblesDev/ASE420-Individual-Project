import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.markov_chain import generate_pronounceable_password

def test_markov_chain_regression():
    length = 8
    characters = 'abcdef'

    password = generate_pronounceable_password(length, characters)

    assert len(password) == length