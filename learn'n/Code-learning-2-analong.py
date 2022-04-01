import learn
import graph
import random

from numpy import average

def findbiggest(list):
    x = 0
    for i in range(len(list)):
        if i != len(list) - 1:
            if list[i + 1] > list[i]:
                x = i + 1
            elif list[i + 1] == list[i]:
                rand = random.randint(0, 2)
                if rand == 0:
                    x = i
                elif rand == 1:
                    x = i + 1
            else:
                x = i
    return(x)

def main(inst, rounds):
    global GScore
    ai = []
    newai = []
    best = 0

    for i in range(inst):
        ai.append(learn.laern(10, 25, 50, 3, 25))
    for z in range(rounds):
        for i in range(inst):
            newai.append(ai[best].revise())
        for i in range(inst):
            ai[i].redefine(newai[i])
        scores = []
        for x in range(inst):
            scores.append(average([list_of_tests[0].score(run(ai[x].final, list_of_tests[0].getin())), list_of_tests[0].score(run(ai[x].final, list_of_tests[0].getin())), list_of_tests[0].score(run(ai[x].final, list_of_tests[0].getin())), list_of_tests[0].score(run(ai[x].final, list_of_tests[0].getin())),  list_of_tests[1].score(run(ai[x].final, list_of_tests[1].getin())), list_of_tests[1].score(run(ai[x].final, list_of_tests[1].getin())), list_of_tests[1].score(run(ai[x].final, list_of_tests[1].getin())), list_of_tests[1].score(run(ai[x].final, list_of_tests[1].getin()))]))
        best = findbiggest(scores)
    print(scores[best])
    GScore = scores[best]
    return(ai[best])

class test:
    def __init__(self, input, goal):
        self.input = input
        self.goal = goal
    
    def getin(self):
        return(random.choice(self.input))
    
    def score(self, out):
        score = 0
        if findbiggest(self.goal) == findbiggest(out):
            score = 1
        return(score)
        
list_of_tests = [test([[0,0,0,0,0, 0,1,1,1,0, 0,1,1,1,0, 0,1,1,1,0, 0,0,0,0,0], [0,0,0,0,0, 0,0,0,0,0, 0,0,1,1,1, 0,0,1,1,1, 0,0,1,1,1], [1,1,1,0,0, 1,1,1,0,0, 1,1,1,0,0, 0,0,0,0,0, 0,0,0,0,0], [0,0,0,0,0, 1,1,1,0,0, 1,1,1,0,0, 1,1,1,0,0, 0,0,0,0,0], [0,0,1,1,1, 0,0,1,1,1, 0,0,1,1,1, 0,0,0,0,0, 0,0,0,0,0], [0,1,1,1,0, 0,1,1,1,0, 0,1,1,1,0, 0,0,0,0,0, 0,0,0,0,0], [0,0,0,0,0, 0,0,0,0,0, 0,1,1,1,0, 0,1,1,1,0, 0,1,1,1,0]], [0,0,1]), test([[0,0,0,0,0, 0,0,0,0,0, 0,0,1,0,0, 0,1,1,1,0, 1,1,1,1,1], [0,0,1,0,0, 0,1,1,1,0, 1,1,1,1,1, 0,0,0,0,0, 0,0,0,0,0], [0,0,0,0,0, 0,0,1,0,0, 0,1,1,1,0, 1,1,1,1,1, 0,0,0,0,0], [0,0,0,0,1, 0,0,0,1,1, 0,0,1,1,1, 0,1,1,1,1, 1,1,1,1,1], [1,0,0,0,0, 1,1,0,0,0, 1,1,1,0,0, 1,1,1,1,0, 1,1,1,1,1], [0,0,1,0,0, 0,0,1,1,0, 0,0,1,1,1, 0,0,0,0,0, 0,0,0,0,0]], [0,1,0])]

def run(net, tests):
    neruos = []
    for x in range(len(net[1])):
        tempneruos = []
        for y in range(len(net[1][x])):
                neruoins = 0
                for i in range(len(net[1][x][y].inputs)):
                    if x == 0:
                            neruoins = neruoins + tests[net[1][x][y].inputs[i]]
                    else:
                            neruoins = neruoins + neruos[x - 1][net[1][x][y].inputs[i]]
                tempneruos.append(neruoins / net[1][x][y].weight / len(net[1][x][y].inputs))
        neruos.append(tempneruos)
    return(neruos[len(neruos) - 1])

GScore = 0
while GScore < .89:
    net = main(200, 500)
net.save()
print(net.final)