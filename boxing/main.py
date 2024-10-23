from classes import *
import random as rand

lut_boxeador1 = Boxeador('Muhammad Ali')
lut_muay_thai1 = Muay_Thai('Buakaw Banchamek')
lut_jujitsu1 = Jujitsu('Rickson Gracie')
lut_mma1 = MMA('Anderson Silva')
lut_mma2 = MMA('Khabib Nurmagomedov')

print(f'\nLuta entre: {lut_mma1.nome} e {lut_mma2.nome}!\n')

turno : bool
turno = 0
while(lut_mma1.energia > 0 and lut_mma2.energia > 0):
    turno = rand.choice([0,1])
    if turno == 0:
        ataque_escolhido = rand.choice([lut_mma1.cruzado,lut_mma1.chute_alto,
                                        lut_mma1.chave_braco,lut_mma1.gancho,
                                        lut_mma1.soco,lut_mma1.superman_punch])
        
        print(f'{lut_mma1.nome} atacou com {ataque_escolhido.__name__}!')
        ataque_escolhido(lut_mma2)
    elif turno == 1:
        ataque_escolhido = rand.choice([lut_mma2.cruzado, lut_mma2.chute_alto,
                                        lut_mma2.chave_braco,lut_mma2.gancho,
                                        lut_mma2.soco,lut_mma2.superman_punch])
        
        print(f'{lut_mma2.nome} atacou com {ataque_escolhido.__name__}!')
        ataque_escolhido(lut_mma1)
    if lut_mma1.energia <= 0:
        print(f'{lut_mma2.nome} ganhou!')
    elif lut_mma2.energia <= 0:
        print(f'{lut_mma1.nome} ganhou!')