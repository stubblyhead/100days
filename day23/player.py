STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle


class Player:
    def __init__(self):
        self.p = Turtle('turtle')
        self.p.pu()
        self.p.seth(90)
        self.p.goto(STARTING_POSITION)
    
    def move_turtle(self):
        self.fd(10)

