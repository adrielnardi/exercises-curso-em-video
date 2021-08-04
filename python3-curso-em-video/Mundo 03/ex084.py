'''
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.

Make a program that reads multiple people's names and weights, keeping everything in a list. At the end, show:
A) How many people were registered.
B) A listing with the heaviest people.
C) A listing with the lighter people.
'''
aux,principal = [],[]
maior = menor = 0
while True:
    aux.append(str(input('Nome: ')))
    aux.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior = menor = aux[1]
    else:
        if aux[1] > maior:
            maior = aux[1]
        if aux[1] < menor:
            menor = aux[1]
    principal.append(aux[:])
    aux.clear()
    resp = str(input('Quer continuar [S/N]? '))
    if resp in 'Nn':
        break
print(f'Ao todo, foram cadastradas {len(principal)} pessoas.')
print(f'O maior peso foi de {maior} kg. Peso de ', end='')
for p in principal:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menor} kg. Peso de ', end='')
for p in principal:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()
