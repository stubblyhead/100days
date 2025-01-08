from turtle import Turtle, Screen, colormode
import time

my_turtle = Turtle()
screen = Screen()
screen.delay(1)
time.sleep(5)
my_turtle.shape('turtle')
colormode(255)
my_turtle.speed('fast')


def w():
    my_turtle.forward(5)

def s():
    my_turtle.backward(5)

def a():
    my_turtle.lt(5)

def d():
    my_turtle.rt(5)

def c():
    my_turtle.pu()
    my_turtle.setpos(0,0)
    my_turtle.setheading(0)
    my_turtle.clear()
    my_turtle.pd()
    
screen.listen()
screen.onkey(key='w',fun=w)
screen.onkey(key='a',fun=a)
screen.onkey(key='s',fun=s)
screen.onkey(key='d',fun=d)
screen.onkey(key='c',fun=c)



screen.exitonclick()