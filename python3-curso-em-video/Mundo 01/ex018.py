'''
Faça um programa que leia um ângulo qualquer e mostre na tela o valor
do seno, cosseno e tangente desse ângulo.

Make a program that reads any angle and shows the value on the screen
of the sine, cosine and tangent of that angle.
'''
import math
a = float(input('Ângulo? '))
r = math.radians(a)
s = math.sin(r)
print(f"Seno: {s:.2f}")
c = math.cos(r)
print(f"Cosseno: {c:.2f}")
t = math.tan(r)
print(f"Tangente: {t:.2f}")

