from turtle import Screen
from board import Board
from paddle import Paddle

screen = Screen()
screen.delay(100)
screen.bgcolor('black')
screen.title('Ping?  Pong!')
screen.setup(1200,600)
screen.screensize(1200,600)
screen.tracer(0)

board = Board()

left_paddle = Paddle('left')
right_paddle = Paddle('right')
screen.update()


screen.exitonclick()