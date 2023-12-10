import math
import random
import string
from . import password_validator as pv
from . import markov_chain as mc

def generate_password(length, use_advanced, strength, pronounceable, custom_chars=None):
    characters = ''.join(set(custom_chars)) if custom_chars else get_characters(use_advanced)
    password = ''

    if pronounceable:
        password = mc.generate_pronounceable_password(length, characters)
    else:
        password = generate_random_password(length, characters, strength)

    return password

def generate_random_password(length, characters, strength):
    if strength == 'low':
        return ''.join(random.choices(characters, k=length))
    elif strength == 'medium':
        return ''.join(random.sample(characters, k=min(len(characters), length)))
    else:  # high strength
        return generate_high_strength_password(characters, length)

def generate_high_strength_password(characters, length):
    password = []
    while len(password) < length:
        char = random.SystemRandom().choice(characters)
        if len(password) == 0 or password[-1] != char:
            password.append(char)
    return ''.join(password)

def get_characters(use_advanced):
    characters = string.ascii_lowercase
    if use_advanced:
        characters += string.ascii_uppercase + string.digits + string.punctuation
    return characters

def get_custom_characters(custom_chars):
    return ''.join(set(custom_chars))  # I'm gonna add this in so that duplicates are removed

def calculate_entropy(password):
    char_space = len(set(password))
    return math.log2(char_space ** len(password))