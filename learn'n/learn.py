import random

class laern:
    def __init__(self, layers, number_of_inputs, number_of_hidden_neurons, number_of_outputs, change):
        self.chang = change
        self.steps = layers
        self.innum = number_of_inputs
        self.hidnum = number_of_hidden_neurons
        self.outnum = number_of_outputs
        self.ins = []
        self.hids = []
        self.outs = []
        self.make_in()
        self.make_hid() #, self.outs
        self.final = [self.ins, self.hids]

    def redefine(self, final):
        self.final = final
    
    def revise(self):
        self.hids = self.final[1]
        self.remake_hid()
        #print(self.hids[0][0].inputs)
        return([self.ins, self.hids])

    def make_in(self):
        for i in range(self.innum):
            self.ins.append(i)
    
    def remake_hid(self):
        midlayers = self.steps - 1
        for runs in range(midlayers):
            if(runs == 0):
                innur = self.innum
            else:
                innur = self.hidnum
            if(runs == midlayers - 1):
                nurnum = self.outnum
            else:
                nurnum = self.hidnum
            for i in range(nurnum):
                if(random.randint(1, 100) < self.chang):
                    self.hids[runs][i] = self.hidsetup(innur)
                #elif(random.randint(1, 100) > self.chang):
                    #self.hids[runs][i] = neuron(fin[1][runs][i].inputs, fin[1][runs][i].weight, self.rancolor())

    def make_hid(self):
        midlayers = self.steps - 1
        for runs in range(midlayers):
            if(runs == 0):
                innur = self.innum
            else:
                innur = self.hidnum
            if(runs == midlayers - 1):
                self.hids.append([])
                nurnum = self.outnum
                for i in range(nurnum):
                    self.hids[runs].append(self.hidsetup(innur))
            else:
                self.hids.append([])
                nurnum = self.hidnum
                for i in range(nurnum):
                    self.hids[runs].append(self.hidsetup(innur))

    def hidsetup(self, innur):
        possins = []
        ins = []
        for x in range(innur):
            possins.append(x)
        for i in range(random.randint(1, innur)):
            choice = random.randint(0, len(possins) - 1)
            ins.append(possins[choice])
            del(possins[choice])
        weight = random.randint(len(ins) * -1, len(ins))
        while weight == 0:
            weight = random.randint(len(ins) * -1, len(ins))
        return(neuron(ins, weight, self.rancolor()))

    def rancolor(self):
        letter = ['A', 'B', 'C', 'D', 'E', 'F']
        color = []
        for i in range(6):
            num = random.randint(1, 15)
            if(num > 9):
                nums = num - 10
                color.append(letter[nums])
            else:
                color.append(str(num))
        return("#" + "".join(color))

    def save(self):
        with open('output.txt', 'w') as f:
            f.write(str(self.final))

class neuron:
    def __init__(self, inputs, weight, color):
        self.inputs = inputs
        self.weight = weight
        self.color = color
