import random

a = random.randint(1,3)
print(a)

b = random.random(); print(b) # 0.0 to 1.0(1 excluded) [0.0,1.0)

c = random.choice(['Apple','Grapes','Orange'])
print(c)

d = random.uniform(1.0,2.0) 
print(d)

e = ['Apple','Grapes','Orange']
random.shuffle(e)
print(e)

f = random.randrange(1,31,3)
print(f)

i =0
while i<9:
    random.seed(i)
    print(random.randint(0,50))
    i+=1
    
# random module can be used in sampling and to get random numbers based on specific distribution like normal, gauss etc.