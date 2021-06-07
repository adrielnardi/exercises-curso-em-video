'''
Um professor quer sortear um dos seus quatros alunos para apagar
o quadro. Faça um programa que ajude ele, lendo o nome deles e
escrevendo o nome do escolhido.

A teacher wants to raffle one of his four students to erase
the board. Make a program that helps him, reading their names and
writing the name of the chosen one.
'''
import random
lista = []
for i in range(1,5):
    nome = input(f"{i}º Aluno: ")
    lista.append(nome)
print(f"Foi escolhido o(a) aluno(a) {random.choice(lista)}")