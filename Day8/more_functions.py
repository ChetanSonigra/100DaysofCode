def greet():
    print('Hello Chetan')
    print('How do you do Chetan?')
    print("Isn't the whether nice today?")

greet()

# function that allows for input

def greet_with_name(name):         #  name is parameter
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    
greet_with_name('Ram')             # 'Ram' - actual value passed is argument.

# function with more than one input

def greet(name,location):
    print(f'Hello {name}')
    print(f"What is it like in {location}")

greet('Chetan','Rajkot')
greet('Rajkot','Chetan')      # positional arguments

greet(location='Rajkot',name='Chetan')  # keyword arguments.


def paint_calc(height,width,cover):
  import math
  cans = math.ceil(height*width/cover)
  print(f"You'll need {cans} cans of paint.")
   

test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


def prime_checker(number):
  for i in range(2,number//2):
    if number%i==0:
      print("It's not a prime number.")
      return
  print("It's a prime number.")

n = int(input()) # Check this number
prime_checker(number=n)