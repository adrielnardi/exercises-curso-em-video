'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
pelo usuário. O programa será interrompido quando o número solicitado for negativo.

Make a program that shows the multiplication table of several numbers, one at a time, for each value entered
by the user. The program will be interrupted when the requested number is negative.
'''
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    for i in range(1, 11):
        print(f'{n} x {i} = {n * i}')
