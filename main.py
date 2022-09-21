import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)



#OBJETOS:

player = Player()
car_maneger = CarManager()

screen.listen() #ouviro o teclado (evento)
screen.onkeypress(player.mover_up,"Up")




game_is_on = True
while game_is_on:
    time.sleep(0.1)      #o loop acontecerá a cada 0,1 segundo.
    screen.update()
    
    car_maneger.criar_carros() #criará um novo carro a cada atualização do screen que ocorre´ra a cada 0,1 seg.
    car_maneger.mover_car()

screen.exitonclick()
