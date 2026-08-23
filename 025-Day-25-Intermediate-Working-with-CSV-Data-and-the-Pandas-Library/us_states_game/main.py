import turtle as t
import pandas as pd

CSV_PATH = "./50_states_scaled.csv"
IMAGE_PATH = "./big_blank_states_img.gif"


# ===================Screen================================
screen = t.Screen()
# screen._root.tk.call('tk', 'scaling', 3.0)
screen.setup(2175, 1473)
screen.title("U.S. States Game")
screen.bgcolor("lavender")
screen.addshape(IMAGE_PATH)
t.shape(IMAGE_PATH)

# =====================================csv handling=============================
data = pd.read_csv(CSV_PATH)
states = data.state.to_list()
guessed = []
remaining = states[:]

tim = t.Turtle()
tim.hideturtle()
tim.penup()
tim.speed("fastest")

while True:
    answer_state = screen.textinput(
        title=f"You have guessed {len(guessed)}/50", prompt="What's another state?"
    )
    if answer_state:
        answer_state = answer_state.strip().title()
    else:
        answer_state = None
    if answer_state not in guessed and answer_state in states:
        xcor = data[data.state == answer_state].x.item()
        ycor = data[data.state == answer_state].y.item()
        tim.goto((xcor, ycor))
        tim.write(answer_state, align="center", font=("Arial", 30, "normal"))
        guessed.append(answer_state)
        remaining.remove(answer_state)
    if answer_state.lower() == 'exit':
        break
    if len(guessed) == len(states):
        print("Congrats You Win!")
        break

## Generate a file for teh  states the user missed

missed_states = pd.DataFrame(remaining)
missed_states.to_csv('missed_states.csv')



