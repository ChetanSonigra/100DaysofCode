# 1. Create a snake body.
# 2. Move the snake.
# 3. Control the snake.
# 4. Detect collision with food.
# 5. Create a score board.
# 6. Detect collision with wall.
# 7. Detect collision with tail.

import turtle,random,time
from snake import Snake

tim = turtle.Turtle()

screen = turtle.Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake=Snake()

screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.right,'Right')
screen.onkey(snake.left,'Left')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()


screen.exitonclick()
