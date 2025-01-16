FONT = ("Courier", 24, "normal")
GAMEOVER_FONT = ("Courier", 24, "bold")
from turtle import Turtle


class Scoreboard:
    def __init__(self):
        self.level = 0
        self.level_disp = Turtle()
        # self.level_disp.hideturtle()
        self.level_disp.pu()
        self.level_disp.goto(-290,265)
        self.update_level()
        self.game_over_msg = Turtle()
        self.game_over_msg.hideturtle()

        

    def update_level(self):
        self.level += 1
        self.level_disp.clear()
        self.level_disp.write(f'Level: {self.level}', align='left', font=FONT)

    def game_over(self):
        self.game_over_msg.write('GAME OVER', align='center', font=GAMEOVER_FONT)


    