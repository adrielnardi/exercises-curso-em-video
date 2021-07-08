'''
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

Develop a program that reads six integers and shows the sum only
those who are peers. If the value entered is odd, disregard it.
'''
sum,c = 0,0
for i in range(1, 7):
    n = int(input(f"Digite o {i} inteiro: "))
    if n % 2 == 0:
        sum += n
print(f'A soma de todos os pares digitados é {sum}.')
