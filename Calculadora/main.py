from calculadora import *

def menu():
    print('\nCALCULADORA')
    print('1. Digite números e sinais de operação para calcular...')
    print('2. (+ Adição) (* Multiplicação) (/ Divisão) (= Terminar operação) (z Desfazer ultima operação)\n')

def entrada():
    op = ''
    while op != 'q':
        if op == '+' or op == '-' or op == '*' or op == '/':
            n = float(input('>> '))

            if op == '+':
                o = Adicao(n)
            elif op == '-':
                o = Subtracao(n)
            elif op == '*':
                o = Multiplicacao(n)
            elif op == '/':
                o = Divisao(n)

            calculadora.add_operacao(o)

        elif op == '=':
            calculadora.calcular_total()
            print(f'>> {calculadora.resultado}')

        elif op == 'd':
            calculadora.desfazer_ultima()
            print(f'>> {calculadora.resultado}')

        else:
            print('>> Não entendi')

        op = input('>> ')

calculadora = Calculadora()
menu()
entrada()