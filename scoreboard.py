from turtle import Turtle

FONT = ("Courier", 18, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()   #sumir com a seta ou seja com a tartaruga
        self.penup()
        self.goto(-270, 260)
        self.update_placar()
        
    def update_placar(self):
        self.clear()
        self.write(f"Level= {self.level}", align="left", font= FONT)

    def aumentar_nivel(self):
        self.level +=1
        self.update_placar()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font= FONT)

        
