#car = CarBluePrint() # object = class_name()   -- object constructor.

from turtle import Turtle, Screen
timmy = Turtle()          # creating object.
print(timmy)
timmy.shape('turtle')     # calling methods
timmy.color('coral')
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)  # Retrieving object variables.
my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column('Pokemon Name',['Pikachu','Squirtle','Charmander'])
table.add_column('Type',['electric','water','fire'])
print(table.align)
table.align = 'l'
print(table.align)
print(table)


# instance method and variables
class Test:
    count = 0                # class/static variable
    def __init__(self,a) -> None:    # self is not keyword, you can use any name instead.
        self.a = a          # instance variable
        Test.count += 1
    def fun(self):          # instance method
        self.b = 5
        
    @classmethod
    def count_read(cls):           # class method - can't access instance variables.
        print(cls.count)
        
    @staticmethod
    def is_sqaure(a,b):            # like global method, don't use class/instance variable. but related to class.
        if a==b:
            return True
        return False
    
    def get_a(self):
        return self.a
    
    def set_a(self,a):
        self.a = a
    
    
t = Test(1)
print(Test.count)
t2 = Test(4)
print(Test.count)
t.fun()
t.c = 10        # instance variable
print(dir(t))        
print(dir(Test))

Test.count_read()
t.count_read()   

print(dir(object))       # Every class inherits from object class by default.


# Inheritance: 
class Rectangle:
    def __init__(self,l,b) -> None:
        self.length =l
        self.breadth =b
        
    def perimeter(self):
        return 2*self.length*self.breadth
    
    def area(self):
        return self.length*self.breadth
    
class Cuboid(Rectangle):
    def __init__(self, l, b,h) -> None:
        super().__init__(l, b)
        self.height = h
        
    def volume(self):
        return self.length*self.breadth*self.height

c = Cuboid(1,2,3)
# method resolution order - mro
Cuboid.mro()

# Nested class: when there is lot of similar data repeating inside class. like billing address, shiping address
class Customer:
    def __init__(self,id,name,bdno,bstreet,bcity,bcountry,bpin,sdno,street,scity,scountry,spin) -> None:
        self.id = id
        self.name =name
        self.baddr = self.Address(bdno,bstreet,bcity,bcountry,bpin)
        self.saddr = self.Address(sdno,street,scity,scountry,spin)
        
    class Address:     
        def __init__(self,dno,street,city,country,pin) -> None:
            self.dno = dno
            self.street = street
            self.city = city
            self.country=country
            self.pin = pin
            
        def display(self):
            print(self.dno,self.street,self.city,self.country,self.pin,sep='\n')

c=Customer(1,'Chetan',101,'Mavdi','Rajkot','India',360004,222,'Udaynagar','Ahmedabad','India',340003)

c.baddr.display()


# Polymorphism: Duck Typing, operator overloading, method overloading, method overriding
# 1. Duck Typing: It doesn't matter which object, it should just have specific method.
def Petlover(pet):
    pet.talk()
    pet.walk()
    
class Duck:
    def talk(self):
        print('Duck is talking')
    def walk(self):
        print('Duck is walking')
        
class Dog:
    def talk(self):
        print('Dog is talking')
    def walk(self):
        print('Dog is walking')
        
d = Duck()
dg = Dog()
Petlover(d)
Petlover(dg)

# 2. Method Overloading: same method behaves differently based on parameters.
# for different data types and for different number of arguments.
import functools
class Arith:
    def sum(self,*args):
        total = functools.reduce(lambda x,y: x+y,args)
        return total
    

a = Arith()
a.sum(2,5,6,7)
a.sum('2','5','a')

# 3. Method overriding: 
class iPhone6:
    def home(self):
        print('Home button is pressed.')
        
class iPhoneX(iPhone6):
    def home(self):
        print('Home button is touched.')
        super().home()  
        
i6 = iPhone6()
ix =iPhoneX()

i6.home()
ix.home()      


# 4. Operator Overloading: __add__ method works differently for different type of data.
# you can create __add__ method for any class.
c = 8+3
d = 'a' + 'b'
print(c,d)


# Abstraction: Abstract Class and Interface
# abstract class can't be instantiated. purpose is to create a child class.
# It's used to enforce abstract method for child classes.
# Interface has all methods as abstract method, while Abstract class can have concrete method.

from abc import ABC,abstractmethod

class Parent(ABC):
    @abstractmethod
    def show(self):
        pass
    def display(self):
        print('This is display.')
        
class Child(Parent):
    def show(self):
        print('This is show.')

# p = Parent()  # Will throw error
c = Child()   # will throw error if show method is not defined.