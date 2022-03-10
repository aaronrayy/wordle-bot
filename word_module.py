class word:
    words = []

    f = open("data.txt")

    for line in f:
        s = line.split()
        for word in s:
            a = word.lower()
            words.append(a)
    
    f.close

class guess:
    def __init__(self, g, n):
        self.w = g
        self.num_in = n
    w = ""
    letters = []
    tags = []
    num_in = 0