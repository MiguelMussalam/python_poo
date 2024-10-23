from abc import ABC,abstractmethod

class Lutador(ABC):
    nome : str
    energia : float

    def __init__(self,nome):
        self.nome = nome
        self.energia = 100
    
    def soco(self,oponente : 'Lutador'):
        if oponente.energia > 0:
            oponente.energia -= 5.5
        print(f'Energia do {oponente.nome}: {oponente.energia:.2f}\n')

    def __str__(self):
        return f'Nome: {self.nome}\nEnergia: {self.energia}\n'


class Boxeador(Lutador):

    def cruzado(self, oponente: Lutador):
        if oponente.energia > 0:
            oponente.energia = max(0, oponente.energia - 10.2)
        print(f'Energia do {oponente.nome}: {oponente.energia:.2f}\n')

    def gancho(self, oponente: Lutador):
        if oponente.energia > 0:
            oponente.energia = max(0, oponente.energia - 20.8)

        print(f'Energia do {oponente.nome}: {oponente.energia:.2f}\n')
        
    
class Muay_Thai(Boxeador):

    def chute_alto(self, oponente: Lutador):
        if oponente.energia > 0:
            oponente.energia = max(0, oponente.energia - 15.4)

        print(f'Energia do {oponente.nome} {oponente.energia:.2f}\n')
        

class Jujitsu(Lutador):

    def chave_braco(self, oponente: Lutador):
        if oponente.energia > 0:
            oponente.energia = max(0, oponente.energia - 100)
        print(f'Energia do {oponente.nome}: {oponente.energia:.2f}\n')
        
class MMA(Muay_Thai,Jujitsu):

    def superman_punch(self, oponente: Lutador):
        if oponente.energia > 0:
            oponente.energia = max(0, oponente.energia - 53.2)
        print(f'Energia do {oponente.nome}: {oponente.energia:.2f}\n')