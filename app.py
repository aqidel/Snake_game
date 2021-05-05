# Main part of the game
import turtle
from snake import *
from ball import Ball
from border import make_border

window = turtle.Screen()
window.bgcolor('black')
window.screensize(600, 600)
window.listen()

# Turning off function of the game
boolean = True

def turnoff():
    global boolean
    boolean = False

# Turning off the game if border/other part of the snake is reached
def crash():
    head = snake[len(snake) - 1]
    if head.xcor() >= 300:
        turnoff()
    if head.xcor() <= -300:
        turnoff()
    if head.ycor() >= 300:
        turnoff()
    if head.ycor() <= -300:
        turnoff()
    for i in snake:
        if [head.xcor(), head.ycor()] == [i.xcor(), i.ycor()]:
            if head == i:
                return
            turnoff()

# Initialisation of border & snake & ball
make_border()
Snake_chain()
ball = Ball()

# Controls of the snake
window.onkeypress(go_up, 'Up')
window.onkeypress(go_down, 'Down')
window.onkeypress(go_right, 'Right')
window.onkeypress(go_left, 'Left')
window.onkeypress(turnoff, 'Escape')

# Loop for updating screen & auto-movement of the snake & ball spawn/destroying & crash checkout 
while boolean:
    window.update()
    coord_change(direction[0], direction[1])
    ball.eat_the_ball()
    crash()