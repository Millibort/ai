import learn

inst = 5
ai = []
newai = []

for i in range(inst):
    ai.append(learn.laern(5, 10, 15, 5, 25))
for i in range(inst):
    newai.append(ai[2].revise())
for i in range(inst):
    ai[i].redefine(newai[i])

class test:
    def __init__(self, input, out):
        self.input = input
        self.out = out



def run(net, tests):
    for x in range(len(net[1])):
        for y in range(len(net[1][x])):
            for z in range(len(net[1][x][y])):
                for i in range(len(net[1][x][y].inputs)):
