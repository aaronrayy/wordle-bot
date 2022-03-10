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
