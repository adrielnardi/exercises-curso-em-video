'''
Escreva um programa que pergunte a quantidade de Km percorridos
por um carro alugado e a quantidade de dias pelos quais ele foi
alugado. Calcule o preço a pagar, sabendo que o carro custa R$60
por dia e R$0.15 por km rodado.

Write a program that asks the number of kilometers traveled
for a rental car and the number of days it has been gone
rented. Calculate the price to pay, knowing that the car costs R $ 60
per day and R $ 0.15 per km traveled.
'''
dias = int(input("Dias alugados? "))
km = float(input("Km rodados? "))
print(f"O aluguel do carro custará R$ {round(dias*60 + km*0.15,2)}")