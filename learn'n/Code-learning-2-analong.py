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

def main(inst, rounds, tests):
    global GScore
    ai = []
    newai = []
    best = 0

    for i in range(inst):
        ai.append(learn.laern(20, 25, 75, 3, 25))
    for z in range(rounds):
        for i in range(inst):
            newai.append(ai[best].revise())
        for i in range(inst):
            ai[i].redefine(newai[i])
        scores = []
        for x in range(inst):
            tests_out = []
            for i in range(tests):
                for z in range(len(list_of_tests)):
                    tests_out.append(list_of_tests[z].score(run(ai[x].final, list_of_tests[z].getin())))
            scores.append(average(tests_out))
        best = findbiggest(scores)
        while best == 0.5:
            scores.pop(best)
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
        #print([findbiggest(self.goal), findbiggest(out)])
        if findbiggest(self.goal) == findbiggest(out):
            return(1)
        return(0)
        
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
                            #print(round(neruoins / net[1][x][y].weight / len(net[1][x][y].inputs), 2))
                tempneruos.append(neruoins / net[1][x][y].weight)
        neruos.append(tempneruos)
    return(neruos[len(neruos) - 1])

GScore = 0
#while GScore < .89:
net = main(50, 100, len(list_of_tests[0].input))
net.save()
#for i in range(15):
    #inpu = input("0,0,0,0,0\n0,1,1,1,0\n0,1,1,1,0\n0,1,1,1,0\n0,0,0,0,0\n")
    #print(average([list_of_tests[0].score(run(net.final, list_of_tests[0].getin())), list_of_tests[0].score(run(net.final, list_of_tests[0].getin())), list_of_tests[0].score(run(net.final, list_of_tests[0].getin())), list_of_tests[1].score(run(net.final, list_of_tests[0].getin())), list_of_tests[1].score(run(net.final, list_of_tests[0].getin())), list_of_tests[1].score(run(net.final, list_of_tests[0].getin()))]))
a = run(net.final, list_of_tests[0].getin())
b = run(net.final, list_of_tests[0].getin())
c = run(net.final, list_of_tests[1].getin())
d = run(net.final, list_of_tests[1].getin())

print(a)
print(b)
print(c)
print(d)

print(list_of_tests[0].score(a))
print(list_of_tests[0].score(b))
print(list_of_tests[1].score(c))
print(list_of_tests[1].score(d))