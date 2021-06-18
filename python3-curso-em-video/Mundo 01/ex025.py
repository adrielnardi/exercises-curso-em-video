'''
Crie um programa que leia o nome de uma pessoa e diga se ela
tem "SILVA" no nome.

Create a program that reads a person's name and tells them
has "SILVA" in its name.
'''
nome = str(input("Nome: ")).strip()
print(f"Tem Silva? {'silva' in nome.lower()}")