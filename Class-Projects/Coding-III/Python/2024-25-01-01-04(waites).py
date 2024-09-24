import turtle as t

t.title("BOXES")
t.setup(600, 600, 0, 0)
t.screensize(400, 400)
t.setworldcoordinates(0, 400, 400, 0)

class Box():
    def __init__(self, args):
        self.x = args[0]
        self.y = args[1]
        self.length = args[2]
        self.fill = args[3]
        self.stroke = args[4]

    def draw(self):
        t.fillcolor(self.fill)
        t.pencolor(self.stroke)
        t.begin_fill()
        t.goto(self.x, self.y)
        for i in range(4):
            t.fd(self.length)
            t.seth(t.heading() + 90)
        t.end_fill

boxes = []

boxes.append(Box(0, 0, 50, "#222", "#0f0"))

boxes[0].draw()











t.done()

