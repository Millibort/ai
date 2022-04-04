from tkinter import E
import learn
import graph
import random

from numpy import average

def findbiggest(list):
    x = 0
    for i in range(len(list)):
        if list[i] > list[x]:
            x = i
    return(x)

def main(inst, rounds, tests):
    global GScore
    ai = []
    best = 0

    for i in range(inst):
        ai.append(learn.laern(10, 25, 75, 3, 20))
    for z in range(rounds):
        for i in range(inst):
            if i != best:
                ai[i].redefine(ai[best].revise())
            #else:
                #print(i)
        scores = []
        for x in range(inst):
            tests_out = []
            for z in range(len(list_of_tests)):
                for i in range(len(list_of_tests[z].input)):
                    #print(list_of_tests[z].getin(i))
                    score = list_of_tests[z].score(run(ai[x].final, list_of_tests[z].getin(i)))
                    #print(score)
                    tests_out.append(score)
            scores.append(average(tests_out))
        best = findbiggest(scores)
        Graph_Best(scores[best])
        #print([scores[best], scores])
    print(scores[best])     
    GScore = scores[best]
    return(ai[best])

class test:
    def __init__(self, input, goal):
        self.input = input
        self.goal = goal
    
    def getin(self, num):
        return(self.input[num])
    
    def score(self, out):
        #print([findbiggest(self.goal), findbiggest(out)])
        if findbiggest(self.goal) == findbiggest(out):
            return(1)
        return(0)
        
list_of_tests = [test([[1,1,1,0,0, 1,1,1,0,0, 1,1,1,0,0, 0,0,0,0,0, 0,0,0,0,0], [0,0,0,0,0, 0,0,1,1,0, 0,0,1,1,0, 0,0,0,0,0, 0,0,0,0,0], [0,0,0,0,0, 0,0,0,0,0, 0,1,0,0,0, 0,0,0,0,0, 0,0,0,0,0], [0,0,1,1,1, 0,0,1,1,1, 0,0,1,1,1, 0,0,0,0,0, 0,0,0,0,0], [0,0,0,0,0, 0,0,0,0,0, 0,0,1,1,1, 0,0,1,1,1, 0,0,1,1,1], [0,0,0,0,0, 1,1,1,0,0, 1,1,1,0,0, 1,1,1,0,0, 0,0,0,0,0], [0,0,0,0,0, 0,0,1,1,1, 0,0,1,1,1, 0,0,1,1,1, 0,0,0,0,0], [0,0,0,0,0, 0,0,0,0,0, 0,1,1,0,0, 0,1,1,0,0, 0,0,0,0,0],  [0,0,0,0,0, 0,1,1,1,0, 0,1,1,1,0, 0,1,1,1,0, 0,0,0,0,0], [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 1,1,0,0,0, 1,1,0,0,0], [0,0,0,0,0, 0,0,0,0,0, 0,0,0,1,1, 0,0,0,1,1, 0,0,0,0,0]], [0,0,1]), test([[0,0,1,0,0, 0,1,1,1,0, 1,1,1,1,1, 0,0,0,0,0, 0,0,0,0,0], [0,0,0,0,0, 0,1,0,0,0, 1,1,1,0,0, 0,0,0,0,0, 0,0,0,0,0], [0,0,0,1,0, 0,0,1,1,1, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0], [0,0,0,0,0, 0,0,0,0,0, 0,0,1,1,0, 0,1,1,1,0, 1,1,1,1,1], [0,0,0,0,0, 0,0,0,0,0, 0,0,0,1,0, 0,0,1,1,1, 0,0,0,0,0], [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,1,0,0, 0,1,1,1,0], [0,0,0,0,0, 0,1,0,0,0, 1,1,1,0,0, 0,0,0,0,0, 0,0,0,0,0], [0,0,0,0,0, 0,0,1,0,0, 0,1,1,1,0, 1,1,1,1,1, 0,0,0,0,0], [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,1,0,0,0, 1,1,1,0,0], [0,0,0,0,0, 0,1,0,0,0, 1,1,1,0,0, 0,0,0,0,0, 0,0,0,0,0], [0,0,0,0,0, 0,0,0,0,0, 0,0,1,0,0, 0,1,1,1,0, 0,0,0,0,0]], [0,1,0]), test([[0,0,1,0,0, 0,1,1,1,0, 1,1,1,1,1, 0,1,1,1,0, 0,0,1,0,0], [0,0,1,0,0, 0,1,1,1,0, 0,0,1,0,0, 0,0,0,0,0, 0,0,0,0,0], [0,0,0,1,0, 0,0,1,1,1, 0,0,0,1,0, 0,0,0,0,0, 0,0,0,0,0], [0,0,0,0,0, 0,1,0,0,0, 1,1,1,0,0, 0,1,0,0,0, 0,0,0,0,0], [0,0,0,0,0, 0,0,0,0,0, 0,0,0,1,0, 0,0,1,1,1, 0,0,0,1,0], [0,0,0,0,0, 0,0,1,0,0, 0,1,1,1,0, 0,0,1,0,0, 0,0,0,0,0], [0,1,0,0,0, 1,1,1,0,0, 0,1,0,0,0, 0,0,0,0,0, 0,0,0,0,0], [0,0,0,0,0, 0,0,0,0,0, 0,0,0,1,0, 0,0,1,1,1, 0,0,0,1,0],[0,0,0,0,0, 0,0,0,0,0, 0,1,0,0,0, 1,1,1,0,0, 0,1,0,0,0], [0,0,0,1,0, 0,0,1,1,1, 0,0,0,1,0, 0,0,0,0,0, 0,0,0,0,0], [0,0,0,0,0, 0,0,1,0,0, 0,1,1,1,0, 0,0,1,0,0, 0,0,0,0,0]], [1,0,0])]

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
                tempneruos.append(neruoins / net[1][x][y].weight)
        neruos.append(tempneruos)
    return(neruos[len(neruos) - 1])

