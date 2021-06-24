'''
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

Make a program that reads any year and shows if it is BISSEX.
'''
ano = int(input("Digite o ano: "))
print("BISSEXTO") if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 else print("NÃO BISSEXTO")