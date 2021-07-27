'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.

Develop a program that reads four values from the keyboard and stores them in a tuple. At the end, show:
A) How many times did the value 9 appear.
B) In which position the first value 3 was entered.
C) What were the even numbers.
'''
c=0
num = (int(input('Digite 1º número: ')),
       int(input('Digite 2º número: ')),
       int(input('Digite 3º número: ')),
       int(input('Digite 4º número: ')))

print(f'Valores digitados:  {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
print(f'O primeiro 3 apareceu na {num.index(3)+1}ª posição' if 3 in num else 'O valor 3 não foi digitado em nenhuma posição')


print('Valores pares?  ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
    else:
        c = c + 1
        if c == len(num):
            print("Sem valores pares")
