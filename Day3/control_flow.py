# if , elif, elif, else
# if , else
# if, if , else,else - nested if else.
# comparison operator: <,>,==, !=,<>, <=,>=
# logical operator: not(~),and(&), or(|)
print('''
      *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
      ''')
print('Welcome to the treasure island.\nYour mission is to find the treasure.')
l_or_r = input('You are at cross road, do you want to go left or right?')
if l_or_r.lower() !='left':
    print('Game Over!')
else:
    s_or_w =input('You came to a lake, there is an island in the middle of lake. Type "wait" to wait for a boat.Type "swim" to swim across.')
    if s_or_w.lower() != 'wait':
        print('Game Over!')
    else:
        color= input('You arrived at an island unharmed. There is a house with 3 doors. One red, one yellow, one blue. Which one do you choose?')
        if color.lower()!='yellow':
            print('You entered the room of beasts. Game Over!')
        else:
            print('You found the treasure. You won!!!')
            
                    