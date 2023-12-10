import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from services.markov_chain import generate_pronounceable_password, build_markov_chain

# if Markov chain is built correctly from a set of words
def test_build_markov_chain():
    words_set = {"test", "python", "markov"}
    chain = build_markov_chain(words_set)
    assert isinstance(chain, dict)
    assert all(key in "testpythonmarkov" for key in chain.keys())

# if the generated password has the correct length
def test_generate_pronounceable_password_length():
    length = 10
    characters = 'abcdefghijklmnopqrstuvwxyz'
    password = generate_pronounceable_password(length, characters)
    assert len(password) == length

# if the generated password contains only the specified characters
def test_generate_pronounceable_password_characters():
    length = 10
    characters = 'abcd'
    password = generate_pronounceable_password(length, characters)
    assert all(char in characters for char in password)