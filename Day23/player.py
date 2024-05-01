STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):
    def __init__(self, shape: str = "turtle", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.color('blue')
        self.up()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        
    def move(self):
        self.forward(MOVE_DISTANCE)
        
    def is_at_finishline(self):
        return self.ycor()>=FINISH_LINE_Y
    
    def goto_start(self):
        self.goto(STARTING_POSITION)
            
            
