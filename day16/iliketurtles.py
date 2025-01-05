from turtle import Turtle, Screen
import time



my_turtle = Turtle()
my_screen = Screen()
print(my_screen.canvheight, my_screen.canvwidth)

my_screen.delay(50)
time.sleep(5)
my_turtle.shape("turtle")
my_turtle.color("red")
my_turtle.forward(100)
print(my_turtle)
my_screen.exitonclick()