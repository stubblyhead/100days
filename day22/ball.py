from turtle import Turtle
from random import randint

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.pu()
        self.seth(randint(-45,45))
        self.speed(8)
    
    def move(self):
        self.fd(5)

    def bounce_paddle(self):
        cur_hd = self.heading()
        self.seth(180-cur_hd+randint(-5,5))

    def bounce_wall(self):
        cur_hd = self.heading()
        self.seth(-cur_hd+randint(-5,5))