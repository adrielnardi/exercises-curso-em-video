'''
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre
todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele
quer ou não continuar a digitar valores.

Create a program that reads several integers from the keyboard. At the end of the run, show the average between
all values and which was the highest and lowest values read. The program should ask the user if he
whether or not you continue to enter values.
'''
resp = 'S'
soma = c = media = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    c += 1
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
media = soma / c
print(f'Você digitou {c} números e a média foi {media}.')
print(f'O maior valor foi {maior} e o menor foi {menor}.')
