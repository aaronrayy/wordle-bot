from os import stat
from tracemalloc import start

def compare_letters(comp, guess):
    status = 0
    # for i in range(5):
    #     if (guess.letters)[i] in comp:
    #         print("i: ", i, "\n   ", (guess.letters)[i], "\n   ", comp)
    #         status += 1

    # if status == guess.num_in:
    #     return True
    # else:
    #     return False
    # c = list(comp)
    # print("comp: ", c)
    # print("   guess: ", guess.letters)
    # if all(x in guess.letters for x in list(comp)):
    #     return True
    # else:
    #     return False
    for i in range(len(guess.letters)):
        if comp.find(guess.letters[i]) > 0:
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
    f = open("output.txt", "w")
    for word in bank:
        if compare_letters(word, guess):
            f.write(word)
            f.write("\n")
            options.append(word)
    return options