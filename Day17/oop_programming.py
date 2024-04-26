class User():     # class name is generally in Pascal case.
    def __init__(self,id, name) -> None:     # special method to initialize
        print('User is being created.')
        self.id = id
        self.name = name
        self.followers = 0
        self.following = 0
        
    def follow(self,user):
        user.followers += 1
        self.following += 1
        
# user_1 = User()
# user_1.id = '001'
# user_1.name = 'Chetan'   # This way of assigning variables is difficult for every object.

user_1 = User('001','Chetan')
user_2 = User('002','Ram')
print(user_1.name)

user_1.follow(user_2)
print(user_1.followers,user_1.following, user_2.followers,user_2.following)

# So in python we have constructor/initialization. 
# 1. To set variables,counters,switches to their starting value at the beginning of program/subprogram.
# 2. To clear of previous data in preparation of use. 

class Car():
    def __init__(self,seats) -> None:
        self.seats = seats
    
    def enter_race_mode(self):
        self.seats = 2
my_car = Car(6)