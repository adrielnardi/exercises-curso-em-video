'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os
valores únicos digitados, em ordem crescente.

Create a program where the user can enter several numeric values and register them in a list.
If the number already exists inside it, it will not be added. At the end, all
single values entered, in ascending order.
'''
numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não pode ser adicionado...')
    r = str(input('Quer continuar [S/N]? '))[0]
    if r in 'Nn':
        break
print('-=' * 30)
print(f'Sequẽncia digitada: {numeros}')
numeros.sort()
print(f'Ordem crescente: {numeros}')
