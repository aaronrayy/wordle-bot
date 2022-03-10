class word:
    words = []
    f = open("data.txt")

    for line in f:
        s = line.replace("\n", "")
        words.append(s)

class guess:
    def __init__(self, g, n):
        self.w = g
        self.num_in = n
    w = ""
    letters = []
    tags = []
    num_in = 0