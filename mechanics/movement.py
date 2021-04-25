import time
coordinates = [0, 0]
direction = [1, '+']
previous_move = ''
snake = []

def coord_change(num, sign):
    if sign == '+':
        coordinates[num] += 20
    else:
        coordinates[num] -= 20
    snake[0].goto(coordinates[0], coordinates[1])
    snake.append(snake[0])
    snake.remove(snake[0])
    time.sleep(1)

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