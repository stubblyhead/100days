from turtle import Screen, Turtle
import time
from snaaaake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.delay(100)
screen.bgcolor('black')
screen.title('Snake?  Snaaaaaake!!!!')
screen.setup(600,600)
screen.screensize(600,600)
screen.tracer(0)
score = Scoreboard()
time.sleep(3)
my_snake = Snake()
food = Food()
screen.update()


screen.listen()
screen.onkey(my_snake.up, 'KP_Up')
screen.onkey(my_snake.down, 'KP_Down')
screen.onkey(my_snake.left, 'KP_Left')
screen.onkey(my_snake.right, 'KP_Right')


while True:
    my_snake.move()
    screen.update()
    dist = my_snake.head.distance(food)
    if  dist < 15:
        score.update_score()
        food.move_food()
        my_snake.grow()
    if abs(my_snake.head.xcor()) > 280 or abs(my_snake.head.ycor()) > 280:
        break
    if my_snake.tail_collision():
        break

score.game_over()
screen.exitonclick()