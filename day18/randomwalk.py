from turtle import Turtle, Screen, colormode
import time
from random import randint

my_turtle = Turtle()
screen = Screen()
screen.delay(5)
time.sleep(5)
my_turtle.shape('turtle')
colormode(255)
my_turtle.width(5)
my_turtle.speed('fastest')
while True:
    r_val = randint(0,255)
    b_val = randint(0,255)
    g_val = randint(0,255)
    my_turtle.pencolor(r_val, b_val, g_val)
    turn = randint(0,359)
    my_turtle.setheading(turn)
    my_turtle.forward(50)


screen.exitonclick()