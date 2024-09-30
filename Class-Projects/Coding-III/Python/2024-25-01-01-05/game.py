import turtle as t
import player
import utils

p1 = player.Player()
p1.move()
p1.move()
p1.take_hit()

utils.fill_rect(x=100, y=100, w=100, h=60, f="#fff")