import random

def load_words(file_path):
    with open(file_path, 'r') as file:
        words = file.readlines()

    words = [word.strip() for word in words] # remove newline characters]
    return words

def select_random_word(words):
    return random.choice(words)

