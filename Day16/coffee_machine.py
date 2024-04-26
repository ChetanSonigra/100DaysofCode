from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()

money_machine = MoneyMachine()

coffee_maker = CoffeeMaker()

should_continue = True

while should_continue:
    user_input = input(f'What would you like? {menu.get_items()}: ')
    
    if user_input == 'off':
        should_continue = False
    elif user_input == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_input)
        if drink:
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
                
                       