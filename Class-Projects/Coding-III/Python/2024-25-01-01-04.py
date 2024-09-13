import turtle as t
import math

#* Setup

size = 900

# Set up the screen
t.hideturtle()
t.title = "SUPER COOL GAME"
t.setup(size, size, 0, 0) #sizeX, sizeY, monitorX, monitorY
t.speed(0) # Remove animations
t.color("#000000", "#ffffff") # pen, fill
t.bgcolor("#ADD8E6")

# Calculate the layout
gridLength = int(t.numinput("Grid Size", "Give me an odd number", 5, 3, 99))
squareSize = size / gridLength
penWidth = squareSize / 10
t.width(penWidth)
squareSize -= penWidth / 10









#* Draw the grid

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
class DialogueBox:
    def __init__(self):
        # Dialogue box that's in the middle of the screen
        # boxSizeX = size / 4
        # boxSizeY = size / 7

        # t.up()
        # t.goto(-boxSizeX, boxSizeY)
        # t.down()
        # t.begin_fill()
        # t.goto(boxSizeX, boxSizeY)
        # t.goto(boxSizeX, -boxSizeY)
        # t.goto(-boxSizeX, -boxSizeY)
        # t.goto(-boxSizeX, boxSizeY)
        # t.end_fill()

        # Dialogue box that's at the bottom left
        boxSizeX = size / 6
        boxSizeY = size / 18
        origin = -size / 2
        self.origin = origin
        self.boxSizeX = boxSizeX
        self.boxSizeY = boxSizeY

        t.up()
        t.goto(origin, origin)
        t.color("#ffffff", "#ffffff")
        t.width(penWidth / 10)
        t.down()
        t.begin_fill()
        t.goto(origin, origin + boxSizeY)
        t.goto(origin + boxSizeX, origin + boxSizeY)
        t.goto(origin + boxSizeX, origin)
        t.goto(origin, origin)
        t.end_fill()

    input = ""

    def add(self, key):
        self.input += key
        fontSize = self.boxSizeX / 6

        t.up()
        t.goto(self.origin + (self.boxSizeX / 2), self.origin + (self.boxSizeY / 2) - (fontSize / 2))
        t.color("#000000", "#000000")
        t.down()
        t.write(f"> {self.input}", align = "center", font = ("Arial", int(fontSize), "normal"))

        print(self.input)

# Function that runs on input
dialogueBox = None

def handleInput(key):
    # Initialize class DialogueBox() if it's not already existing
    
    global dialogueBox

    try:
        t.undo()
        print(key)
        dialogueBox.add(key)
    except:
        dialogueBox = DialogueBox()
        dialogueBox.add(key)

# Listen for input
keys = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "r", "o", "y", "g", "b", "i", "v", "Enter", "Backspace"]
for key in keys:
    t.onkey((lambda k=key: handleInput(k)), key)

# Focus the window to listen for input
t.listen()









#* Keeps window open
t.done()