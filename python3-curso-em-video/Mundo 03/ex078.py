'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre
qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

Make a program that reads 5 numeric values and stores them in a list. At the end, show
which was the highest and lowest value entered and their respective positions in the list.
'''
lista = []
maior,menor = 0,0
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}... ', end='')
