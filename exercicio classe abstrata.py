from abc import ABC, abstractmethod

class Funcionario(ABC):
    nome : str
    cpf : str
    __senha : int

    def __init__(self,nome,cpf,senha):
        self.nome = nome
        self.cpf = cpf
        self.__senha = senha

    @abstractmethod
    def autenticar(self,user: str, senha: int):
        pass

    def get_senha(self):
        return self.__senha

    def __str__(self):
        return f'Nome: {self.nome}\nCPF: {self.cpf}\n'

class Gerente(Funcionario):

    def autenticar(self, user: str, senha: int):
        if (self.cpf == user) and (self.get_senha() == senha):
            return 1
        else:
            return 0
    
    def cancelar_operacao(self):
        return f'Operação cancelada'

class Operador_caixa(Funcionario):

    numero_caixa : int

    def __init__(self, nome, cpf, senha,numero_caixa):
        super().__init__(nome, cpf, senha)
        self.numero_caixa = numero_caixa

    def autenticar(self, user: str, senha: int):
        if (self.numero_caixa == int(user)) and (self.get_senha() == senha):
            return 1
        else:
            return 0
    
    def registrar_produto(self):
        return f'Produto registrado'

    def __str__(self):
        return f'{super().__str__()}Numero caixa: {self.numero_caixa}\n'

class Seguranca(Funcionario):

    posto : int

    def __init__(self, nome, cpf, senha,posto):
        super().__init__(nome, cpf, senha)
        self.posto = posto

    def autenticar(self, user: str, senha: int):
        if (self.posto == user) and (self.get_senha() == senha):
            return 1
        else:
            return 0
    
    def acionar_alarme(self):
        return f'Alarme acionado'

    def __str__(self) -> str:
        return f'{super().__str__()}Posto: {self.posto}\n'
    

if __name__ == '__main__':

    gerente = Gerente('gus fring','111222',123)
    operador_caixa = Operador_caixa('john','333444',456,5)
    seguranca = Seguranca('Mike','555666',789,5)

    print(gerente)
    print(operador_caixa)
    print(seguranca)

    print(f'Autenticação gerente:{gerente.autenticar("111222",123)}')
    print(f'Autenticação operador caixa:{operador_caixa.autenticar("5",456)}')
    print(f'Autenticação segurança:{seguranca.autenticar(5,789)}')

    print(gerente.cancelar_operacao())
    print(operador_caixa.registrar_produto())
    print(seguranca.acionar_alarme())