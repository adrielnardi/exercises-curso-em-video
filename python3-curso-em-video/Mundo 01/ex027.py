'''
Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.

Make a program that reads a person's full name,
then showing the first and last name separately.
'''
n = str(input("Nome Completo: ")).strip().split()
print(f"Primeiro nome: {n[0]}")
print(f"Último nome: {n[len(n)-1]}")