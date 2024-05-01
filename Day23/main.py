import time,random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

cars=[]
player = Player()
scoreboard= Scoreboard()
carmanager = CarManager()

screen.listen()
screen.onkeypress(player.move,'Up')

game_is_on = True
c=0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    carmanager.create_car()
    carmanager.move_car()
    for car in carmanager.all_cars:
        # Detect collision with cars
        if player.distance(car)<20:
            scoreboard.game_over()
            game_is_on=False
            
            
        # Detect successful crossing.
        if player.is_at_finishline():
            player.goto_start()
            carmanager.increase_speed()
            scoreboard.level_up()
        
        
    c+=1
    

screen.exitonclick()