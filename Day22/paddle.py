from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x,y,shape: str = "square", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.color('white')
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.up()
        self.goto(x,y)
        
    def go_up(self):
        new_y = self.ycor() + 20
        if new_y<260:
            self.goto(self.xcor(),new_y)
        
    def go_down(self):
        new_y = self.ycor() - 20
        if new_y>-260:
            self.goto(self.xcor(),new_y)