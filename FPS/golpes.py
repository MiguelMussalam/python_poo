from abc import ABC,abstractmethod

class Golpe(ABC):

    @abstractmethod
    def golpear(self,jogador):
        pass


class Soco(Golpe):

    def golpear(self, jogador):
        jogador.energia -= 1

class Chute(Golpe):

    def golpear(self, jogador):
        jogador.energia -= 2