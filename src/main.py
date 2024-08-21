from frota import *


def operar_carro(carro: Carro):
    try:
        print('   <Primeiro carro>')
        print('1- Ligar motor')
        print('2- Desligar motor')
        print('3- Acelerar')

        op = 0
        while op not in (1, 2, 3):
            op = int(input("Digite as opcoes[1-3]: "))

        if op == 1:
                carro.ligar()
        elif op == 2:
            carro.desligar()
        elif op == 3:
            v = float(input("Informe a velocidade: "))
            t = float(input("Informe o tempo: "))
            carro.acelerar(v, t)

        print('Infos atuais do carro')
        print(carro)
    except Exception as e:
        print("Erro!")
        print(e)

if __name__ == "__main__":

    print('Cadastre o primeiro carro')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')

    kms = float(input('Digite com quantos Kms: '))

    carro1 = Carro(nm_modelo, nm_marca, nm_cor, kms, motor = False)

    print('Cadastre o segundo carro')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')

    kms = float(input('Digite com quantos Kms: '))
    carro2 = Carro(nm_modelo, nm_marca, nm_cor,kms, motor = False)

    '''
    Controlando os carros até eles atingirem 600 Km
    '''
    while carro1.odometro < 600 and carro2.odometro < 600:
        print('Deseja operar qual carro?')
        print(f'1 -{carro1.modelo}')
        print(f'2 -{carro2.modelo}')
        try:
            x = int(input())
            if x == 1:
                operar_carro(carro1)
            if x == 2:
                operar_carro(carro2)
        except Exception as e:
            print("Erro!")
            print(e)

    carro1.desligar()
    carro2.desligar()
    if carro1.odometro >= 600:
        print('Carro 1 chegou ao destino primeiro.')
    else:
        print('Carro 2 chegou ao destino primeiro')


