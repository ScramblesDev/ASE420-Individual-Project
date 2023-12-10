import random
import string
import math
from collections import defaultdict

english_words_set = {"apple", "banana", "cherry", "date", "elephant", "fig", "grape"}

def generate_password(length, use_advanced, strength, pronounceable, custom_chars=None):
    if custom_chars:
        # so if a custom character set is provided, just use it directly
        characters = ''.join(set(custom_chars))  # this removes duplicates
        # we're gonna skip strength validation for custom character sets
        password = generate_random_password(length, characters, 'low')
    else:
        characters = get_characters(use_advanced)
        password = generate_random_password(length, characters, strength)

    if pronounceable:
        password = generate_pronounceable_password(length)

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

def generate_pronounceable_password(length):
    markov_chain = build_markov_chain(english_words_set)
    return generate_markov_word(markov_chain, length)

def build_markov_chain(words_set):
    markov_chain = defaultdict(list)
    for word in words_set:
        word = word.lower()
        for char, next_char in zip(word, word[1:]):
            markov_chain[char].append(next_char)
    return markov_chain

def generate_markov_word(markov_chain, length):
    word = random.choice(list(markov_chain.keys()))
    while len(word) < length:
        if word[-1] in markov_chain:
            word += random.choice(markov_chain[word[-1]])
        else:
            break
    return word[:length]

def validate_password_strength(password, length, use_advanced, custom_chars=None):
    if len(password) < length:
        return False

    if custom_chars:
        # when we're using custom characters, just check if the password contains only those characters
        return all(char in custom_chars for char in password)

    if use_advanced:
        # this is basically for advanced passwords. it's gonna check for the inclusion of various character types
        return (any(c.isupper() for c in password) and 
                any(c.isdigit() for c in password) and 
                any(c in string.punctuation for c in password))

    return True  # basic validation passed

def calculate_entropy(password):
    # this gives us a rough estimate of the entropy
    char_space = len(set(password))
    return math.log2(char_space ** len(password))