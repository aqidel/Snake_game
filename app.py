import turtle
from snake import *
from ball import Ball

window = turtle.Screen()
window.bgcolor('black')
window.screensize(600, 600)
window.listen()

# Mechanics

Snake_chain()
ball = Ball()

window.onkeypress(go_up, 'Up')
window.onkeypress(go_down, 'Down')
window.onkeypress(go_right, 'Right')
window.onkeypress(go_left, 'Left')
window.onkeypress(Snake_chain, 'r')
window.onkeypress(turtle.bye, 'e')

while True:
    window.update()
    coord_change(direction[0], direction[1])
    ball.eat_the_ball()