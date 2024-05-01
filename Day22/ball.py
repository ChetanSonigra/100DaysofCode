import turtle

class Ball(turtle.Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.up()
        self.x_move =10
        self.y_move =10
        self.move_speed =0.1
        
    def move(self):
        x = self.xcor()+self.x_move
        y = self.ycor()+self.y_move
        self.goto(x,y)
        
    def bounce_y(self):
        self.y_move*=-1
        
    def bounce_x(self):
        self.x_move*=-1
        
    def refresh(self):
        self.goto(0,0)
        
    def fast(self):
        if self.move_speed>0:
            self.move_speed*=0.9