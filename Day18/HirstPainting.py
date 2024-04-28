import random,turtle,colorgram

# colors = colorgram.extract('Day18/image.jpg',30)

# colors_list = []

# for c in colors:
#     r = c.rgb.r
#     g = c.rgb.g
#     b = c.rgb.b
#     colors_list.append((r,g,b))
    
colors_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
turtle.colormode(255)

timmy = turtle.Turtle()
timmy.hideturtle()
timmy.up()
timmy.goto((-225,-200))
timmy.down()

for i in range(10):
    for j in range(10):
        timmy.dot(20,random.choice(colors_list))
        timmy.up()
        timmy.forward(50)
        timmy.down()
    timmy.up()
    timmy.left(90)
    timmy.forward(50)
    timmy.right(90)
    timmy.backward(500)
    timmy.down()

    
screen = turtle.Screen()
screen.exitonclick()