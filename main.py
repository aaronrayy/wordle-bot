from os import stat
import wordModule
import search_words

#instance of word module word class
w = wordModule.word()

print("hello.\n   enter a word to check if its in the word list\n      type 'q' at any time to exit\n")

#main loop
while(1):
    #user guess the program will use
    start_word = input("enter word: ")

    #checks if user guess is valid (5 letters, and in the word bank)
    if (len(start_word) == 5) and (start_word in w.words):
        #instance of word module guess class
        curr = wordModule.guess(start_word, 0)
        curr.letters = list(start_word)
        
        #string representing status of letters in the guess (from wordle)
        results = input("\n     now enter the status of each letter.\n          y --> letter is in the word and in the right spot\n          n --> letter is not in the word at all\n          m --> letter is in the word, but not in the right spot\n\n          enter as one complete string: ")
        results = list(results)
        #adds tag data to 'curr' instance of tags list
        for i in range(5):
            if (results[i] == 'y') or (results[i] == 'm'):
                curr.tags.append(results[i])
                curr.num_in += 1
            else:
                curr.tags.append("n")

        #searches for matching words in word bank
        print("searching for matching word...")

        options = search_words.search(w.words, curr)
        print(options)

    #checks for quit command
    elif start_word == 'q':
        print("exiting now")
        break
    #guess was not valid. restart loop
    else:
        print("invalid input. please try again")