def Graph_Best(best):
    global EX
    EX = EX + 5
    y = round(best * 100)
    print(EX,y)
    graph.bob.pendown()
    graph.bob.goto(EX, y)
    graph.bob.penup()

graph.bob.speed(0)
graph.bob.penup()
EX = -500
graph.bob.goto(EX, 50)

GScore = 0
#while GScore < .89:
net = main(5, 200, len(list_of_tests[0].input))
net.save()

#for i in range(15):
    #inpu = input("0,0,0,0,0\n0,1,1,1,0\n0,1,1,1,0\n0,1,1,1,0\n0,0,0,0,0\n")
    #print(average([list_of_tests[0].score(run(net.final, list_of_tests[0].getin())), list_of_tests[0].score(run(net.final, list_of_tests[0].getin())), list_of_tests[0].score(run(net.final, list_of_tests[0].getin())), list_of_tests[1].score(run(net.final, list_of_tests[0].getin())), list_of_tests[1].score(run(net.final, list_of_tests[0].getin())), list_of_tests[1].score(run(net.final, list_of_tests[0].getin()))]))
a = run(net.final, list_of_tests[0].getin(1))
b = run(net.final, list_of_tests[0].getin(2))
c = run(net.final, list_of_tests[1].getin(1))
d = run(net.final, list_of_tests[1].getin(2))
e = run(net.final, list_of_tests[2].getin(1))
f = run(net.final, [0,0,0,0,0, 0,0,0,0,0, 0,0,0,1,0, 0,0,1,1,1, 0,0,0,1,0])

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

print(list_of_tests[0].score(a))
print(list_of_tests[0].score(b))
print(list_of_tests[1].score(c))
print(list_of_tests[1].score(d))
print(list_of_tests[2].score(e))
print(list_of_tests[2].score(f))