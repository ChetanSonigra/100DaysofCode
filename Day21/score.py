from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Ariel',16,'normal')

class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.highscore =self.read_highscore()
        self.color('white')
        self.up()
        self.goto(0,276)
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.highscore=self.read_highscore()
        self.write(f"Score: {self.score} High Score: {self.highscore}",move=False,align='center',font=('Ariel',16,'normal'))
        
    def reset(self):
        if self.score>self.highscore:
            with open('Day21/highscore.txt','w') as f:
                f.write(str(self.score))
        self.score=0
        self.update_scoreboard()
        
    def increase_score(self):
        self.score +=1
        self.update_scoreboard()
        
    def read_highscore(self):
        with open('Day21/highscore.txt') as f:
            highscore=f.read()
        return int(highscore)
        
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write('Game Over!',move=False,align=ALIGNMENT,font=FONT)
        
    