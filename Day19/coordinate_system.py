# You can have many number of turtle objects. 
# Each has it's behaviour and attribute independently.

import turtle,random

#tim = turtle.Turtle()

screen = turtle.Screen()

screen.setup(500,400)

is_race_on = False

user_bet = screen.textinput('Make Your Bet','Which turtle will win the race? Enter a color: ')


turtles = []
colors = ['red','orange','green','blue','purple','yellow']

for i in range(6):
    tim = turtle.Turtle(shape='turtle')
    tim.color(colors[i])
    turtles.append(tim)

i = 0
for t in turtles:
    t.up()
    t.goto(-230,-100+i)
    i +=35
    
if user_bet:
    is_race_on=True

while is_race_on:
    for t in turtles:
        if t.xcor()>230:
            is_race_on=False
            winning_turtle=t.pencolor()
            if winning_turtle == user_bet:
                print(f'You have won! The {winning_turtle} turtle is the winner!')
                turtle.TK.messagebox.showinfo(title='Race Results',message=f'You have won! The {winning_turtle} turtle is the winner!')
            else:
                print(f'You lost! The {winning_turtle} turtle is the winner!')
                turtle.TK.messagebox.showinfo(title='Race Results',message=f'You have lost! The {winning_turtle} turtle is the winner!')
                
        rand_distance=random.randint(0,10)
        t.forward(rand_distance)

screen.exitonclick()