FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()
        self.setposition(-230,260)
        self.level=1

    def writee(self):
        self.write(f"Level {self.level}",False,"center",FONT)

    def add_level(self):
        self.level+=1
        self.clear()
        self.writee()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",False,"center",FONT)


