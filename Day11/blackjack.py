## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random,os
from art import logo

cards = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']

def total(cards):
    """
    Calculates total score of cards.
    args: list containing cards
    returns: integer with total score.
    """
    
    cards_total = 0
    if cards.count('A')==3:
        return 13
    for x in cards:
        if isinstance(x,int):
            cards_total += x
        elif x in ('J','Q','K'):
            cards_total += 10

    countA = cards.count('A')
    for i in range(countA):
        if cards_total <11:
            cards_total += 11
        else:
            cards_total +=1
        
    return cards_total

def compare(user_total,computer_total):
    if user_total==computer_total or user_total>21 and computer_total>21:
        print('Draw!')
    elif user_total>21 and computer_total<=21:
        print('You lose!')
    elif user_total>computer_total or computer_total>21:
        print('You win!')
    else:
        print('You lose!')


while True:
    play = input('Do you want to play blackjack?(y/n)')
    if play=='n':
        break
    else:
        os.system('cls')
    
    print(logo)
    user_cards = []
    computer_cards = []
    for i in range(2):
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
        
    while True:
        print('Your cards: ',user_cards)
        print('computer\'s first card:', computer_cards[0])

        get_a_card = input("Type 'y' to get another card. Type 'n' to pass.")

        if get_a_card == 'y':
            user_cards.append(random.choice(cards))
        else:
            break

    while total(computer_cards)<17:
        computer_cards.append(random.choice(cards))

    user_total = total(user_cards)
    computer_total = total(computer_cards)
    
    print('Your final hand: ', user_cards)
    print("Computer's final hand: ",computer_cards)
    
    compare(user_total,computer_total)

