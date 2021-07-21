'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) Quantas pessoas têm mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres têm menos de 20 anos.

Create a program that reads the age and sex of several people. For each registered person,
the program should ask whether the user wants to continue or not. At the end, show:
A) How many people are over 18 years old.
B) How many men were registered.
C) How many women are under 20 years old.
'''
total18 = Htotal = mulhermenos20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        total18 += 1
    if sexo == 'M':
        Htotal += 1
    if sexo == 'F' and idade < 20:
        mulhermenos20 += 1
    resp = '-'
    while resp not in 'SN':
        resp = str(input('Continuar [S/N]? ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Pessoas com mais 18 anos: {total18}')
print(f'Total de homens: {Htotal}')
print(f'Mulher com menos 20: {mulhermenos20}')