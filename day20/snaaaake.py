from turtle import Turtle
import time

class Snake:
    def __init__(self):
        self.segments = []
        for i in range(3):
            self.segments.append(Turtle('square'))
            self.segments[-1].color('white')
            self.segments[-1].pu()
            self.segments[-1].setx(-20*i)
            self.segments[-1].speed('slowest')
        self.head = self.segments[0]
    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            self.segments[i].setposition(self.segments[i-1].position())
        self.segments[0].fd(20)
        time.sleep(0.1)
    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].seth(90)
    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].seth(270)
    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].seth(180)
    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].seth(0)

    def grow(self):
        self.segments.append(self.segments[-1].clone())

    def tail_collision(self):
        collision = False
        for s in self.segments[1:]:
            if self.head.distance(s) < 10:
                collision = True
                break
        return collision
