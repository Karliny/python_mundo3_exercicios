lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range (0,len(lanche)):
    print(f'Eu vou comer {lanche[con]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

#SORTED É UM MÉTODO QUE ORGANIZA A TUPLA EM ORDEM ALFABETICA
#Nas tuplas podem haver dados de diferentes tipos int, str
#o MÉTODO DEL apaga a tupla


'''cont = 0
while True:
    print(f'Eu vou comer {lanche[cont]}')
    cont = cont + 1
    if cont == len(lanche):
        break''''''
    
    
'''for cont in range(0,len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
    
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi muito!')'''
    