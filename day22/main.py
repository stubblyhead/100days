from turtle import Screen
import turtle
from board import Board
from paddle import Paddle
from ball import Ball
import time
from random import randint

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
ball = Ball()



screen.listen()
screen.onkey(left_paddle.up, 'w')
screen.onkey(left_paddle.down, 's')
screen.onkey(left_paddle.up, 'W')
screen.onkey(left_paddle.down, 'S')
screen.onkey(right_paddle.up, 'o')
screen.onkey(right_paddle.down, 'l')
screen.onkey(right_paddle.up, 'O')
screen.onkey(right_paddle.down, 'L')
last_score = None
time.sleep(5)
while True:
    screen.update()
    ball.move()
    time.sleep(0.01)
    #bounces off left paddle
    if ball.xcor() <= -540 and left_paddle.ycor()-80<ball.ycor()<left_paddle.ycor()+80:
        ball.bounce_paddle()
    #bounces off right paddle
    if ball.xcor() >= 540 and right_paddle.ycor()-80<ball.ycor()<right_paddle.ycor()+80:
        ball.bounce_paddle()
    #bounces off top or bottom
    if abs(ball.ycor()) >= 250:
        ball.bounce_wall()
    
    if ball.xcor() >= 550:
        board.add_left()
        if board.lscore == 5:
            break
        ball.goto(0,0)
        ball.seth(randint(-45,45))
        screen.update()
        time.sleep(2)
    if ball.xcor() <= -550:
        board.add_right()
        if board.rscore == 5:
            break
        ball.goto(0,0)
        ball.seth(randint(135,225))
        screen.update()
        time.sleep(2)
ball.hideturtle()
if board.lscore > board.rscore:
    board.winner('Left')
else:
    board.winner('Right')

turtle.mainloop()
