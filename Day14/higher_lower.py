# checkout https://www.higherlowergame.com/

from art import logo,vs
import random,os
from game_data import data


def check_answer(user_input,a_follower,b_follower):
    if a_follower>b_follower:
        return user_input == 'A'
    else:
        return user_input == 'B'


print(logo)

should_game_continue = True
score = 0
choice2 = random.choice(data)

while should_game_continue:
    
    choice1 = choice2

    choice2 = random.choice(data)
    while choice1==choice2:
        choice2 = random.choice(data)
    
    #print(choice1,choice2)
    
    print(f"Compare A: {choice1['name']}, A {choice1['description']} from {choice1['country']}.")
    print(vs)
    print(f"Against B: {choice2['name']}, A {choice2['description']} from {choice2['country']}.")
    
    user_input = input('Who has more follower? Type A or B: ')
    
    os.system('cls')
    print(logo)
    
    if check_answer(user_input,choice1['follower_count'],choice2['follower_count']):   
        score +=1
        print('You are right. Current score:',score)
    else:
        should_game_continue = False
        print("Sorry, that's wrong. Final score: ", score)
