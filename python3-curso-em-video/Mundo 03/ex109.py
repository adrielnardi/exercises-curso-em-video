'''
Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor
retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

Modify the functions that were created in challenge 107 so that they accept one more parameter, informing if the value
returned by them will or will not be formatted by the currency() function, developed in challenge 108.
'''
from modulo import moeda

valor = float(input('Informe um valor: R$ '))

print(f'''
Aumento de 10%:  {moeda.aumentarEx109(valor, 10, True)} 'formatado' 
Subtração de 15%: {moeda.diminuirEx109(valor, 15, True)} 'formatado'
Dobro: {moeda.dobroEx109(valor)} 'não formatado'
Metade: {moeda.metadeEx109(valor)} 'não formatado'
''')