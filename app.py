import turtle
from snake import *
from ball import *

window = turtle.Screen()
window.bgcolor('black')
window.screensize(600, 600)
window.listen()

# Mechanics

create_snake()

while True:
    window.update()
    window.onkeypress(go_up, 'Up')
    window.onkeypress(go_down, 'Down')
    window.onkeypress(go_right, 'Right')
    window.onkeypress(go_left, 'Left')
    window.onkeypress(create_snake, 'r')
    window.onkeypress(turtle.bye, 'e')
    coord_change(direction[0], direction[1])