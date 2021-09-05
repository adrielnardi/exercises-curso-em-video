'''
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

Create a program that has a function called vote() that will receive a person's year of birth as a parameter,
returning a literal value indicating whether a person has a DENIED, OPTIONAL, and REQUIRED vote in elections.
'''
from datetime import date
def voto(ano):
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: FACULTATIVO O VOTO'
    else:
        return f'Com {idade} anos: OBRIGATÓRIO O VOTO'


nasc = int(input("Em que ano você nasceu? "))
print(voto(nasc))