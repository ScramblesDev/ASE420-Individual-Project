import random
import string

english_words_set = {"apple", "banana", "cherry", "date", "elephant", "fig", "grape"}

def generate_password(length, use_advanced, strength, pronounceable):
    if pronounceable:
        return generate_pronounceable_password(length)
    else:
        return generate_random_password(length, use_advanced, strength)

def generate_random_password(length, use_advanced, strength):
    characters = string.ascii_lowercase
    if use_advanced:
        characters += string.ascii_uppercase + string.digits + string.punctuation
    if strength == 'low':
        return ''.join(random.choices(characters, k=length))
    elif strength == 'medium':
        return ''.join(random.sample(characters, k=length))
    else:  # high strength
        return ''.join(random.SystemRandom().choice(characters) for _ in range(length))

def generate_pronounceable_password(length):
    word = ''
    while len(word) < length:
        word += random.choice(list(english_words_set))
    return word[:length]

