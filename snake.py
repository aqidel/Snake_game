# Snake module
import turtle
import time

# Array including all snake's parts
snake = []
# Coordinates of the head
coordinates = [0, 0]
# Direction of movement. 1 (+,-) for y (up, down); 0 (+,-) for x (right, left)
direction = [1, '+']
# For backward movement prevention. I.e., with 'down' value can't return same way (upward)
previous_move = ''

class Snake_chain(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.penup()
        self.shape('square')
        self.color('white')
        self.create_snake()

    def create_snake(self):
        if len(snake) > 0:
            self.setpos(snake[0].xcor(), snake[0].ycor() - 20)
        snake.insert(0, self)

# Auto-movement every 0.5 sec to given direction
def coord_change(num, sign):
    if sign == '+':
        coordinates[num] += 20
    else:
        coordinates[num] -= 20
    snake[0].setpos(coordinates[0], coordinates[1])
    snake.append(snake[0])
    snake.remove(snake[0])
    time.sleep(0.5)

# For contols from app.py & giving direction & backward movement prevention
def go_up():
    global previous_move
    if previous_move == 'down':
        return
    direction[0] = 1 
    direction[1] = '+'
    previous_move = 'up'

def go_down():
    global previous_move
    if previous_move == 'up':
        return
    direction[0] = 1 
    direction[1] = '-'
    previous_move = 'down'

def go_right():
    global previous_move
    if previous_move == 'left':
        return
    direction[0] = 0
    direction[1] = '+'
    previous_move = 'right'

def go_left():
    global previous_move
    if previous_move == 'right':
        return
    direction[0] = 0
    direction[1] = '-'
    previous_move = 'left'