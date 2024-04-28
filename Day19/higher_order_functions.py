def add(n1,n2):
    return n1+n2
    
def substract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2
    
def divide(n1,n2):
    return n1/n2

def calculator(n1,n2,func):          # calculator is higher order function.
    return func(n1,n2)

result = calculator(5,6,add)
print(result)