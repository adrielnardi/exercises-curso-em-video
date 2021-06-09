'''
Crie um programa que leia o nome de uma cidade e diga se ela
começa ou não com o nome "SANTO".

Create a program that reads the name of a city and tells you if it
begins or not with the name "SANTO".
'''
cidade = str(input("Cidade: ")).strip()
print(f"Começa com Santo? {cidade[:5].upper() == 'SANTO'}")
