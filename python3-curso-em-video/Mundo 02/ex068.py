'''
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

Make a program that plays even or odd with the computer. The game will only be stopped when the
player LOSE, showing the total consecutive victories he has won at the end of the game.
'''
from random import randint
c = 0
while True:
    jogador = int(input('Diga um valor de 0 a 10: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = '-'
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar [P/I]? ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}', end=' ')
    print('DEU PAR.' if total % 2 == 0 else 'DEU ÍMPAR.')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            c += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            c += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {c} vezes.')