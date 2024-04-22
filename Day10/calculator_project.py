from art import logo

def add(n1,n2):
    return n1+n2
       
def substract(n1,n2):
    return n1-n2
    
def multiply(n1,n2):
    return n1*n2
    
def divide(n1,n2):
    return n1/n2

operations = {'+':add, '-':substract, '*':multiply, '/': divide}

# using answer from previous function call is not possible if we are using print statements.
def calculator():
    
    print(logo)
    
    num1 = float(input('What is the first number? '))
    should_continue = True

    for symbol in operations:
        print(symbol)
    while should_continue:
        
        operation_symbol = input('Pick an operation from above: ')
        num2 = float(input('What is the next number? '))
        
        answer = operations[operation_symbol](num1,num2)
        print(f'{num1} {operation_symbol} {num2} = {answer}')
        ask_a_user = input(f"Type 'y' to continue calculating with {answer}, 'n' to exit.: ")
        
        if ask_a_user == 'n':
            should_continue=False
            calculator()                      # recursion - similar to while loop take care of infinite recursion.
        else:
            num1=answer
    
calculator()