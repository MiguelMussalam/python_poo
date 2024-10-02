import pickle
import csv
from typing import List
from common import *
from Interface_Eleicao import Transparencia

class Urna(Transparencia):
    mesario : Pessoa
    __secao : int
    __zona : int
    __eleitores_presentes : List[Eleitor] = []
    __votos = {} #dicionario chave = numero do candidato, valor é a quantidade de votos

    def __init__(self, mesario : Pessoa, secao : int, zona : int,
                 candidatos : List[Candidato], eleitores : List[Eleitor]):
        self.mesario = mesario
        self.__secao = secao
        self.__zona = zona
        self.__nome_arquivo = f'{self.__zona}_{self.__secao}.pkl'
        self.__candidatos = candidatos
        self.__eleitores = []
        for eleitor in eleitores:
            if eleitor.zona == zona and eleitor.secao == secao:
                self.__eleitores.append(eleitor)

        for candidato in self.__candidatos:
            self.__votos[candidato.get_numero()] = 0
        self.__votos['BRANCO'] = 0
        self.__votos['NULO'] = 0

        with open(self.__nome_arquivo, 'wb') as arquivo:
            pickle.dump(self.__votos, arquivo)

    def get_eleitor(self, titulo : int):
        for eleitor in self.__eleitores:
            if eleitor.get_titulo() == titulo:
                return eleitor
        return False

    def registrar_voto(self, eleitor : Eleitor, n_cand : int):
        self.__eleitores_presentes.append(eleitor)
        if n_cand in self.__votos:
            self.__votos[n_cand] += 1
        else:
            self.__votos['NULO'] += 1

        with open(self.__nome_arquivo, 'wb') as arquivo:
            pickle.dump(self.__votos, arquivo)

    def __str__(self):
        info =  f'Urna da seção {self.__secao}, zona {self.__zona}\n'
        info += f'Mesario {self.mesario}\n'
        return info
    
    def to_csv(self):
        with open(f'urna_{self.__zona}_{self.__secao}.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Seção', 'Zona', 'Titulo eleitor'])

            for eleitor in self.__eleitores:
                writer.writerow([self.__zona,self.__secao,eleitor.get_titulo()])

    def to_txt(self):
        with open(f'urna_{self.__zona}_{self.__secao}.txt', mode='w') as file:
            file.write(self.__str__())
            for eleitor in self.__eleitores:
                file.write(f'Titulo: {eleitor.get_titulo()}\n')

if __name__ == '__main__':

    mesario = Eleitor('mesas','100','200',27,50,100)

    c1 = Candidato('joao','1','2',1)
    c2 = Candidato('joberto','2','3',2)

    e1 = Eleitor('mogek','3','4',3,50,100)
    e2 = Eleitor('mojeg','4','5',4,50,100)

    urna = Urna(mesario,50,100,[c1,c2],[e1,e2])
    urna.to_csv()
    urna.to_txt()
