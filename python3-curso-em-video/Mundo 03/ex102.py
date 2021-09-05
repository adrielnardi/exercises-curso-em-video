'''
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a
calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o
processo de cálculo do fatorial.

Create a program that has a factorial() function that takes two parameters: the first one that indicates the number a
calculate and another one called show, which will be a logical value (optional) indicating whether or not it will be shown on the screen.
factorial calculation process.
'''
def fatorial(n, show=False):
    f = 1
    for cont in range(n, 0, -1):
        if show:
            print(cont, end=' x ' if cont > 1 else ' = ')
        f *= cont
    print(f)


#Main
fatorial(5,show=True)
fatorial(5,show=False)
