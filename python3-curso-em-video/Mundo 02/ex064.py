'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma
entre eles (desconsiderando o flag).

Create a program that reads several integers from the keyboard. The program will only stop when the user types
the value 999, which is the stop condition. At the end, show how many numbers were entered and what was the sum
between them (disregarding the flag).
'''
n = c = soma = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    soma += n
    c += 1
    n = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {c} números e a soma entre eles foi {soma}.')