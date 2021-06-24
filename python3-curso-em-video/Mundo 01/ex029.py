'''
Escreva um programa que leia a velocidade de um carro. Se ele
ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi
multado. A multa vai custar R$7.00 por cada Km acima do limite.

Write a program that reads the speed of a car. If he
exceed 80 km/h, show a message saying that it was
fined. The fine will cost R$7.00 for each Km above the limit.
'''
v = float(input("Velocidade: "))
print(f"Multado em {(v-80)*7}") if v > 80 else print("Boa Viagem!")

