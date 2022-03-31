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
    ai = []
    newai = []
    best = 0

    for i in range(inst):
        ai.append(learn.laern(5, 25, 50, 3, 25))
    for z in range(rounds):
        for i in range(inst):
            newai.append(ai[best].revise())
        for i in range(inst):
            ai[i].redefine(newai[i])
        scores = []
        for x in range(inst):
            scores.append(average([list_of_tests[0].score(run(ai[x].final, list_of_tests[0].getin())), list_of_tests[0].score(run(ai[x].final, list_of_tests[0].getin())), list_of_tests[0].score(run(ai[x].final, list_of_tests[0].getin())), list_of_tests[0].score(run(ai[x].final, list_of_tests[0].getin()))]))
        best = findbiggest(scores)
    print(scores[best])
    return(ai[best])

class test:
    def __init__(self, input, goal):
        self.input = input
        self.goal = goal
    
    def getin(self):
        return(random.choice(self.input))
    
    def score(self, out):
        score = 0
        for i in range(len(self.goal)):
            if out[i] == self.goal[i]:
                score = score + 1
        return(score)
        
list_of_tests = [test([[0,0,0,0,0, 0,1,1,1,0, 0,1,1,1,0, 0,1,1,1,0, 0,0,0,0,0], [0,0,0,0,0, 0,0,0,0,0, 0,0,1,1,1, 0,0,1,1,1, 0,0,1,1,1], [1,1,1,0,0, 1,1,1,0,0, 1,1,1,0,0, 0,0,0,0,0, 0,0,0,0,0], [0,0,0,0,0, 1,1,1,0,0, 1,1,1,0,0, 1,1,1,0,0, 0,0,0,0,0], [0,0,1,1,1, 0,0,1,1,1, 0,0,1,1,1, 0,0,0,0,0, 0,0,0,0,0], [0,1,1,1,0, 0,1,1,1,0, 0,1,1,1,0, 0,0,0,0,0, 0,0,0,0,0], [0,0,0,0,0, 0,0,0,0,0, 0,1,1,1,0, 0,1,1,1,0, 0,1,1,1,0]], [0,0,1]), test([[1,0,1,1,0,1,1,1,0,0], [1,1,1,0,0,1,0,1,1,0]], [0,1])]

def run(net, tests):
    neruos = []
    for x in range(len(net[1])):
        tempneruos = []
        for y in range(len(net[1][x])):
                neruoins = 0
                for i in range(len(net[1][x][y].inputs)):
                    if x == 0:
                        if tests[net[1][x][y].inputs[i]] == 1:
                            neruoins = neruoins + 1
                    else:
                        if neruos[x - 1][net[1][x][y].inputs[i]] == 1:
                            neruoins = neruoins + 1
                if neruoins >= net[1][x][y].weight:
                    tempneruos.append(1)
                else:
                    tempneruos.append(0)
        neruos.append(tempneruos)
    return(neruos[len(neruos) - 1])

#tests = learn.laern(5, 4, 10, 5, 50)
#print(run(tests.final, list_of_tests[0].getin()))
#print()
#print(tests.final)
net = main(50, 50)
net.save()
#graph.disp(net, False, 750, True)
print(net.final)