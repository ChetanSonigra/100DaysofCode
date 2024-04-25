# 1. print report
# 2. check resources are sufficient?
# 3. process coins.
# 4. check transaction successful?
# 5. make a drink.
# 6. deduct resources.

from resources_data import MENU,resources
MONEY = 0

def is_resource_sufficient(item):
    """Checks if resources are sufficient to make a drink."""
    for resource in resources:
        if resources[resource] < MENU[item]['ingredients'].get(resource,0):
            print(f'Sorry, there is not enough {resource}.')
            return False

    return True

        
def take_coins():
    """Takes 4 inputs for money from users and returns total"""
    print('Please insert coins.')
    quarters = int(input('How many quarters?: '))
    dimes = int(input('How many dimes?: '))
    nickles = int(input('How many nickles?: '))
    pennies = int(input('How many pennies?: '))
    
    total = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
    
    return total

    
def adjust_resources(item):
    """Reduces resources based on item purchased"""
    for resource in resources:
        resources[resource] -= MENU[item]['ingredients'].get(resource,0)
    
    
is_on = True
while is_on:
    user_input = input('What would you like? (espresso/latte/cappuccino): ').lower()

    if user_input == 'report':
        for k,v in resources.items():
            if k =='coffee':
                print(f'{k}: {v}g')
            else:
                print(f'{k}: {v}ml')
        print(f"Money: ${MONEY}")
    elif user_input == 'off':
        is_on = False
    elif is_resource_sufficient(user_input):
        user_coins = take_coins()
        
        change = user_coins - MENU[user_input]['cost']
        
        if change<0:
            print("Sorry, that's not enough money. Money refunded.")
        else:
            adjust_resources(user_input)
            MONEY += MENU[user_input]['cost']
            print(f"Here is ${change} in change.")
            print(f'Here is your {user_input}. Enjoy..')
            
    