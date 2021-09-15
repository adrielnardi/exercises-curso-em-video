'''
Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções
utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

Create a package called utilitiesCeV that has two built-in modules called currency and data. Transfer all functions
used in challenges 107, 108 and 109 for the first package and keep everything running.
'''
from modulo import moeda

p = float(input("Digite o preço: R$ "))

moeda.resumo(p,50,20)