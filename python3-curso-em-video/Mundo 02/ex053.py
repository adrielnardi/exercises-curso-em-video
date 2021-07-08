'''
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

Create a program that reads any sentence and says if it is a palindrome, disregarding spaces.
'''
frase = str(input('Frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}.')
if inverso == junto:
    print('É um Palíndromo!')
else:
    print('Não é um Palíndromo!')
