'''
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

Create a program where the user can type seven numeric values and enter them in a single list that keeps
separate the odd and even values. At the end, show the odd and even values in ascending order.
'''
num = [[], []]
valor = 0
for i in range(1, 8):
    valor = int(input(f'Digite o {i}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' * 30)
num[0].sort()
num[1].sort()
print(f"Lista Completa Ordenada: {num}")
print(f'Pares Ordenados: {num[0]}')
print(f'Impares Ordenados: {num[1]}')
