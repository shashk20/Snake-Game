from turtle import Turtle
import random
ALIGNMENT="center"
FONT=("Arial", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as data:
            self.highscore=int(data.read())
        self.color("white")
        self.penup()
        self.ht()
        self.setpos(0,260)

    def refresh(self):
        self.score+=8
        self.show()
    def reset(self):
        if self.score>self.highscore:
            with open("data.txt",mode="w") as new_data:
                new_data.write(str(self.score))
            self.highscore=self.score
        self.score=0
        self.show()

    def show(self):
        self.clear()
        self.write(f"Score:   {self.score} High Score: {self.highscore}", False, align=ALIGNMENT,font=FONT)