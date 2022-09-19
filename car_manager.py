from turtle import Turtle, st
import random

CORES = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        todos_cars = []


    def criar_carros(self):
       novo_car = Turtle("square")
       novo_car.penup()
       novo_car.shapesize(stretch_wid=2, stretch_len=1)
       novo_car.color(random.choice(CORES))
    
