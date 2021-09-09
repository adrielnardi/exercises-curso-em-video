'''
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.

Create a module called currency.py that has the built-in functions increase(), decrease(), double(), and half().
Also make a program that imports this module and uses some of these functions.
'''
from modulo import moeda

valor = float(input('Informe um valor: '))
print(f'''Aumento de 10%: R${moeda.aumentar(valor, 10):.2f}
Subtração de 10%: R${moeda.diminuir(valor, 10):.2f}
Dobro: R${moeda.dobro(valor):.2f}
Metade: R${moeda.metade(valor):.2f}''')