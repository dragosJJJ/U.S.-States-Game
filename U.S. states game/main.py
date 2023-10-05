import turtle
from state import State
import csv, pandas

screen = turtle.Screen()

data = pandas.read_csv("50_states.csv")

screen.title("U.S. States Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
screen.setup(width=725, height=491)

all_states = data["state"].tolist()
print(all_states)
game_is_on = True

guessed_states = 0
while game_is_on:
    guess = screen.textinput(title=f'{guessed_states}/50 Guessed Correctly', prompt="").title()
    if guess == "Exit":
        game_is_on = False
    if guess in all_states:
        line = data[data.state == guess]
        guessed_states += 1
        new_state = State(guess, (int(line.iloc[0,1]), int(line.iloc[0,2])))
    

print(data)

screen.mainloop()
