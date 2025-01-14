from turtle import Turtle
FONT = ('Courier',72,'normal')

class Board():
    def __init__(self):
        s=self
        s.lscore = 0
        s.rscore = 0
        s.lscore_disp = Turtle()
        s.lscore_disp.hideturtle()
        s.lscore_disp.pu()
        s.lscore_disp.pencolor('white')
        s.lscore_disp.goto(-200,200)
        s.lscore_disp.write(s.lscore,align='center',font=FONT)
        s.rscore_disp = Turtle()
        s.rscore_disp.hideturtle()
        s.rscore_disp.pu()
        s.rscore_disp.pencolor('white')
        s.rscore_disp.goto(200,200)
        s.rscore_disp.write(s.rscore,align='center',font=FONT)
        s.net=Turtle()
        s.net.hideturtle()
        s.net.width(5)
        s.net.sety(300)
        s.net.seth(270)
        s.net.pencolor('white')
        for _ in range(6):
            s.net.pd()
            s.net.fd(50)
            s.net.pu()
            s.net.fd(50)
        