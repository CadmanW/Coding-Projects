# Import turtle and my functions file
import turtle as t

#* Setup
size = 1000

# Set up the application
t.hideturtle()
t.title = "SUPER COOL GAME"
t.setup(size, size, 0, 0) #sizeX, sizeY, monitorX, monitorY
t.speed(0) # Remove animations
t.bgcolor("#ADD8E6")
t.setundobuffer(50)

# Calculate the layout
gridLength = int(t.numinput("Grid Size", "Give me an odd number", 5, 3, 99))
squareSize = size / gridLength
penWidth = squareSize / 10
squareSize -= penWidth / 10
t.width(penWidth)

def drawGrid():
    
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
class DialogueBox:
    def __init__(self):
        # Calculate size and position of dialogue box to put it at the bottom left of the screen
        boxSizeX = size / 6
        boxSizeY = size / 18
        origin = -size / 2
        self.origin = origin
        self.boxSizeX = boxSizeX
        self.boxSizeY = boxSizeY

        # Draws the Dialogue box
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
        t.setundobuffer(t.undobufferentries() + 1)

        self.fontSize = self.boxSizeX / 6

        t.up()
        t.goto(self.origin + (self.boxSizeX / 2), self.origin + (self.boxSizeY / 2) - (self.fontSize / 2))
        t.color("#000000", "#000000")
        t.down()
        t.write(f"> {self.input}", align = "center", font = ("Arial", int(self.fontSize), "normal"))

    def submitCMD(self):
        # Get command into parts for square selection and color
        input = [self.input[:-1], self.input[-1]]
        self.input = ""

        while t.undobufferentries():
            t.undo()

        # for i in range(len(input) + 11):
        #     t.undo()

        # Throws an error if input is invalid
        try:
            # Figure out color selected
            colors = {
                'r': "#FF0000",
                'o': "#FFA500",
                'y': "#FFFF00",
                'g': "#00FF00",
                'b': "#0000FF",
                'i': "#4B0082",
                'v': "#8F00FF"
            }

            color = colors[str(input[1])]


            # Figure out (x, y) of the square selected
            num = int(input[0])

            x = (num - 1) % gridLength

            y = 0

            if (y % gridLength == 0):
                y += 1
            
            while num >= gridLength:
                num = num / gridLength
                y += 1

            print("x, y", x, y)
            print(x * squareSize, y * squareSize)

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

            global dialogueBox
            dialogueBox = None

        except:
            print("Invalid Command")




































drawGrid()


dialogueBox = None
# Function that runs on input
def handleInput(key):
    # Use the global variable for dialogueBox instead of local
    global dialogueBox

    try:
        dialogueBox # Throws an error if dialogueBox doesn't exist

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
        if key == "u":
            t.undo()
        else:
            dialogueBox = DialogueBox()
            dialogueBox.input += key
            dialogueBox.update()





# Make notes on the commands




#* Listen for input
keys = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "r", "o", "y", "g", "b", "i", "v", "-", "/"]

# Bind handleInput(key_pressed) to the keys
for key in keys:
    t.onkey((lambda k = key: handleInput(k)), key)

# Focus the window to listen for input
t.listen()

# Keeps window open
t.done()