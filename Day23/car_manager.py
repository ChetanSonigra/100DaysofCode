COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random

class CarManager(Turtle):
    def __init__(self, shape: str = "square", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.all_cars = []
        self.moving_speed = 0
        self.hideturtle()
    
    def move_car(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE+self.moving_speed)
            
    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance==1:
            new_car = Turtle('square')
            new_car.color(random.choice(COLORS))
            new_car.up()
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.goto(300,random.randint(-250,250))
            self.all_cars.append(new_car)
        
    def increase_speed(self):
        self.moving_speed += MOVE_INCREMENT

