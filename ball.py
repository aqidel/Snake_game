import turtle
from snake import coordinates

def create_ball():
	ball = turtle.Turtle()
	ball.speed(0)
	ball.penup()
	ball.shape('square')
	ball.color('white')
	ball.goto(60, 0)
	return ball

ball = create_ball()

create_ball()
