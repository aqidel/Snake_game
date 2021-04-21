import turtle
import time
from mechanics.movement import *
from mechanics.snake import snake_part

window = turtle.Screen()
window.bgcolor('black')
window.screensize(600, 600)
window.listen()

# Mechanics

while True:
    window.update()
    window.onkeypress(go_up, 'Up')
    window.onkeypress(go_down, 'Down')
    window.onkeypress(go_right, 'Right')
    window.onkeypress(go_left, 'Left')
    window.onkeypress(snake_part, 'r')
    window.onkeypress(turtle.bye, 'e')
    while True:
    	time.sleep(1)
    	coord_change()