import turtle as t

size = 400
input = 5

t.title("BOXES")
t.setup(size + 200, size + 200, 0, 0)
t.screensize(size, size)
t.setworldcoordinates(0, size, size, 0)
t.tracer(0, 0)

class Drawable():
    def draw(self):
        pass

class Box(Drawable):
    def __init__(self, *args):
        self.x = args[0]
        self.y = args[1]
        self.length = args[2]
        self.fill = args[3]
        self.stroke = args[4]

    def __str__(self):
        return f"Location: ({self.x}, {self.y}) area: {self.length ** 2} pixels"

    def draw(self):
        t.fillcolor(self.fill)
        t.pencolor(self.stroke)
        t.begin_fill()
        t.goto(self.x, self.y)
        for i in range(4):
            t.fd(self.length)
            t.seth(t.heading() + 90)
        t.end_fill

class Grid(Drawable):
    def __init__(self, *args):
        self.fill = args[0]
        self.stroke = args[1]

    def __str__(self):
        string = ""

        for i in range(input):
            string += f"{'----' * input}-\n{f'| {i} ' * (input)}\n"
        string += f"{'----' * input}-"

        return string

    def draw(self):
        t.color(self.stroke, self.fill)

        for i in range(input + 1):
            t.pu()
            t.goto((size / input) * i, 0)
            t.pd()
            t.goto((size / input) * i, size)

        for i in range(input + 2):
            t.pu()
            t.goto(0, (size / input) * i)
            t.pd()
            t.goto(size, (size / input) * i)

boxes = []

boxes.append(Box(0, 0, 50, "#222", "#0F0"))

for box in boxes:
    pass

print(boxes[0])

grid = Grid("white", "black")
grid.draw()\

print(grid)

t.done() 