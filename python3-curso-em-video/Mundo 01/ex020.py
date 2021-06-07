'''
O mesmo professor do desafio anterior quer sortear a ordem de
apresentação de trabalhos dos alunos. Faça um programa que leia
o nome dos quatro alunos e mostre a ordem sorteada.

The same teacher from the previous challenge wants to draw the order of
presentation of student work. Make a program that reads
the name of the four students and show the order drawn.
'''
import random
lista = []
for i in range(1,5):
    nome = input(f"{i}º Aluno: ")
    lista.append(nome)
lista_ordenada = sorted(lista)
print(f"Foi escolhido o(a) aluno(a) {lista_ordenada}")

