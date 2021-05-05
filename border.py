import turtle

# Function for border drawing

def make_border():
    border = turtle.Turtle()
    border.speed(0)
    border.color('white')
    border.penup()
    border.goto(290, 0)
    border.pendown()
    border.goto(290, 290)
    border.goto(-290, 290)
    border.goto(-290, -290)
    border.goto(290, -290)
    border.goto(290, 0)
    border.color('black')