'''
Melhore o jogo do EXERCÍCIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
palpites foram necessários para vencer.

Improve the EXERCISE 028 game where the computer will "think" of a number between 0 and 10.
Only now the player will try to guess until he gets it right, showing at the end how many
guesses were needed to win.
'''
from random import randint
sorteio = randint(0,10)
print('Tente advinhar um número entre 0 e 10...')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == sorteio:
        acertou = True
    else:
        if jogador < sorteio:
            print('O número é maior, tente mais uma vez')
        elif jogador > sorteio:
            print('O número é menor, tente mais uma vez')
print(f'O número é {sorteio}. Acertou com {palpites} tentativas. Parabéns!')