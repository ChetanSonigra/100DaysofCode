# STEPS:
# 1. Create the screen.
# 2. Create and move paddle.
# 3. Create another paddle.
# 4. Create the ball andmake it move.
# 5. Detect collosion with wall and bounce.
# 6. Detect collision with paddle.
# 7. Detect when paddle misses.
# 8. Keep score

import turtle,time
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = turtle.Screen()
screen.setup(800,600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

paddle_r=Paddle(350,0)
paddle_l=Paddle(-350,0)
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(paddle_r.go_up,'Up')
screen.onkeypress(paddle_r.go_down,'Down')
screen.onkeypress(paddle_l.go_up,'W')
screen.onkeypress(paddle_l.go_down,'S')

game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    # Detect collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
        
    # Detect ball miss
    if ball.xcor()>360:
        ball.refresh()
        ball.bounce_x()
        scoreboard.update_l()
    
    if ball.xcor()<-360:
        ball.refresh()
        ball.bounce_x()
        scoreboard.update_r()
    
    # Detect collision with paddle
    if 20<=ball.distance(paddle_r)<50 and ball.xcor()>330 or 20<=ball.distance(paddle_l)<50 and ball.xcor()<-330:
        ball.bounce_x()
        ball.fast()
        
screen.exitonclick()

