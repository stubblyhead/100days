from turtle import Screen, Turtle, textinput
import pandas

state_data = pandas.read_csv('50_states.csv')
state_dict = {}
for s in state_data.state:
    state_dict[s] = (int(state_data.x[state_data.state == s].iloc[0]), int(state_data.y[state_data.state == s].iloc[0]))

print(state_dict)

screen = Screen()
screen.title('us states game')
screen.bgpic('blank_states_img.gif')

answer = Turtle()
answer.hideturtle()
answer.pu()

while state_dict:
    guess = textinput(prompt='Guess a state',title='your guess')
    if guess in state_dict.keys():
        answer.goto(state_dict[guess])
        answer.write(guess, align='center', font=['Arial', 8, 'normal'])
        state_dict.pop(guess)
    else:
        print('you dumbass')
        break

screen.exitonclick()