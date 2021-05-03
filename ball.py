import turtle
import random
from snake import coordinates
from snake import Snake_chain

class Ball(turtle.Turtle):
	def __init__(self):
		super().__init__()
		self.speed(0)
		self.penup()
		self.shape('square')
		self.color('white')
		self.ball_coord = []
		self.ball_spawn()

	def ball_spawn(self):
		coord = 1
		self.ball_coord = []
		for i in range(2):
			while coord % 20:
				coord = random.randint(-30, 30) * 10
			self.ball_coord.append(coord)
		self.setpos(self.ball_coord[0], self.ball_coord[1])
		coord = 1

	def eat_the_ball(self):
		if [self.xcor(), self.ycor()] == coordinates:
			Snake_chain()
			self.ball_spawn()