from turtle import Turtle


POSICAO_INICIAL = (0, -280)    #posição da tartle inicial         
MOVER_DISTANCIA = 10
FINAL_LINHA_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.restart_posi()   #criado após a função criada abaixo para usar também quando travessia com exito
        self.setheading(90)    #turtle inicar virado para  norte


    def mover_up(self):
        self.forward(MOVER_DISTANCIA)

    def restart_posi(self):
        self.goto(POSICAO_INICIAL)
   
    def linha_chegada(self):
        if self.ycor() > FINAL_LINHA_Y:
            return True
        else: return False


