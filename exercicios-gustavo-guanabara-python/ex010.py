'''
Crie um programa que leia quanto dinheiro uma pessoa tem
na carteira e mostre quantos Dólares ela pode comprar.

Create a program that reads how much money a person has
in her wallet and show how many dollars she can buy.
'''
dolar = 5.44
carteira = float(input("Quanto vocẽ tem na carteira: "))
print(f'Você tem {round(carteira / dolar,2)} dólares')
