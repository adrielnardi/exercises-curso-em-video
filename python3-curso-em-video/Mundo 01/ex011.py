'''
Faça um programa que leia a largura e a altura de uma parede
em metros, calcule a sua área e a quantidade de tinta necessária
para pintá-la. Sabendo que cada litro de tinta pinta uma área de 2m².

Make a program that reads the width and height of a wall
in meters, calculate your area and the amount of ink needed
to paint it. Knowing that each liter of paint paints an area of 2m².
'''
largura = float(input("Largura: "))
altura = float(input("Altura: "))
print(f"Dimensão: {largura}x{altura}")
print(f"Área: {largura*altura}m²")
print(f"Precisa de {(largura*altura)/2} litros")