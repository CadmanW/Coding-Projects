import turtle
from player import *
from turtlehelper import TurtleHelper
import random

WATER = "#87cdde"
GRASS = "#b3ff90"
SAND = "#ffe680"
ROCK = "#999999"

turtle.setup(1024, 512)
turtle.setworldcoordinates(0, 512, 1024, 0)
turtle.tracer(0)
turtle.hideturtle()
turtle.bgcolor("#222")

tiles = []
# Draw all tiles for the 
for x in range(0, 1024, 128):
    for y in range(0, 512, 128):
        tileColor = random.choice([
                WATER, GRASS, SAND, ROCK
        ])
        tiles.append({"x":x, "y":y, "c":tileColor})
        TurtleHelper.fill_rect(
            t=turtle,
            x=x, y=y,
            w=128, h=128,
            f=tileColor
        )

p1 = Player(t=turtle, x=0, y=0, h=128, w=128, f=PLAYER_RED)
p1.draw()


turtle.onkey(lambda move_key="Up": p1.move(move_key, 1024, 512), "Up")
turtle.onkey(lambda move_key="Up": p1.move(move_key, 1024, 512), "w")

turtle.onkey(lambda move_key="Down": p1.move(move_key, 1024, 512), "Down")
turtle.onkey(lambda move_key="Down": p1.move(move_key, 1024, 512), "s")

turtle.onkey(lambda move_key="Left": p1.move(move_key, 1024, 512), "Left")
turtle.onkey(lambda move_key="Left": p1.move(move_key, 1024, 512), "a")

turtle.onkey(lambda move_key="Right": p1.move(move_key, 1024, 512), "Right")
turtle.onkey(lambda move_key="Right": p1.move(move_key, 1024, 512), "d")

turtle.listen()






turtle.done()