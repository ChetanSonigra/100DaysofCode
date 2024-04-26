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
