'''
Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.

Develop a program that reads the length of three lines
and tell the user whether or not they can form a triangle.
'''
r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))
print("Forma Triângulo") if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 \
                         else print("Não Forma Triângulo")

