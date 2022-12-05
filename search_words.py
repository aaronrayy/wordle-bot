from math import fabs
from os import stat
from tracemalloc import start

#function that prints out a given output list of matching words. called in main.py
def printout(l):
    print("     i found", len(l), "words that could help you :-)\n")
    i = 1
    for element in l:
        print("     " + str(i) + ": " + element)
        i += 1

def check_ys(comp, guess):
    status = 0
    for i in range(5):
        if (guess.tags[i] == 'y') and ((guess.w)[i] == comp[i]):
            status += 1
    if status == guess.num_y:
        return True
    return False

def check_ms(comp, guess):
    status = 0
    for i in range(5):
        if (guess.tags[i] == 'm') and (guess.w[i] in comp) and ((guess.w)[i] != comp[i]):
            status += 1
    if status == guess.num_m:
        return True
    return False

def check_ns(comp, guess):
    for i in range(5):
        if (guess.tags[i] == 'n') and ((guess.w)[i] in comp):
            return False
    return True

def search(bank, options, guess, step):
    """
    searches through a word list given a word and status tags
        bank --> a list
        guess --> an instance of the guess class. contains the guess itself, list of status tags, and number of letters in the guess that are in the word
    returns a list of possible words that match the given tags
    """
    #options = []
    temp = []
    temp2 = []
    f = open("output.txt", "w")

    if step < 1:
        for word in bank:
            if check_ns(word, guess):
                temp.append(word)
    else:
        for word in options:
            if check_ns(word, guess):
                temp.append(word)
    
    for word in temp:
        if check_ys(word, guess):
            temp2.append(word)

    if (guess.num_m == 0):
        for word in temp2:
            f.write(word + "\n")
            # options.append(word)
        # f.close
        return temp2
    else:
        for word in temp2:
            if check_ms(word, guess):
                f.write(word + "\n")
                # options.append(word)
        # f.close
        return temp2