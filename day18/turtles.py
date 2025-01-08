from turtle import Turtle, Screen
import time
import random


def star(turtle):
    for _ in range(100):
        turtle.forward(200)
        turtle.rt(169)

my_turtle = Turtle()
screen = Screen()
screen.delay(25)
time.sleep(5)
my_turtle.color('green')
my_turtle.shape('turtle')
for _ in range(4):
    for __ in range(5):
        my_turtle.pendown()
        my_turtle.forward(10)
        my_turtle.penup()
        my_turtle.forward(10)
        
    my_turtle.rt(90)


screen.exitonclick()