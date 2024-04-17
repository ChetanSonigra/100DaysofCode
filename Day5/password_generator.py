import random

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
numbers = '1234567890'
specialcharacters = '!#$%&*()+'

print('Welcome to the password generator!')
no_of_letters = int(input('How many letters would you like?\n'))
no_of_numbers = int(input('How many numbers would you like?\n'))
no_of_specialcharacters = int(input('How many symbols would you like?\n'))

password =[]
for i in range(no_of_letters):
    password.append(random.choice(letters))
for i in range(no_of_numbers):
    password.append(random.choice(numbers))
for i in range(no_of_specialcharacters):
    password.append(random.choice(specialcharacters))
    
random.shuffle(password)
print('Here is your password: ', "".join(password))