COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from random import randint, choice
from turtle import Turtle

class Car(Turtle):
    def __init__(self, speed):
        super().__init__()
        self.shape('square')
        self.shapesize(1,2)
        self.pu()
        self.color(choice(COLORS))
        self.setx(310)
        self.sety(randint(-250,250))
        self.seth(180)
        self.speed = speed

    def speed_up(self):
        self.speed += MOVE_INCREMENT


class CarManager:
    def __init__(self):
        self.cars = []
        self.cur_speed = STARTING_MOVE_DISTANCE
    
    def spawn_car(self):
        if randint(1,100) <= 50:
            self.cars.append(Car(self.cur_speed))

    def move_cars(self):
        for c in self.cars:
            c.fd(c.speed)

    def level_up(self):
        for c in self.cars:
            c.speed_up()
            self.cur_speed += MOVE_INCREMENT

