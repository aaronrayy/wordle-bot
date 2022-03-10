class word:
    words = []
    f = open("data.txt")

    for line in f:
        s = line.replace("\n", "")
        words.append(s)

class guess:
    def __init__(self, g):
        self.w = g
    w = ""
    tags = []