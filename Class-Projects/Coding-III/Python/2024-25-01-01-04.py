# Import turtle and my functions file
import turtle as t

#* Setup
size = 1300
cmdBox = None

# Set up the application
t.hideturtle()
t.title = "SUPER COOL GAME"
t.setup(size, size, 0, 0) #sizeX, sizeY, monitorX, monitorY
t.tracer(0, 0) # Remove animations
t.bgcolor("#ADD8E6")
t.setundobuffer(1024)

# Calculate the layout
gridLength = int(t.numinput("Grid Size", "Give me an odd number", 5))
squareSize = size / gridLength
penWidth = squareSize / 10
squareSize -= penWidth / 10
t.width(penWidth)

#* Draw the grid
t.color("#000000", "#ffffff") # pen, fill

# Horizontal
t.seth(90)
for i in range(0, gridLength + 1):
    t.up()
    t.goto(-size / 2, (-squareSize * i) + (size / 2))
    t.down()
    t.goto(size / 2, (-squareSize * i) + (size / 2))

# Vertical
t.seth(180)
for i in range(0, gridLength + 1):
    t.up()
    t.goto((squareSize * i) - (size / 2), size / 2)
    t.down()
    t.goto((squareSize * i) - (size / 2), -size / 2)


#* Handle input

# Box that opens when there is input, displaying said input
class CmdBox:
    def draw(self):
        self.status = 1

        # Calculate size and position of dialogue box to put it at the bottom left of the screen
        boxSizeY = size / 18
        origin = -size / 2
        self.origin = origin
        self.boxSizeY = boxSizeY

        # Draws the Dialogue box
        t.up()
        t.goto(origin, origin)
        t.color("#ff0000", "#ffffff")
        t.width(penWidth / 10)
        t.down()
        t.begin_fill()
        t.goto(origin, origin + boxSizeY)
        t.goto(origin + size, origin + boxSizeY)
        t.goto(origin + size, origin)
        t.goto(origin, origin)
        t.end_fill()

        t.pu()
        t.goto(0, 0)

    cmd = ""

    def update(self):
        t.undo()

        self.fontSize = size / 35

        t.up()
        t.goto(self.origin + (size / 2), self.origin + (self.boxSizeY / 2) - (self.fontSize / 2))
        t.color("#000000", "#000000")
        t.down()
        t.write(f"> {self.cmd}", align = "center", font = ("Arial", int(self.fontSize), "normal"))


    def submitCMD(self):
        cmd = self.cmd.split(" ")
        self.cmd = ""

        # Throws an error if command is invalid is invalid
        try:
            # Figure out color selected
            colors = {
                'red': "#FF0000",
                'orange': "#FFA500",
                'yellow': "#FFFF00",
                'green': "#00FF00",
                'blue': "#0000FF",
                'indigo': "#4B0082",
                'voilet': "#8F00FF"
            }

            color = colors[str(cmd[1])]


            # Figure out (x, y) of the square selected
            num = int(cmd[0])

            x = (num - 1) % gridLength

            y = 0
            while num > gridLength:
                num -= gridLength
                y += 1


            # Draw the newly color-filled square
            t.up()
            t.goto((-size / 2) + (x * squareSize) + (penWidth / 2), (size / 2) - (y * squareSize) - (penWidth / 2))
            t.seth(0)
            t.color("#000000", color)
            t.down()
            t.begin_fill()
            for i in range(4):
                t.fd(squareSize - penWidth)
                t.right(90)
            t.end_fill()

        except:
            print(f"Invalid Command: \"{self.cmd}\"")

cmdBox = CmdBox()
cmdBox.draw()


# Function that runs on input
def handleInput(key):
    global cmdBox

    match key:
        case "BackSpace":
            cmdBox.cmd = cmdBox.cmd[:-1]
            cmdBox.update()
        case "/":
            cmdBox.submitCMD()
        case "space":
            cmdBox.cmd += " "
            cmdBox.update()
        case _:
            cmdBox.cmd += key
            cmdBox.update()












#* Listen for and handle input
keys = ["space", "BackSpace", "/", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
for key in keys:
    t.onkey((lambda k = key: handleInput(k)), key)


# Focus the window to listen for input
t.listen()


# Keeps window open
t.done()