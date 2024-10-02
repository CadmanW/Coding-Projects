import turtle
from player import *
from turtlehelper import TurtleHelper

turtle.setup(1024, 512)
turtle.setworldcoordinates(0, 512, 1024, 0)
turtle.tracer(0)

p1 = Player(t=turtle, x=0, y=0, h=128, w=128, c=PLAYER_RED)
p1.draw()


turtle.onkey(lambda k="Up": p1.move(k), "Up")
turtle.onkey(lambda k="Up": p1.move(k), "w")

turtle.onkey(lambda k="Down": p1.move(k), "Down")
turtle.onkey(lambda k="Down": p1.move(k), "s")

turtle.onkey(lambda k="Left": p1.move(k), "Left")
turtle.onkey(lambda k="Left": p1.move(k), "a")

turtle.onkey(lambda k="Right": p1.move(k), "Right")
turtle.onkey(lambda k="Right": p1.move(k), "d")

turtle.listen()






turtle.done()