fruits =['Apple','Peach','Pear']

for fruit in fruits:
    print(fruit + 'Pie')
    
print(fruits,fruit)

for i in range(1,11,3):
    print(i)
    
for i, v in enumerate(['tic', 'tac', 'toe']): # using enumerate to get index and value at same time.
    print(i, v)

# break statement breaks out of innermost for/while loop.
# else can be used with for/while loop.
# else is not executed if loop is terminated with break.
for i in range(1,10):
    if i%5==0:
        break
else:
    print('loop did not break')
    
# continue continues the loop for next iteration
i =1
while i<10:
    if i%3==0:
        i+=1
        continue
    print(i)
    i+=1
    
# pass does nothing.
# it can be used when statement is required syntactically but program requires no action.
# commonly used for creating minimal classes.
class A:
    pass

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418|490:                     # you can combine multiple literals
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
