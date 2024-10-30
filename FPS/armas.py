from abc import ABC, ABCMeta,abstractmethod
from golpes import *

class Arma(ABC):
    destruicao : float

    def __init__(self,destruicao):
        self.destruicao = destruicao
    
    def agredir(self,jogador):
        jogador.energia -= 5
    
    def __str__(self):
        return f'Poder de destruição: {self.destruicao}\n'

class Disparavel(metaclass= ABCMeta):
    
    @abstractmethod
    def disparar(self,jogador):
        pass

    @abstractmethod
    def recarregar(self):
        pass

class Revolver(Arma,Disparavel):
    cartuchos : int = 6

    def __init__(self):
        self.destruicao = 20

    def disparar(self,jogador):
        if self.cartuchos > 0:
            self.cartuchos -= 1
            jogador.energia -= self.destruicao
        else:
            print('Sem municão, necessário recarregar!\n')

    def recarregar(self):
        self.cartuchos = 6

class Lanca_Chamas(Arma,Disparavel):
    gas : float

    def __init__(self):
        self.gas = 100
        self.destruicao = 30
    
    def disparar(self, jogador):
        if self.gas >= 5.5:
            self.gas -= 5.5
            jogador.energia -= self.destruicao
        else:
            print('Sem gas, necessário recarregar!\n')
    
    def recarregar(self):
        self.gas = 100

class Faca(Arma):
    lamina : int
    def __init__(self):
        self.lamina = 10
        self.destruicao = 15

    def agredir(self, jogador):
        if self.lamina > 0:
            jogador.energia -= 15
            self.lamina -= 1
        else:
            jogador.energia -= 5
    
class Soco_Ingles(Faca,Soco):

    def __init__(self):
        super().__init__()
        self.destruicao = 20
    
    def agredir(self,j):
        super().agredir(j)
        self.golpear(j)

