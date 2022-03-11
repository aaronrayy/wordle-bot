from os import stat
from tracemalloc import start

def printout(l):
    print("     i found", len(l), "words that could help you :-)\n")
    i = 1
    for element in l:
        print("     " + str(i) + ": " + element)
        i += 1

def compare_letters(comp, guess):
    status = 0
    for i in range(5):
        # if ((guess.tags[i] == 'y') or (guess.tags[i] == 'm')) and (guess.w[i] in comp):
        #     status += 1
        if (guess.tags[i] == 'y') and (guess.w[i] == comp[i]):
            status += 1
        elif (guess.tags[i] == 'm') and (guess.w[i] in comp):
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
        if compare_letters(word, guess) and (word != guess.w):
            f.write(word + "\n")
            options.append(word)
    f.close
    return options