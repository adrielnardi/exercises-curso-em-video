'''
Faça um programa que tenha uma função chamada area(), que receba as dimensões de um
terreno retangular(largura e comprimento) e mostre a área do terreno.

Write a program that has a function called area(), which receives the dimensions of a
rectangular terrain (width and length) and show the terrain area.
'''
def area(l,c):
    a = l * c
    print(f"Área {l}x{c} = {a}m²")


print("Controle de Terrenos")
largura = float(input('Largura (m): '))
comprimento = float(input("Comprimento (m): "))

area(largura,comprimento)