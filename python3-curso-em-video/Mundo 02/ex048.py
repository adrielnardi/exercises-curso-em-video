'''
Faça um programa que calcule a soma entre todos os números ímpares que
são múltiplos de três e que se encontram no intervalo de 1 até 500.

Make a program that calculates the sum between all the odd numbers that
are multiples of three and in the range of 1 to 500.
'''
sum,c = 0,0
for i in range(1, 501, 2):
    if i % 3 == 0:
        sum += i
        c += 1
print(f'A soma de todos os {c} valores solicitados é {sum}.')
