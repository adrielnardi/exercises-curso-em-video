'''
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt('Digite um n: ')

Create a program that has the readInt() function, which will work similarly to Python's input() function, only doing
the validation to accept only a numeric value. Ex: n = readInt('Type an n: ')
'''
def leiaInt(msg=''):
    while True:
        num = input(msg).strip()
        if num.replace('-', '', 1).isdigit():  # isnumeric()
            return int(num)
        print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')


# Main
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')