'''
Crie um programa que faça o computador jogar Jokenpô com você.

Create a program that makes the computer play Jokenpô with you.
'''
from time import sleep
from random import randint
computador = randint(0,2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''')
item = ('Pedra','Papel','Tesoura')
jogador = int(input("Sua Jogada? "))
while jogador < 0 or jogador > 2:
    jogador = int(input("Sua Jogada? "))

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ!!!')
sleep(0.5)
print('-=' * 12)
print(f'Jogador jogou {item[jogador]}')
print(f'Computador jogou {item[computador]}')
print('-=' * 12)

if jogador == 0:
    if computador == 0:
        print("Empate!")
    elif computador ==1:
        print("Perdeu!")
    elif computador == 2:
        print("Venceu!")
elif jogador ==1:
    if computador == 0:
        print("Venceu!")
    elif computador ==1:
        print("Empate!")
    elif computador == 2:
        print("Perdeu!")
elif jogador == 2:
    if computador == 0:
        print("Perde!")
    elif computador ==1:
        print("Ganhe!")
    elif computador == 2:
        print("Empate!")
else:
    print("Opção Inválida!")