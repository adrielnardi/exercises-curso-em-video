'''
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e
somapar(). A primeira função vai sortear 5 números e vai colocá-los dentroda lista e a
segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.

Make a program that has a list called numbers and two functions called draw() and sum().
The first function will draw 5 numbers and place them inside of the list and the second
function will show the sum between all the PAIR values drawn by the previous function.
'''
from random import randint

def sorteia(lista):
    print("Sorteando 5 valores: ")
    for cont in range(0,5):
        lista.append(randint(1,10))
    print(numeros)

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f"Somando os valores pares da {lista}, temos {soma}")

numeros = list()
sorteia(numeros)
somaPar(numeros)

