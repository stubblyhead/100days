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

    def prune(self):
        for c in self.cars:
            if c.xcor() <= -350:
                self.cars.remove(c)

    def level_up(self):
        for c in self.cars:
            c.speed_up()
        self.cur_speed += MOVE_INCREMENT

    def check_collision(self, position):
        # turtle x range 9 to -9 from center
        # turtle y range 16 to -8 from center
        # car x range 20 to -20 from center
        # car y range 10 to -10 from center
        T_X_MIN = -9  # turtle doesn't move left and right so we can make these constants
        T_X_MAX = 9
        t_y_min = position[1] - 8  # turtle goes from 8 below center...
        t_y_max = position[1] + 16 # to 16 above center

        
        for c in self.cars:
            c_x, c_y = c.pos()
            if -29 > c_x or 29 < c_x:  # car is far enough from center that we can skip
                next
            elif t_y_min < c_y < t_y_max:
                return True # current car overlaps turtle's position
        return False # checked all the cars; no collsions                



