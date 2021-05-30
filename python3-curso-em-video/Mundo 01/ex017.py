'''
Faça um programa que leia o comprimento do cateto oposto e do
cateto adjacente de um triângulo retângulo, calcule e mostre o
comprimento da hipotenusa.

Make a program that reads the length of the opposite leg and the
adjacent side of a right triangle, calculate and show the
hypotenuse length.
'''
from math import hypot
co = float(input("Cateto Oposto: "))
ca = float(input("Cateto Adjacente: "))
print(f"Hipotenusa: {hypot(co,ca):.2f}")