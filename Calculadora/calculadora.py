from abc import ABC,abstractmethod
from typing import List

class Operacao(ABC):
    operador : float

    def __init__(self,n):
        self.operador = n

    @abstractmethod
    def calcular(self,n : float):
        pass

    @abstractmethod
    def calcular_inverso(self,n : float):
        pass

class Adicao(Operacao):

    def calcular(self,n: float):
        return n + self.operador

    def calcular_inverso(self,n: float):
        return n - self.operador

class Subtracao(Operacao):

    def calcular(self,n: float):
        return n - self.operador

    def calcular_inverso(self,n: float):
        return n + self.operador

class Divisao(Operacao):
    
    def calcular(self,n : float):
        return n / self.operador
    
    def calcular_inverso(self, n: float):
        return n * self.operador

class Multiplicacao(Operacao):

    def calcular(self,n : float):
        return n * self.operador
    
    def calcular_inverso(self, n: float):
        return n / self.operador

class Calculadora():
    resultado : float = 0
    operacoes : List[Operacao] = []

    def add_operacao(self,op : Operacao):
        self.operacoes.append(op)

    def calcular_total(self):
        for op in self.operacoes:
            self.resultado = op.calcular(self.resultado)
            print(self.resultado)
        return self.resultado

    def desfazer_ultima(self):
        op = self.operacoes.pop()
        self.resultado = op.calcular_inverso(self.resultado)
        return self.resultado