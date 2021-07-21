'''
Refaça o EXERCÍCIO 051, lendo o primeiro termo e a razão de uma PA, mostrando
os 10 primeiros termos da progressão usando a estrutura while.

Redo EXERCISE 051, reading the first term and the reason for a PA, showing
the first 10 terms of the progression using the while structure.
'''
print('== Gerador de PA ===')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} → ', end='')
    termo += razao
    cont += 1
print('FIM')