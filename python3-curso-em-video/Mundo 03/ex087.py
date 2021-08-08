'''
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
0 [_][_][_]
1 [_][_][_]
2 [_][_][_]
   0  1  2

Enhance the previous challenge by showing no end:
A) The sum of all the even values entered.
B) The sum of the values in the third column.
C) The highest value in the second row.
0 [_] [_] [_]
1 [_] [_] [_]
2 [_] [_] [_]
     0 1 2
'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = maiorvalor2col = soma3col = 0
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Digite um valor para [{i}, {j}]: '))
print('-=' * 30)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end='')
        if matriz[i][j] % 2 == 0:
            somapar += matriz[i][j]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {somapar}.')
for i in range(0, 3):
    soma3col += matriz[i][2]
print(f'A soma dos valores da terceira coluna é {soma3col}.')
for j in range(0, 3):
    if j == 0:
        maiorvalor2col = matriz[1][j]
    elif matriz[1][j] > maiorvalor2col:
        maiorvalor2col = matriz[1][j]
print(f'O maior valor da segunda linha é {maiorvalor2col}.')
