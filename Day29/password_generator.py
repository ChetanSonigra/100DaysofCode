
def generate_password():
    import random

    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    numbers = '1234567890'
    specialcharacters = '!#$%&*()+'

    # print('Welcome to the password generator!')
    no_of_letters = random.randint(8,10)
    no_of_numbers = random.randint(2,4)
    no_of_specialcharacters = random.randint(2,4)

    password =[]
    password_letters = [random.choice(letters) for i in range(no_of_letters)]
    password_numbers = [random.choice(numbers) for i in range(no_of_numbers)]
    password_sps = [random.choice(specialcharacters) for i in range(no_of_specialcharacters)]
        
    password = password_letters + password_numbers + password_sps
    random.shuffle(password)
    
    return "".join(password)
