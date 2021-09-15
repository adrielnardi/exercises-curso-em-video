'''
Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada
leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar
apenas valores que seja monetários.

Within the utilitiesCeV package that we created in challenge 111, we have a module called data. Create a function
called readMoney() that is able to work like the imput() function, but with a data validation to accept only values
that are monetary.
'''
from modulo.utilidadescev import moeda,dado

p = dado.leiaDinheiro('Informe um preço: R$ ')

moeda.resumo(p, 60, 30)
