'''
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e
quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha
sido informado corretamente.

Write a program that has a function called token() that takes two optional parameters: a player's name and
how many goals he scored. The program should be able to show the player's sheet, even if some data doesn't have
been informed correctly.
'''
def ficha(nome='<desconhecido>', gol=0):
    print(f'O jogador {nome} fez {gol} gol(s) no campeonato.')


# Main
nome = input('Nome do Jogador: ').strip()
gols = input('Número de Gols: ').strip()

gols = int(gols) if gols.isnumeric() else 0

if nome:
    ficha(nome, gols)
else:
    ficha(gol=gols)
