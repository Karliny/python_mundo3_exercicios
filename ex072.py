#Crie um programa que tenha uma tupla preenchida totalmente com os numeros por extenso de zero a vinte. Seu programa deverá ler um numero no teclado de 0 a 20 e mostrar ele por extenso
while True:
    numeros = ('zero','um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
    escolha = int(input('Escolha um número entre 0 e 10: '))
    if escolha > 0 and escolha <= 10:
        print(f'Você escolheu o número: {numeros[escolha]}')
    else:
        print('Você só pode escolher um número entre 0 e 10')