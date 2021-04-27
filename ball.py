import turtle
import random
from snake import coordinates
from snake import create_snake

ball_coord = []

def ball_coords_generator():
	coord = 1
	for i in range(2):
		while coord % 20:
			coord = random.randint(-30, 30) * 10
		ball_coord.append(coord)
		coord = 1

def create_ball():
	ball = turtle.Turtle()
	ball.speed(0)
	ball.penup()
	ball.shape('square')
	ball.color('white')
	ball_coords_generator()
	ball.goto(ball_coord[0], ball_coord[1])
	return ball

ball = create_ball()

def eat_the_ball():
	if [ball.xcor(), ball.ycor()] == coordinates:
		create_snake()
		ball_coords_generator()
		ball.goto(ball_coord[0], ball_coord[1])