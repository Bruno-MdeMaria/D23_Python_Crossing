from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()   #sumir com a seta ou seja com a tartaruga
        self.penup()
        self.write(f"Level= {self.level}", align="left", font= FONT)

    
