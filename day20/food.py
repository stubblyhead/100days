from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.pu()
        self.shapesize(0.5,0.5)
        self.color('orange')
        self.speed('fastest')
        self.move_food()
        

    def move_food(self):
        self.goto(5*random.randint(-59,59),5*random.randint(-59,59))

        