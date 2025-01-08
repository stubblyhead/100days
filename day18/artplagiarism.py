import colorgram
from turtle import Turtle, Screen, colormode
import time
from random import randint, choice

my_turtle = Turtle()
screen = Screen()
screen.delay(1)
time.sleep(5)
my_turtle.shape('turtle')
colormode(255)
my_turtle.speed(1)
my_turtle.ht()

my_colors = colorgram.extract('car.jpg',12)
color_tpls = [ tuple(i.rgb) for i in my_colors[2:] ]

my_turtle.pu()
my_turtle.goto(-190,-140)
my_turtle.setheading(0)

for _ in range(10):
    for __ in range(10):
        my_turtle.color(choice(color_tpls))
        my_turtle.dot(20)
        my_turtle.forward(50)
    my_turtle.setx(my_turtle.xcor() - 500)
    my_turtle.sety(my_turtle.ycor() + 50)


screen.exitonclick()