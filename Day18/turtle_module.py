from turtle import Turtle,Screen

timmy = Turtle()

timmy.shape('turtle')

timmy.color('red')        # color name comes from Tk module - Tk color specification string.


screen= Screen()
screen.setup(width=500,height=500)

# 1. draw a square

# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# 2. draw a dashed line

timmy.shape('arrow')
timmy.color('black')

# for i in range(15):
#     timmy.forward(10)
#     timmy.up()
#     timmy.forward(10)
#     timmy.down()


# 3. Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon

# shapes = {3:'peru',4:'yellow',5:'lime',6:'orange',7:'cyan',8:'violet',9:'dark salmon',10:'deep pink'}

# for s,col in shapes.items():
#     angle = 360/s
#     timmy.color(col)
#     for i in range(s):
#         timmy.forward(80)
#         timmy.right(angle)
        

# 4. Draw a random walk.
import random,turtle

# colors = ['peru','yellow','dark salmon','cyan','violet','deep pink','orange','lime','red'] 

turtle.colormode(255)
timmy.shape('arrow')
timmy.width(10)           # or timmy.pensize()


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r,g,b


dir = [0,90,180,270]
timmy.speed('fastest')

for i in range(1000):
    timmy.color(random_color())
    timmy.setheading(random.choice(dir))
    timmy.forward(30)
    x,y = timmy.position()
    if not (-200<x<200 or -200<y<200):
        timmy.undo()


# 5. Draw a circle with radius 100 at every side with some step value.  Spirograph
# import turtle

# turtle.colormode(255)


# timmy.speed('fastest')
# for i in range(0,360,10):
#     timmy.circle(100)
#     timmy.setheading(i)
#     timmy.color(random_color())


screen.exitonclick()