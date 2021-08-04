'''
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
0 [_][_][_]
1 [_][_][_]
2 [_][_][_]
   0  1  2
No final, mostre a matriz na tela, com a formatação correta.

Create a program that creates a 3x3 dimensional matrix and fills it with values read by the keyboard.
0 [_][_][_]
1 [_][_][_]
2 [_][_][_]
    0 1 2
At the end, show the matrix on the screen, with the correct formatting.
'''
matriz = [[0 for y in range(3)] for x in range(3)]
#ou matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Digite um valor para [{i}, {j}]: '))
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end='')
    print()