from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.goto(0,260)
        self.score = 0
        self.pencolor('white')
        self.font = ('Courier', 18, 'normal')
        self.write(f"Score: {self.score}", align="center",font=self.font)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=self.font)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game over.", align="center", font=self.font)