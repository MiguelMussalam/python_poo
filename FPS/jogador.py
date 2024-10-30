from armas import *
from golpes import *
from typing import List
class Jogador():
    energia : float
    armas : List[Arma]

    def __init__(self):
        self.energia = 150
        self.armas : List[Arma] = []
    
    def add_arma(self,arma : Arma):
        self.armas.append(arma)

    def atirar(self,disparavel : Disparavel, jogador : 'Jogador'):
        disparavel.disparar(jogador)

    def bater(self,golpe : Golpe = None, arma : Arma = None, jogador : 'Jogador' = None):
        if golpe is not None:
            golpe.golpear(jogador)
        elif arma is not None:
            arma.agredir(jogador)
        
    def __str__(self):
        return f'Energia: {self.energia}\n'