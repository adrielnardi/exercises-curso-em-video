'''
Faça um programa que leia o ano de nascimento de um jovem e
informe, de acordo com sua idade, se ele ainda se alistar
ao serviço militar, se é a hora de se alistar ou se já passou
do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que
passou do prazo.

Make a program that reads the year of birth of a young person and
inform, according to your age, if he is still enlisting
to military service, whether it's time to enlist or if it's past
enlistment time. Your program should also show how much time is left or
has passed the deadline.
'''
from datetime import date
atual = date.today().year
nascimento = int(input("Nascimento: "))
idade = atual - nascimento
print(f"Nasceu em {nascimento} tem {idade} no ano {atual}")
if idade > 18:
    saldo = idade - 18
    print(f"Passou {saldo} anos do alistamento")
elif idade < 18:
    saldo = 18 - idade
    print(f"Falta {saldo} anos para se alistar")
else:
    print("Ano do seu alistamento")