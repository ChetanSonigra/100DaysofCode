# Describe the problem.
def my_function():
    for i in range(1,20):
        if i == 20:
            print('Hello')
my_function()  # problem: doesn't print Hello

# Reproduce the bug.
from random import randint
images=[1,2,3,4,5,6]
num= randint(1,6)     # set num=1,2,3,4,5,6 to reproduce the bug.
print(images[num])

# Evaluate each line. rubber duck
year = int(input('What is your birth year?'))
if year>1980 and year<1994:
    print('You are millenial.')
elif year>1994:
    print('You are GenZ.')


# Fixing errors and watching for red underlines.
'''a = input('Enter your age: ')
if a>18:
print('adult')  '''        # red underlines.
# type error 


# print 
pages=0
words_per_page=0
pages =int(input('Number of pages: '))
words_per_page==int(input('Words per page: '))  # extra '='
total_words =pages*words_per_page
print(f"pages = {pages}")
print(f"words per page = {words_per_page}")
print(total_words)

# Use a debugger - pythontutor.com to visualize execution.
def mutate(a_list):
    b_list = []
    for i in a_list:
        new_item = i*2
    b_list.append(new_item)
mutate([1,2,4,6,19])

# Take a break.
# Ask someone else.
# Run your code often.
# Ask stackoverflow.