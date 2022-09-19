from turtle import Turtle


STARTING_POSITION = (0, -280)    #posição da tartle inicial         
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)    #turtle inicar virado para  norte


    def mover_up(self):
        pass