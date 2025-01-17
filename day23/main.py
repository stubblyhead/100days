import time
from turtle import Screen,Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

traffic = CarManager()
player = Player()
screen = Screen()
score = Scoreboard()



screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(player.move_turtle, 'W')
screen.onkey(player.move_turtle, 'w')

while True:
    time.sleep(0.1)
    traffic.spawn_car()
    traffic.move_cars()
    traffic.prune()
    if traffic.check_collision(player.p.pos()):
        break
    if player.p.ycor() >= 280:
        score.update_level()
        traffic.level_up()
        player.to_start()
    screen.update()

score.game_over()

screen.mainloop()