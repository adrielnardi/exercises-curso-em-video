'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela
cada um dos dígitos separados.
Ex:Digite um número:1834-unidade:4,dezena:3,centena:8,milhar:1

Make a program that reads a number from 0 to 9999 and shows it on the screen
each of the separate digits.
Ex: Enter a number: 1834-unit: 4, ten: 3, hundred: 8, thousands: 1
'''
n = int(input("Número de 0-9999: "))
u = n//1%10
print(f"Unidade: {u}")
d = n//10%10
print(f"Dezena: {d}")
c = n//100%10
print(f"Centena: {c}")
m = n//1000%10
print(f"Milhar: {m}")