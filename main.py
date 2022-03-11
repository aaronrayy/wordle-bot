from os import stat
from tabnanny import check
import word_module
import search_words

#function to check if the inputted status tags string is valid
def check_tags(l):
    for i in range(len(l)):
        if (l[i] != 'y') and (l[i] != 'm') and (l[i] != 'n'):
            return True
    return False

#instance of word module word class
w = word_module.word()

# print(w.words)
# print()
# print(len(w.words))


print("hello. i will help you play wordle.\n   enter a word to check if its in the word list\n   you may type 'q' at any time to exit")
#main loop
while(1):
    #user guess the program will use
    start_word = input("\n   enter word: ")

    #checks if user guess is valid (5 letters, and in the word bank)
    if (len(start_word) == 5) and (start_word in w.words):
        #instance of word module guess class
        curr = word_module.guess(start_word, 0)
        #curr.letters = list(start_word)
        
        #string representing status of letters in the guess (from wordle)
        print("\n     great!\n     now enter the status of each letter.\n          y --> letter is IN the word and in the right spot\n          m --> letter is IN the word, but not in the right spot\n          n --> letter is NOT IN the word at all\n\n                            your guess:", curr.w)
        results = input("          enter as one complete string: ")
        results = list(results)
        #error checking for status tags input. skips over and restarts loop if input is less than 5, greater than 5, or does not contain exclusively 'y', 'm', and 'n'
        if (len(results) < 5) or (len(results) > 5) or check_tags(results):
            print("\n          --invalid status input. try again.--\n")
            continue
        
        #adds tag data to curr's tags list
        for i in range(5):
            if (results[i] == 'y') or (results[i] == 'm'):
                curr.tags.append(results[i])
                curr.letters.append(start_word[i])
                curr.num_in += 1
            else:
                curr.tags.append("n")

        #searches for matching words in word bank
        print(" searching for matching words...\n")
        #print("check output file :-)")

        options = search_words.search(w.words, curr)

        #print("tags: ", curr.tags)
        #print(options)
        search_words.printout(options)
        #print("num in: ", curr.num_in)
    #checks for quit command
    elif start_word == 'q':
        print("\n" + ("  --exiting now. goodbye--\n".center(46)))
        break
    #guess was not valid. restart loop
    else:
        print(" --invalid input. please try again--\n")



