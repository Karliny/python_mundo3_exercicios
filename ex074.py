#Crie um programa que gere 6 numeros aleatorios e os coloque em uma tupla.
#mostre a listagem dos numeros gerados e indique o menor e o maior valor que estão na tupla
menor = maior = 0
from random import randint
for cont in range (0,5):
    numeros = randint(0,10)
    print(numeros)
    if cont == 1:
        menor = numeros
        maior = numeros
    else:
        if numeros > maior:
            maior = numeros
        elif numeros < menor:
            menor = numeros
print(f'O menor número gerado foi {menor} e o maior número foi {maior}')