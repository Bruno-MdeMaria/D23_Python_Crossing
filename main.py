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

    #detectando colisão com o carro:
    for car in car_maneger.todos_cars:   #para cada carro em lista de carros:
        if car.distance(player) < 20:    #se o carro da lista estiver a uma distancia menor que 20 do obejto player:
            game_is_on = False

    #detectando o fim da travessia do player:
    if player.linha_chegada():   # se o return for True (no método linha_chegada return True ou False):
        player.restart_posi()
        car_maneger.aumentar_nivel()


screen.exitonclick()
