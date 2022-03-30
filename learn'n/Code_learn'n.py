import learn
import graph
import random

def main(inst):
    ai = []
    newai = []

    for i in range(inst):
        ai.append(learn.laern(5, 10, 15, 5, 25))
    for i in range(inst):
        newai.append(ai[2].revise())
    for i in range(inst):
        ai[i].redefine(newai[i])

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
        
list_of_tests = [test([[1,0,1,1], [1,1,1,0]], [0,1])]

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

tests = learn.laern(5, 4, 10, 2, 50)
print(list_of_tests[0].score(run(tests.final, list_of_tests[0].getin())))
#print(tests.final)
#graph.disp(tests, True, 500, True)