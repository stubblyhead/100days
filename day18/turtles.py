from turtle import Turtle, Screen
import time

def star(turtle):
    for _ in range(100):
        turtle.forward(100)
        turtle.rt(95)
my_turtle = Turtle()
screen = Screen()
screen.delay(5)
time.sleep(5)
my_turtle.color('green')
my_turtle.shape('turtle')
star(my_turtle)



screen.exitonclick()