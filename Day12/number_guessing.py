
import random

def check_number(guess, number):
    if guess == number:
        return 0
    elif guess>number:
        return 'Too high'
    else:
        return 'Too low'
        
def play():
    print('Welcome to the number guessing game!')
    print('I am thinking a number between 1 to 100.')
    choosen_number = random.randint(1,100)
    difficulty = input("Choose difficulty level. Type 'easy' or 'hard'.")
    
    if difficulty == 'hard':
        attempts = 5
    else:
        attempts = 8
    
    
    while attempts>0:
        print(f"You have {attempts} attempts remaining to guess a number.")
        guess = int(input('Make a guess: '))
        compare = check_number(guess,choosen_number)
        
        if compare == 0:
            print('You guessed it right!')
            return
        else:
            print(compare)
            attempts -=1
            if attempts >0:
                print('Guess Again')
        
    print(f'You have run out of attempts.The acutual answer was {choosen_number}')
    
play()