'''
Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.

Make a program that reads the weight of five people.
At the end, show what was the highest and lowest weight read.
'''
maior, menor = 0,0
for i in range(1, 6):
    peso = float(input(f'Peso da {i}ª pessoa: '))
    if i == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior foi de {maior} kg.')
print(f'O menor foi de {menor} kg.')