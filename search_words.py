from os import stat
from tracemalloc import start


import wordModule

def compare_letters(comp, guess):
    status = 0
    for i in range(5):
        if (guess.letters)[i] in comp:
            status += 1
    if status == guess.num_in:
        return True
    else:
        return False

def search(bank, guess):
    """
    searches through a word list given a word and status tags
        bank --> a list
        guess --> an instance of the guess class. contains the guess itself, list of status tags, and number of letters in the guess that are in the word
    returns a list of possible words that match the given tags
    """
    options = []
    for word in bank:
        if compare_letters(word, guess):
            options.append(word)
    return options