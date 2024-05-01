from turtle import Turtle
ALIGN = 'center'
FONT = ("Arial",32,"normal")

class ScoreBoard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.color('white')
        self.up()
        self.hideturtle()
        self.score_l=0
        self.score_r=0
        self.goto(0,250)
        self.write(f"{self.score_l}  {self.score_r}",False,ALIGN,FONT)
        
    def update_l(self):
        self.score_l +=1
        self.clear()
        self.write(f"{self.score_l}  {self.score_r}",False,ALIGN,FONT)
        
    def update_r(self):
        self.score_r +=1
        self.clear()
        self.write(f"{self.score_l}  {self.score_r}",False,ALIGN,FONT)