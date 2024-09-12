import turtle as t

# Set up the screen
t.title = "SUPER COOL GAME"
t.mode("logo")
t.setup(width = 900, height = 900, startx = -450, starty = 450)
t.speed(0)
t.color('black')
t.bgcolor("#ADD8E6")

# Set up the layout
gridLength = int(t.numinput("Grid Size", "Give me an odd number", 5, 3, 99))
squareSize = 900 / gridLength
borderSize = squareSize / 10
t.width(borderSize)
squareSize -= borderSize / 10











# Horizontal
t.seth(90)
t.up()
for i in range(0, gridLength + 1):
    t.goto(-450, (squareSize * i * -1) + 450)
    t.down()
    t.forward(squareSize * gridLength)
    t.up()

# Vertical
t.seth(180)
for i in range(0, gridLength + 1):
    t.goto((squareSize * i) - 450, 450)
    t.down()
    t.forward(squareSize * gridLength)
    t.up()








def handleInput(key):
    print(key)

# Listen for input
t.onkey((lambda: handleInput("0")), "0")
t.onkey((lambda: handleInput("1")), "1")
t.onkey((lambda: handleInput("2")), "2")
t.onkey((lambda: handleInput("3")), "3")
t.onkey((lambda: handleInput("4")), "4")
t.onkey((lambda: handleInput("5")), "5")
t.onkey((lambda: handleInput("6")), "6")
t.onkey((lambda: handleInput("7")), "7")
t.onkey((lambda: handleInput("8")), "8")
t.onkey((lambda: handleInput("9")), "9")
t.onkey((lambda: handleInput("r")), "r")
t.onkey((lambda: handleInput("o")), "o")
t.onkey((lambda: handleInput("y")), "y")
t.onkey((lambda: handleInput("g")), "g")
t.onkey((lambda: handleInput("b")), "b")
t.onkey((lambda: handleInput("i")), "i")
t.onkey((lambda: handleInput("v")), "v")

t.listen()









# Keeps window open
t.mainloop()