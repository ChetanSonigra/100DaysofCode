import turtle
import pandas as pd

screen = turtle.Screen()
screen.title('US States Game')
image = 'Day25/US_States_Game/blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)

data_df = pd.read_csv('Day25/US_States_Game/50_states.csv')

states = data_df['state'].to_list()

guessed_states = []

while len(guessed_states)<50:
    answer_state = screen.textinput(title=f'States Guessed: {len(guessed_states)}/50',prompt="What's another state's name?").title()
    if answer_state =='Exit':
        break
    if answer_state in states:
        guessed_states.append(answer_state)
        answer_data = data_df[data_df['state']==answer_state]
        x,y = int(answer_data.x), int(answer_data.y)
        state = turtle.Turtle()
        state.hideturtle()
        state.up()
        state.goto(x,y)
        state.write(f"{answer_state}")
        

# states_to_learn.csv
states_to_learn= [state for state in states if state not in guessed_states]  # list comprehension
# for state in states:
#     if state not in guessed_states:
#         states_to_learn.append(state)
data_df = pd.Series(states_to_learn)
data_df.to_csv('Day25/US_States_Game/states_to_learn.csv')


# def get_mouse_click_coor(x,y):
#     print(x,y)
    
    
# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()
screen.exitonclick()