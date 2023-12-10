import random
from collections import defaultdict

english_words_set = {"apple", "banana", "cherry", "date", "elephant", "fig", "grape"}

def generate_pronounceable_password(length, characters):
    markov_chain = build_markov_chain(english_words_set)
    password = ''

    while len(password) < length:
        word = generate_markov_word(markov_chain, length - len(password))
        if characters:
            word = map_to_custom_characters(word, characters)
        password += word

    return password[:length]

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

def map_to_custom_characters(word, custom_chars):
    mapped = ''
    for char in word:
        if char in custom_chars:
            mapped += char
        else:
            # this basically just maps to the closest character in custom set
            mapped += min(custom_chars, key=lambda c: abs(ord(c) - ord(char)))
    return mapped