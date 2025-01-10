from turtle import Turtle, Screen
from random import randint, shuffle

turtles = []
colors = ['red','orange','yellow','green','blue','purple']
screen = Screen()
screen.delay(1)
screen.setup(800,600)
for c in colors:
    turtles.append(Turtle('turtle'))
    turtles[-1].color(c)
    turtles[-1].pu()
    turtles[-1].speed(5)
for i in range(len(turtles)):
    ypos = 250 - 100*i
    turtles[i].setposition(-400,ypos)

bet = screen.textinput('Pick your turtle', 'Choose a turtle to win')
race_over = False
while not race_over:
    shuffle(turtles)
    for t in turtles:
        t.forward(randint(1,10))
        if t.xcor() > 400:
            winner = t.color()[0]
            race_over = True
            break

if bet == winner:
    print('you won')
else:
    print(f'you lost.  the winner was {winner}')




screen.exitonclick()