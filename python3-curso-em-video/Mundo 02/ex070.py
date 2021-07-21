'''
Crie um programa que leia o nome e o preço de vários produtos. O programa
deverá perguntar se o usuário vai continuar. No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$ 1000.
C) Qual é o nome do produto mais barato.

Create a program that reads the name and price of various products. The program
you should ask if the user will continue. At the end, show:
A) What is the total amount spent on the purchase.
B) How many products cost more than R $ 1000.
C) What is the name of the cheapest product.
'''
total = mil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    total += preco
    if preco > 1000:
        mil += 1
    resp = '-'
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'{" NOTA ":-^50}')
print(f'Total da compra: R$ {total:.2f}')
print(f'{mil} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')
print(f'{"":-^50}')