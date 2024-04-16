import random

l = ['Rock','Paper','Scissor']

# Rock
l[0] = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
l[1] = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
l[2] = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
r='y'
while r.lower()=='y':
    user_choice = int(input('What do you choose? Type 0 for rock, 1 for paper, 2 for scissor.\n'))

    computer_choice = random.randint(0,2)
    if computer_choice==user_choice:
        print(l[user_choice])
        print(f'Computer choose:\n {l[computer_choice]}')
        print('Tie!!!')
    elif (computer_choice,user_choice) in [(0,2),(1,0),(2,1)]:
        print(l[user_choice])
        print(f'Computer choose:\n {l[computer_choice]}')
        print('You lose')
    else:
        print(l[user_choice])
        print(f'Computer choose: \n {l[computer_choice]}')
        print('You won!!')
    print('-'*40)
    r = input('This repl has exited.Run again?(Y/N): ')
    
