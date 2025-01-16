import time
from turtle import Screen,Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

traffic = CarManager()
player = Player()
screen = Screen()
score = Scoreboard()
grid_lines = Turtle()


screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(player.move_turtle, 'W')


for i in range(-300,310,10):
    if i %50 == 0:
        grid_lines.pencolor('red')
    else:
        grid_lines.pencolor('black')
    grid_lines.pu()
    grid_lines.goto(-300,i)
    # grid_lines.pd()
    grid_lines.fd(600)


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    traffic.spawn_car()
    traffic.move_cars()
    if player.p.ycor() >= 280:
        score.update_level()
        traffic.level_up()
        player.to_start()
