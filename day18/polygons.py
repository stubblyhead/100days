from turtle import Turtle, Screen, colormode
import time
from random import randint

my_turtle = Turtle()
screen = Screen()
screen.delay(25)
time.sleep(5)
my_turtle.shape('turtle')
colormode(255)
my_turtle.width(3)
for i in range(3,21):
    r_val = randint(0,255)
    b_val = randint(0,255)
    g_val = randint(0,255)
    my_turtle.pencolor(r_val, b_val, g_val)
    for _ in range(i):
        my_turtle.forward(100)
        my_turtle.rt(360/i)   


screen.exitonclick()