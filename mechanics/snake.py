import turtle
from .movement import snake

class snake_part:
	def __init__(self):
		self = turtle.Turtle()
		self.speed(0)
		self.penup()
		self.shape('square')
		self.color('white')
		if len(snake) > 0:
			self.goto(snake[0].xcor(), snake[0].ycor() - 20)
		snake.insert(0, self)
