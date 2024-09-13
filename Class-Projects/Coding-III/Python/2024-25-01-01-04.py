import turtle as t

#* Setup

size = 700

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
        # Calculate size and position of dialogue box to put it at the bottom left of the screen
        boxSizeX = size / 6
        boxSizeY = size / 18
        origin = -size / 2
        self.origin = origin
        self.boxSizeX = boxSizeX
        self.boxSizeY = boxSizeY

        # draws the Dialogue box
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

    def update(self):
        self.fontSize = self.boxSizeX / 6

        t.up()
        t.goto(self.origin + (self.boxSizeX / 2), self.origin + (self.boxSizeY / 2) - (self.fontSize / 2))
        t.color("#000000", "#000000")
        t.down()
        t.write(f"> {self.input}", align = "center", font = ("Arial", int(self.fontSize), "normal"))

    def submitCMD(self):
        #* Validate input
        input = [self.input[:-1], self.input[-1]]

        try:
            int(input[0])

            # Color input[1] the square input[0] and the color

        except:
            print("Invalid Command")


# Function that runs on input
dialogueBox = None

def handleInput(key):
    # Use the global variable for dialogueBox instead of local
    global dialogueBox
    #? Maybe use nonlocal instead? https://docs.python.org/3/reference/simple_stmts.html#nonlocal

    try:
        dialogueBox # Throws an error if dialogueBox doesn't exist

        print(key)
        if key == "-": 
            dialogueBox.input = dialogueBox.input[:-1]
            t.undo()
            dialogueBox.update()

        elif key == "/":
            dialogueBox.submitCMD()

        else:
            dialogueBox.input += key
            t.undo()
            dialogueBox.update()

    except:
        dialogueBox = DialogueBox()
        dialogueBox.input += key
        dialogueBox.update()

# Listen for input
keys = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "r", "o", "y", "g", "b", "i", "v", "-", "/"]
for key in keys:
    t.onkey((lambda k=key: handleInput(k)), key)

# Focus the window to listen for input
t.listen()

#* Keeps window open
t.done()