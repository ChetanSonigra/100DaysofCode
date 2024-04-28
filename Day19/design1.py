import turtle

def draw_attractive_design():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    pen = turtle.Turtle()
    pen.speed(10)
    turtle.bgcolor("black")  
    pen.pensize(2)

    size = 20

    for i in range(300):
        pen.color(colors[i % 6])
        pen.forward(size)
        pen.left(59)
        pen.forward(size)
        pen.left(59)
        pen.forward(size)
        pen.left(59)
        pen.forward(size)
        pen.left(121)
        size += 2  

    pen.hideturtle()

def draw_attractive_design1():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    pen = turtle.Turtle()
    pen.speed('fastest')
    turtle.bgcolor("black")  
    pen.pensize(2)

    size = 20
    for i in range(100):
        for i in range(0,360,10):
            pen.color(colors[i%6])
            pen.circle(size)
            pen.setheading(i)
        size +=5
    pen.hideturtle()

draw_attractive_design1()

turtle.done()