'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.

Develop a program that reads the name, age and sex of 4 people. At the end of the program, show:
- The average age of the group.
- What is the name of the older man.
- How many women are under 20 years old.
'''
somaidade,media,hmaisvelho,mmenos20 = 0,0,0,0
nomevelho = ''
for i in range(1, 5):
    print(f'{i}ª PESSOA: ')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if i == 1 and sexo in 'Mm':
        hmaisvelho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > hmaisvelho:
        hmaisvelho = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mmenos20 += 1
media = somaidade / 4
print(f'A média de idade do grupo é de {media} anos.')
print(f'O homem mais velho tem {hmaisvelho} anos e se chama {nomevelho}.')
print(f'Ao todo são {mmenos20} mulheres com menos de 20 anos.')