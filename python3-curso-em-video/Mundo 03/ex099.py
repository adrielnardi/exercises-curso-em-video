'''
Faça um programa que tenha uma função chamada maior(), que receba vários parãmetros
com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

Make a program that has a function called larger(), which takes several parameters
with integer values. Your program has to analyze all the values and say which one is the biggest.
'''
def maior(* num):
    cont = maior = 0
    for valor in num:
        print(f'{valor}', end=" ")
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f"da um total de {cont} números")
    print(f'O maior valor foi {maior}')
    print('--'*20)


maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()