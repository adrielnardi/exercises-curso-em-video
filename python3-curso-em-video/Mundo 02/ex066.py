'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números
foram digitados e qual foi a soma entre eles (desconsiderando o flag).

Create a program that reads several integers from the keyboard. The program will only stop when
the user enters the value 999, which is the stop condition. At the end, show how many numbers
were typed and what was the sum between them (disregarding the flag).
'''
soma = c = 0
while True:
    n = int(input('Digite um valor [999 para parar]: '))
    if n == 999:
        break
    c += 1
    soma += n
print(f'A soma dos {c} valores foi {soma}!')
