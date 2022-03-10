# wordle-bot
INTRODUCTION
    project to play wordle in an efficient and smart manner. slightly based on 3blue1brown's video

    users input starting word for the wordle and the wordle letter results. for example:
        starting word: 'hello'
        input: h-X,e-X,l-X,l-X,o-X
            where X = {
                y --> letter is in the word and in the right spot
                n --> letter is not in the word at all
                m --> letter is in the word, but not in the right spot
            }

    the word bank comes from
        https://www.bestwordlist.com/5letterwords.htm 
    its a list of apparently all of the 12,478 5-letter english words. since there were 15 pages of the list, i copied and pasted them into a txt file in the source files (data.txt), which is read and input into a word bank using the list type in word_module.py