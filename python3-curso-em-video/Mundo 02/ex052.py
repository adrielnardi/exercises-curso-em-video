'''
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

Make a program that reads an integer and says whether or not it is a main number.
'''
n = int(input('Digite um número: '))
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        print('\033[33m', end='')
        count += 1
    else:
        print('\033[31m', end='')
    print(f'{i} ', end='')
print(f'\n\033[34mO número {n} foi divisível {count} vezes.')
if count == 2:
    print('E por isso, ele É PRIMO!')
else:
    print('E por isso, ele NÃO É PRIMO!')