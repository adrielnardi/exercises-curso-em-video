'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
do Campeonato Brasileiro de Futebol, na ordem de colocação.
Depois mostre:
A) Os 5 primeiros.
B) Os últimos 4 colocados.
C) Times em ordem alfabética.
D) Em que posição está o time da Chapecoense.

Create a tuple filled with the top 20 in the table
of the Brazilian Football Championship, in the order of placement.
Then show:
A) The first 5.
B) The last 4 placed.
C) Teams in alphabetical order.
D) In what position is the Chapecoense team.
'''
times = ('Botafogo', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Corinthians', 'Altético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
         'Atlético-GO')

print('-=' * 50)
print(f'Times do Brasileirão: {times}')
print('-=' * 50)
print(f'Os 5 primeiros: {times[0:5]}')
print('-=' * 50)
print(f'Os 4 últimos: {times[-4:]}')
print('-=' * 50)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 50)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')