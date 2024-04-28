import turtle

tim = turtle.Turtle()
screen = turtle.Screen()

def move_forward():
    tim.forward(10)
    
def move_backward():
    tim.backward(10)
    
def counter_clockwise():
    
    tim.setheading(tim.heading()+10)
    
def clockwise():
    tim.setheading(tim.heading()-10)

def clear_screen():
    tim.clear()
    tim.up()
    tim.home()
    tim.down()

screen.listen()
screen.onkey(key='W',fun=move_forward)
screen.onkey(key='S',fun=move_backward)
screen.onkey(counter_clockwise,'A')
screen.onkey(clockwise,'D')
screen.onkey(key='C',fun=clear_screen)


screen.exitonclick()

