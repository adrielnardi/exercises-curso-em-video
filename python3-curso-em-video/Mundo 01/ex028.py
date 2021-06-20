'''
Escreva um programa que faça o computador "pensar" em um
número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
qual foi o número escolhido pelo computador. O programa deverá
escrever na tela se o usuário venceu ou perdeu.

Write a program that makes the computer "think" of a
integer between 0 and 5 and ask the user to try to find out
what was the number chosen by the computer. The program should
write on the screen whether the user won or lost.
'''
from random import randint
sorteio = randint(0,5)
print('Temte advinhar um número entre 0 e 5...')
n = int(input('Qual será o número? '))
print('Acertou Mizeravi!') if n == sorteio else print(f'Errooouu\nNúmero escolhido: {sorteio}')