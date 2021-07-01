'''
A confederação nacional de natação precisa de um programa que
leia o ano de nascimento de um atleta e mostre sua categoria,
de acordo com a idade:
-Até 9 anos: MIRIM
-Até 14 anos: INFANTIL
-Até 19 anos: JUNIOR
-Até 25 anos: SÊNIOR
-Acima: MASTER

The national swimming confederation needs a program that
read the year of birth of an athlete and show his category,
according to age:
-Up to 9 years old: MIRIM
-Up to 14 years old: CHILD
-Up to 19 years old: JUNIOR
-Up to 25 years old: SENIOR
-Up: MASTER
'''
from datetime import date
print("===NASCIMENTO===")
d_nasc = int(input("DIA: "))
m_nasc = int(input("MÊS: "))
a_nasc = int(input("ANO: "))

a_atual = int(date.today().year)
m_atual = int(date.today().month)
d_atual = int(date.today().day)

idade = a_atual - a_nasc
if m_atual < m_nasc:
    idade = idade - 1
if m_atual == m_nasc and d_atual < d_nasc:
    idade = idade - 1


if idade <= 9:
    print(f"{idade} anos e categoria MIRIM")
elif idade <= 14:
    print(f"{idade} anos e categoria INFANTIL")
elif idade <= 19:
    print(f"{idade} anos e categoria JUNIOR")
elif idade <= 25:
    print(f"{idade} anos e categoria SÊNIOR")
else:
    print(f"{idade} anos e categoria MASTER")
