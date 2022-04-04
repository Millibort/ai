import turtle
import tkinter
import learn
bob = turtle.Turtle()
bob.hideturtle()

def disp(laern, text, space, coloured_dots):
    neghalf = (space / 2) * -1
    bob.speed(0)
    bob.penup()
    test = laern
    widths = []
    wid = space / test.steps
    step = neghalf + wid / 2
    for i in range(int(test.steps)):
        widths.append(step)
        step = step + wid

    inp = []
    inpu = space / test.innum
    step = neghalf + inpu / 2
    for i in range(int(test.innum)):
        inp.append(step)
        step = step + inpu

    hid = []
    hidd = space / test.hidnum
    step = neghalf + hidd / 2
    for i in range(int(test.hidnum)):
        hid.append(step)
        step = step + hidd

    out = []
    outp = space / test.outnum
    step = neghalf + outp / 2
    for i in range(int(test.outnum)):
        out.append(step)
        step = step + outp

    for x in range(len(test.final[1])):
        for z in range(len(test.final[1][x])):
            for y in range(len(test.final[1][x][z].inputs)):
                if(coloured_dots):
                    circ(widths[x + 1], hid[z], test.final[1][x][z].color)
                bob.color(test.final[1][x][z].color)
                bob.goto(widths[x + 1], hid[z])
                bob.pendown()
                if x == 0:
                    bob.goto(widths[x], inp[test.final[1][x][z].inputs[y]])
                else:
                    bob.goto(widths[x], hid[test.final[1][x][z].inputs[y]])
                bob.penup()
            if(text):
                bob.goto(widths[x + 1], hid[z] - 25)
                bob.color("black")
                bob.write(str(test.final[1][x][z].inputs), True, align="center")
                bob.goto(widths[x + 1], hid[z] - 40)
                bob.write(str(test.final[1][x][z].weight), True, align="center")
    
    for z in range(len(test.final[2])):
        for y in range(len(test.final[2][z].inputs)):
            if(coloured_dots):
                circ(widths[len(widths) - 1], out[z], test.final[2][z].color)
            bob.goto(widths[len(widths) - 1], out[z])
            bob.color(test.final[2][z].color)
            bob.pendown()
            bob.goto(widths[len(widths) - 2], hid[test.final[2][z].inputs[y]])
            bob.penup()
        if(text):
            bob.goto(widths[len(widths) - 1], out[z] - 25)
            bob.color("black")
            bob.write(str(test.final[2][z].inputs), True, align="center")
            bob.goto(widths[len(widths) - 1], out[z] - 40)
            bob.write(str(test.final[2][z].weight), True, align="center")

    for i in range(len(inp)):
        circ(widths[0], inp[i], "#000000")

    if(coloured_dots == False):
        run = 1
        while run < len(widths) - 1:
            for i in range(len(hid)):
                circ(widths[run], hid[i], "#000000")
            run = run + 1

        for i in range(len(out)):
            circ(widths[len(widths) - 1], out[i], "#000000")

    ts = turtle.getscreen()
    ts.getcanvas().postscript(file="duck.eps")

def circ(x, y, color):
    bob.color("#000000")
    bob.fillcolor(color)
    bob.goto(x, y - 5)
    bob.pendown()
    bob.begin_fill()
    bob.circle(5)
    bob.end_fill()
    bob.penup()