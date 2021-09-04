'''
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
início, fim e passo. seu programa tem que realizar três contagens através da função criada:
a) De 1 até 10, de 1 em 1
b) De 10 até 0, de 2 em 2
c) uma contagem personalizada

Write a program that has a function called counter(), which takes three parameters:
beginning, end and step. your program has to perform three counts through the created function:
a) From 1 to 10, from 1 to 1
b) From 10 to 0, every 2
c) a custom score
'''


def contador(i, f, p):
    print(f"contagem de {i} até {f} de {p} em {p}: ")

    if p < 0:
        p*=-1
    if p == 0:
        p = 1

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=" ")
            cont += p
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=" ")
            cont -= p


contador(1, 10, 1)
print()
contador(10, 0, 2)
print()

print("Contagem personalizada:")
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))

contador(inicio, fim, passo)
