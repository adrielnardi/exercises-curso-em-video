'''
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as
notas de cada aluno individualmente.

Create a program that reads multiple students' names and two grades and stores them in a composite list.
At the end, show a bulletin containing the average of each one and allow the user to show the
grades for each individual student.
'''
ficha = list()
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media])
    resp = str(input('Quer continuar [S/N]? '))
    if resp in 'Nn':
        break
print('-=' * 50)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 50)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' *50)
    op = int(input('Mostrar notas de qual aluno (999 interrompe)? '))
    if op == 999:
        print('FINALIZANDO...')
        break
    elif op <= len(ficha) - 1:
        print(f'Notas de {ficha[op][0]} são {ficha[op][1]}')
    else:
        print("Digite um número válido!")
print('<<< VOLTE SEMPRE >>>')