from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,side):
        super().__init__()
        self.hideturtle()
        self.shape('square')
        self.pu()
        self.color('white')
        self.rt(90)
        self.shapesize(1,10)
        if side == 'left':
            self.setx(-550)
            self.showturtle()
        elif side == 'right':
            self.setx(550)
            self.showturtle()

    