'''
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre
quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

Create a program that reads the year of birth of seven people. At the end, show
how many people have not yet reached the age of majority and how many are already older.
'''
from datetime import date
atual = date.today().year
cmaior,cmenor = 0,0
for i in range(1, 8):
    nasc = int(input(f'Em que ano a {i}ª pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 18:
        cmaior += 1
    else:
        cmenor += 1
print(f'Tivemos {cmaior} pessoas maiores de idade.')
print(f'Tivemos {cmenor} pessoas menores de idade.')