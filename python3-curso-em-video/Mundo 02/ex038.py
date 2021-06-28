'''
Escreva um programa que leia dois números inteiros e compare-os
mostrando na tela uma mensagem:
-O primeiro valor é maior
-0 segundo valor é maior
-Não existe valor maior, os dois são iguais

Write a program that reads two integers and compares them
showing a message on the screen:
-The first value is higher
-0 second value is greater
-There is no higher value, the two are the same
'''
n1 = int(input("1ª número inteiro: "))
n2 = int(input("2ª número inteiro: "))
if n1 > n2:
    print("O primeiro valor é maior")
elif n2 > n1:
    print("0 segundo valor é maior")
else:
    print("Não existe valor maior, os dois são iguais")

