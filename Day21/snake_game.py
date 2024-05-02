# 1. Create a snake body.
# 2. Move the snake.
# 3. Control the snake.
# 4. Detect collision with food.
# 5. Create a score board.
# 6. Detect collision with wall.
# 7. Detect collision with tail.

import turtle,random,time
from snake import Snake
from food import Food
from score import ScoreBoard

tim = turtle.Turtle()

screen = turtle.Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)


snake=Snake()
food = Food()
scoreboard = ScoreBoard()


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
    
    
    # Detect collition with food.
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
        
    # Detect collition with wall.
    x,y = snake.head.pos()
    if not (-290<=x<=290 and -290<=y<=290):
        #turtle.TK.messagebox.showinfo(title='Game Over!',message=f'Final score: {scoreboard.score}')
        scoreboard.reset()
        snake.reset()
        
    
    # Detect collition with tail. 
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            scoreboard.reset()
            snake.reset()
            

screen.exitonclick()
