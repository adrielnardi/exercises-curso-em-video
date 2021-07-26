'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o
maior valor que estão na tupla.

Create a program that will generate five random numbers and place it in a tuple.
After that, show the list of generated numbers and also indicate the smallest and the
higher value that are in the tuple.
'''
from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: {numeros}')
print(f'O valor maior: {max(numeros)}')
print(f'O valor menor: {min(numeros)}')
