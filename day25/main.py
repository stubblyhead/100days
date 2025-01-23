import turtle
import pandas

state_data = pandas.read_csv('50_states.csv')
state_dict = {}
for s in state_data.state:
    state_dict[s] = (state_data.x[state_data.state == s], state_data.y[state_data.state == s])

print(state_dict)

screen = turtle.Screen()
screen.title('us states game')
screen.bgpic('blank_states_img.gif')

screen.exitonclick()