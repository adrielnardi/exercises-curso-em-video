'''
Escreva um programa que leia um número n inteiro qualquer e mostre
na tela os n primeiros elementos de uma Sequência de Fibonacci.
Ex: 0 → 1 → 1 → 2 → 3 → 5 → 8

Write a program that reads any integer n and shows
on the screen the first n elements of a Fibonacci Sequence.
Ex: 0 → 1 → 1 → 2 → 3 → 5 → 8
'''
print('Sequência de Fibonacci')
n = int(input('Quantos termos você quer mostrar? '))
t1 = 1
t2 = 1
print(f'{t1} → {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' → {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' → FIM')