'''
Crie um programa que leia dois valores e mostre um menu como o abaixo na tela:
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Números
[ 5 ] Sair do Programa
Seu programa deverá realizar a operação solicitada em cada caso.

Create a program that reads two values and shows a menu like the one below on the screen:
[1] Add
[2] Multiply
[3] Greater
[4] New Numbers
[5] Exit the Program
Your program should perform the requested operation in each case.
'''
from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Números
[ 5 ] Sair do Programa''')

opcao = 0
while opcao != 5:
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é {soma}.')
    elif opcao == 2:
        produto = n1 * n2
        print(f'O resultado de {n1} x {n2} é {produto}.')
    elif opcao == 3:
        if n1 == n2:
            print(f'São iguais, o número é {n1}')
        elif n1 > n2:
            maior = n1
            print(f'Entre {n1} e {n2}, o maior valor é {maior}.')
        else:
            maior = n2
            print(f'Entre {n1} e {n2}, o maior valor é {maior}.')

    elif opcao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida! Tente novamente.')
    print('=-=' * 10)
    sleep(1)
print('Fim do programa!')