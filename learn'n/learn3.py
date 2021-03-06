import random

class laern:
    def __init__(self, layers, number_of_inputs, number_of_hidden_neurons, number_of_outputs, change, revisions):
        self.revs = revisions
        self.chang = change
        self.steps = layers
        self.innum = number_of_inputs
        self.hidnum = number_of_hidden_neurons
        self.outnum = number_of_outputs
        self.ins = []
        self.hids = []
        self.outs = []
        self.make_in()
        self.make_hid()
        self.final = [self.ins, self.hids, self.outs]
        for revs in range(self.revs):
            self.hids = self.final[1]
            self.outs = self.final[2]
            self.remake_hid()
            self.final = [self.ins, self.hids, self.outs]

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
                for i in range(nurnum):
                    if(random.randint(1, 100) > self.chang):
                        self.outs[i] = self.hidsetup(innur)
            else:
                nurnum = self.hidnum
                for i in range(nurnum):
                    if(random.randint(1, 100) > self.chang):
                        self.hids[runs][i] = self.hidsetup(innur)

    def make_hid(self):
        midlayers = self.steps - 1
        for runs in range(midlayers):
            if(runs == 0):
                innur = self.innum
            else:
                innur = self.hidnum
            if(runs == midlayers - 1):
                nurnum = self.outnum
                for i in range(nurnum):
                    self.outs.append(self.hidsetup(innur))
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
        weight = random.randint(1, len(ins))
        return(ins,weight,False)

    def save(self):
        with open('output.txt', 'w') as f:
            f.write(str(self.final))