from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,side):
        super().__init__()
        self.hideturtle()
        self.shape('square')
        self.pu()
        self.color('white')
        self.lt(90)
        self.shapesize(1,8)
        self.speed('fastest')
        if side == 'left':
            self.setx(-550)
        elif side == 'right':
            self.setx(550)
        self.showturtle()
        self.speed('normal')
        

    def up(self):
        self.fd(10)
        self.screen.update()

    def down(self):
        self.bk(10)
        self.screen.update()

    