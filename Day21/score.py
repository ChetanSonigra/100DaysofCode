from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Ariel',16,'normal')

class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color('white')
        self.up()
        self.goto(0,276)
        self.hideturtle()
        self.write(f"Score: {self.score}",move=False,align=ALIGNMENT,font=FONT)
        
    def update(self):
        self.score +=1
        self.clear()
        self.write(f"Score: {self.score}",move=False,align='center',font=('Ariel',16,'normal'))
        
    def game_over(self):
        self.goto(0,0)
        self.write('Game Over!',move=False,align=ALIGNMENT,font=FONT)
        
    