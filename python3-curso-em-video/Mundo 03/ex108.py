'''
Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um
valor monetário formatado.

Adapt the code from challenge #107 by creating an additional function called currency() that can display the numbers as
a formatted monetary value.
'''
from modulo import moeda

valor = float(input('Informe um valor: R$ '))

print(f'''
Aumento de 10%: {moeda.aumentarEx108(valor, 10)}
Subtração de 15%: {moeda.diminuirEx108(valor, 15)}
Dobro: {moeda.dobroEx108(valor)}
Metade: {moeda.metadeEx108(valor)}
''')
