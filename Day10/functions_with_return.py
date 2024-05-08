def format_name(fname: str,lname: str) -> str:   # annotations
    """Takes a first and last name and format it to return title case version of name.
    """
    # Above docstring shows up as documentation when we call function.
    if fname=='' or lname=='':
        return 'You did not provide valid inputs.'
    
    formated_f_name = fname.title()
    formated_l_name = lname.title()
    
    return f'{formated_f_name} {formated_l_name}'

output_name = format_name('CHETAN','sonigra')

output_name = format_name(input('What is your first name? '), input('What is your last name? '))
print(output_name)

print(format_name.__doc__)
help(format_name)
print(format_name.__annotations__)
"""
multiline comment
multiline comment
"""

# execution of function introduces a new 
# local symbol table used for local variables of the function.
# variables are looked first in local function, then in enclosing function, 
# then in global variables and then in built in names.

# to access global variables, use 'global'. 
# To access variables of enclosing function, use 'nonlocal'.

# function as object: f = display; f()
# function as parameter: f(add,3,5)
# nested function: outer,inner
# return function: s = outer(); s()

# def function(a,b,*args,c,**kwargs) 
# arguments before args must be positional and after args must be keyword
# def function(a,b,/,c,d,*,e,f) positional, any, keyword

# globals() - gives global variables
# locals() - gives local variables

# Iterators: i = iter(sequence); next(i);next(i)
# Generators: 
def gen():
    l = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    i= 0
    while True:
        i = i%7
        x = l[i]
        i +=1
        yield x

g = gen() 
next(g)
next(g)

# Closure function
def Closure(msg):
    greeting = 'Good day!'
    def display():
        print('*'*10)
        print(greeting,msg)   # can access nonlocal variable 
        print('*'*10)
    return display

d = Closure('Hellow')
d()

# Caller Class: 
# to make class/object callable with __call__ method
# can be converted into closure function.

# Decorator: 
def decorate(func):
    def wrapper(msg):
        print('*'*10)
        func(msg)
        print('*'*10)
    return wrapper

def display(name):
    print('Hello',name)
    
d = decorate(display)
d('Chetan')

@decorate
def display(name):
    print('Hello',name)

display('Chetan')


# Lambda: 
k = lambda miles: miles*1.6

print(k(10))

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(filter(lambda x: (x % 2 != 0), li))
print(final_list)

final_list = list(map(lambda x: x*2, li))
print(final_list)

import functools

sum = functools.reduce((lambda x, y: x + y), li)
print(sum)