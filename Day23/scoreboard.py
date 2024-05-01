FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color('black')
        self.up()
        self.hideturtle()
        self.goto(-260,260)
        self.level = 1
        self.write(f"LEVEL: {self.level}",False,'left',FONT)
        
    def level_up(self):
        self.level += 1
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"LEVEL: {self.level}",False,'left',FONT)
        
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over!",False,'center',FONT)
