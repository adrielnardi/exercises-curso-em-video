'''
Faça um programa que leia três números e mostre qual é o
MAIOR e qual é o MENOR.

Make a program that reads three numbers and shows what the
BIGGER and which is the SMALLER.
'''
for i in range(3):
    n = float(input(f"{i+1} número: "))
    if i == 0:
        maior = n
        menor = n
    if n > maior: maior = n
    if n < menor: menor = n
print(f"MAIOR: {maior}")
print(f"MENOR: {menor}")
