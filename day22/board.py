from turtle import Turtle
FONT = ('Courier',72,'normal')
MSGFONT = ('Courier',24,'normal')

class Board():
    def __init__(s):
        s.lscore = 0
        s.rscore = 0
        s.lscore_disp = Turtle()
        s.lscore_disp.speed('fastest')
        s.lscore_disp.hideturtle()
        s.lscore_disp.pu()
        s.lscore_disp.pencolor('white')
        s.lscore_disp.goto(-200,200)
        s.lscore_disp.write(s.lscore,align='center',font=FONT)
        s.rscore_disp = Turtle()
        s.rscore_disp.speed('fastest')
        s.rscore_disp.hideturtle()
        s.rscore_disp.pu()
        s.rscore_disp.pencolor('white')
        s.rscore_disp.goto(200,200)
        s.rscore_disp.write(s.rscore,align='center',font=FONT)
        s.net=Turtle()
        s.net.speed('fastest')
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

    def add_left(self):
        self.lscore += 1
        self.lscore_disp.clear()
        self.lscore_disp.write(self.lscore,align='center',font=FONT)

    def add_right(self):
        self.rscore += 1
        self.rscore_disp.clear()
        self.rscore_disp.write(self.rscore,align='center',font=FONT)

    def winner(self,side):
        self.net.goto(0,0)
        self.net.write(f'Game over. {side} wins.',align='center',font=MSGFONT)
        
        

        