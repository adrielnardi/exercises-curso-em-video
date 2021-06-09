'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
1 - O nome com todas as letras maiúscula e minúsculas.
2 - Quantas letras ao total (sem considerar espaços).
3 - Quantas letras tem o primeiro nome.

Create a program that reads a person's full name and shows:
1 - The name with all uppercase and lowercase letters.
2 - How many letters in total (without considering spaces).
3 - How many letters has the first name.
'''
nome = str(input("Nome Completo: ")).strip()
print(f"Maiúsculo: {nome.upper()}")
print(f"Minúsculo: {nome.lower()}")
print(f"Seu nome tem {len(nome)-nome.count(' ')} letras")
separa = nome.split()
print(f"Seu primeiro nome tem {len(separa[0])} letras")