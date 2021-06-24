'''
Desenvolva um programa que pergunte a distância de uma viagem
em Km. Calcule o preço da passagem, cobrando R$0.50 por Km
para viagens de até 200Km e R$0.45 para viagens mais longas.

Develop a program that asks the distance of a trip
in Km. Calculate the ticket price, charging R $ 0.50 per Km
for trips up to 200Km and R $ 0.45 for longer trips.
'''
km = float(input("Quantos km? "))
print(f"Custo da viagem: R${km*0.5}") if km <= 200 else print(f"Custo da viagem: R${km*0.45}")
