#Criar uma tupla com 10 primeiros colocados em uma tabela de futebol
#Em seguida mostrar: mostre os 5 primeiros colocados
#Mostre os ultimos 4 da tabela
#Mostre uma lsita com os nomes em ordem alfabetica
#Mostre em que posição está a chapecoense

tabela = ('corinthians', 'flamengo', 'botafogo', 'gremio', 'nautico', 'sport', 'santos', 'chapecoense', 'são paulo', 'cruzeiro')
print('='*30)
print('A lista dos times do Brasileirão')
print('='*30)
print(tabela)
print('='*30)
print(f'Os 5 primeiros colocados são: {tabela[0:5]}')
print('='*30)
print(f'Os 4 últimos colocados são: {tabela[-4:len(tabela)]}')
print('='*30)
print(f'Os times dispostos em ordem alfabética são: {sorted(tabela)}')
print('='*30)
for pos in range(0,len(tabela)):
    if tabela[pos] == 'chapecoense':
        print(f'O time {tabela[pos]} está na posição {pos+1}')