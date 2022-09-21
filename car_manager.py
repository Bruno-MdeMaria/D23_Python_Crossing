from turtle import Turtle
import random

CORES = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVIMENTO_DISTANCIA = 5
AUMENTO_VELOCIDADE = 5


class CarManager:
    def __init__(self):
        self.todos_cars = []
        self.car_speed = MOVIMENTO_DISTANCIA


    def criar_carros(self):
       acada_random = random.randint(1,6)
       if acada_random == 1:
           novo_car = Turtle("square")
           novo_car.penup()
           novo_car.shapesize(stretch_wid=1, stretch_len=2)
           novo_car.color(random.choice(CORES))
           randon_y  = random.randint(-250,250)   #posição no eixo x que o carro será criado
           novo_car.goto(300, randon_y)
           self.todos_cars.append(novo_car)

    def mover_car(self):
        for car in self.todos_cars:
            car.back(self.car_speed)

    def subir_nivel(self):
        self.car_speed += AUMENTO_VELOCIDADE


