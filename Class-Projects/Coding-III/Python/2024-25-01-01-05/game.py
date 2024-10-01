import turtle
import player
from turtlehelpers import TurtleHelpers

p1 = player.Player(t=turtle, x=0, y=0, h=96, w=96, c="ff0000")
p1.draw()

turtle.done


# manage game state 1st lesson if you're gonna develop games
# learn how to create a "state machine"