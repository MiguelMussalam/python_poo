from jogador import *

#Jogadores
jogador1 = Jogador()
jogador2 = Jogador()
print(f'Jogador 1 - {jogador1}')
print(f'Jogador 2 - {jogador2}')

#Armas e golpes
faca = Faca()
soco_ingles = Soco_Ingles()
lanca_chamas = Lanca_Chamas()
revolver = Revolver()
soco = Soco()
chute = Chute()

jogador1.add_arma(faca)
jogador1.add_arma(revolver)
print(f'Armas do jogador: {jogador1.armas}\n')

print(f'faca - {faca}')
print(f'Soco inglês - {soco_ingles}')
print(f'Lanca-Chamas - {lanca_chamas}')
print(f'Revolver - {revolver}')

print('Atirando com um Revolver:')
jogador1.atirar(jogador1.armas[1],jogador2)
print(f'Jogador 1 - {jogador1}')
print(f'Jogador 2 - {jogador2}')

print('Batendo com uma faca:')
jogador1.bater(arma= jogador1.armas[0],jogador= jogador2)
print(f'Jogador 1 - {jogador1}')
print(f'Jogador 2 - {jogador2}')
print(f'Fiação da faca: {jogador1.armas[0].lamina}\n')

# Teste da Faca e fiação - funcionando
"""
for i in range(11):
    jogador1.bater(arma= faca,jogador= jogador2)
    print(f'Jogador 1 - {jogador1}')
    print(f'Jogador 2 - {jogador2}')
    print(f'Fiação da lâmina: {faca.lamina}')
"""

# Teste do Soco Inglês - funcionando
"""
for i in range(11):
    jogador1.bater(arma=soco_ingles,jogador= jogador2)
    print(f'Jogador 1 - {jogador1}')
    print(f'Jogador 2 - {jogador2}')
    print(f'Fiação da lâmina: {soco_ingles.lamina}\n')
"""

# Teste do Lança-Chamas - Funcionando
"""
for i in range(11):
    jogador1.atirar(lanca_chamas, jogador2)
    print(f'Jogador 1 - {jogador1}')
    print(f'Jogador 2 - {jogador2}')
    print(f'Gas do Lança-Chamas: {lanca_chamas.gas}\n')
lanca_chamas.recarregar()
print(f'Gas do Lança-Chamas após recarregar: {lanca_chamas.gas}\n')
"""

# Teste do Revolver - Funcionando
"""
for i in range(7):
    jogador1.atirar(revolver, jogador2)
    print(f'Jogador 1 - {jogador1}')
    print(f'Jogador 2 - {jogador2}')
    print(f'Cartucho do Revolver: {revolver.cartuchos}\n')
revolver.recarregar()
print(f'Cartucho do Revolver após recarregar: {revolver.cartuchos}\n')
"""

# Teste do Soco - Funcionando
"""
for i in range(10):
    jogador1.bater(golpe= soco, jogador= jogador2)
    print(f'Jogador 1 - {jogador1}')
    print(f'Jogador 2 - {jogador2}')
"""

# Teste do Chute - Funcionando
"""
for i in range(10):
    jogador1.bater(golpe= chute, jogador= jogador2)
    print(f'Jogador 1 - {jogador1}')
    print(f'Jogador 2 - {jogador2}')
"""