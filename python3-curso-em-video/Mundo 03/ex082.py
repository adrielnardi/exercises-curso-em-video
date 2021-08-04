'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, cria duas listas extras que vão
conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das
três listas geradas.

Create a program that will read multiple numbers and put them in a list. After that, create two extra lists that will
contain only the typed odd and even values respectively. At the end, show the content of the
three lists generated.
'''
n = list()
par = list()
impar = list()
while True:
    n.append(int(input('Digite um número: ')))
    r = str(input('Quer continuar [S/N]? '))[0]
    if r in 'Nn':
        break
for i, v in enumerate(n):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print('~' * 50)
print(f'Lista: {n}')
print(f'Pares: {par}')
print(f'Impares: {impar}')
