STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280
from turtle import Turtle


class Player:
    def __init__(self):
        self.p = Turtle('turtle')
        self.p.pu()
        self.p.seth(90)
        self.p.goto(STARTING_POSITION)
    
    def move_turtle(self):
        self.p.fd(MOVE_DISTANCE)
        self.p.screen.update()

    def to_start(self):
        self.p.goto(STARTING_POSITION)

