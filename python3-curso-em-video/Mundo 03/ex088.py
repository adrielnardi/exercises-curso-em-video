'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos
serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

Make a program that helps a MEGA SENA player to create guesses. The program will ask how many games
will be generated and will draw 6 numbers between 1 and 60 for each game, registering everything in a composite list.
'''
from random import randint
from time import sleep
lista,jogos = list(),list()
print('-' * 30)
print('         MEGA SENA         ')
print('-' * 30)
qtd = int(input('Quantos jogos será sorteado? '))
total = 1
while total <= qtd:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('-=' * 3, f' SORTEANDO {qtd} JOGOS ', '-=' * 3)
for i, v in enumerate(jogos):
    print(f'Jogo {i + 1}: {v}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! > ', '-=' * 5)