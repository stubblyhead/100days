from turtle import Turtle, Screen, colormode
import time
from random import randint

my_turtle = Turtle()
screen = Screen()
screen.delay(1)
time.sleep(5)
my_turtle.shape('turtle')
colormode(255)
my_turtle.speed('fast')

for _ in range(0,360,8):
    r_val = randint(0,255)
    b_val = randint(0,255)
    g_val = randint(0,255)
    my_turtle.pencolor(r_val, b_val, g_val)
    my_turtle.circle(100)
    my_turtle.rt(8)



screen.exitonclick()