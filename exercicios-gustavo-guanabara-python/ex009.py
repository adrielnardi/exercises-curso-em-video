'''
Faça um programa que leia um número inteiro qualquer e mostre
na tela a sua tabuada.

Make a program that reads any integer and shows
your multiplication table on the screen.
'''
n = int(input("Numero: "))
for i in range(1,10):
    print(f"{n}x{i}={n*i}")
    
