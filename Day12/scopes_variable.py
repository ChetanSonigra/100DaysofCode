# execution of function introduces a new 
# local symbol table used for local variables of the function.
# variables are looked first in local function, then in enclosing function, 
# then in global variables and then in built in names.

# to access global variables, use 'global'. 
# To access variables of enclosing function, use 'nonlocal'.

x = 1
y = 10
def increment():
    #global x         # to modify global variable. this is falliable though and not recommended.
    x = 2
    print('x inside function: ', x)
    print('y inside function: ', y)
    
increment()
print('x outside fucntion: ', x)
print('y outside function: ', y)

# function inside another function can be called in the function only, not globally.
def exeternal_function():
    def internal_function():
        a = 7 
        b = 10
        return a+b
    return internal_function()

# internal_function() can't be called outside exeternal_function()

# You should define global variables with capital letters.
TWITTER_URL = 'www.twitter.com'
PI = 3.14
