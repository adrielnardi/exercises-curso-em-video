'''
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número
de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

Rewrite the readInt() function we did in challenge 104, now including the possibility of typing a number
of invalid type. Enjoy and also create a readFloat() function with the same functionality.
'''
def leiaInt():
    while True:
        try:
            n = int(input('Digite um número inteiro: '))
        except (ValueError, TypeError):
            print('\033[31mErro! Por favor digite um número inteiro válido\033[m')
        else:
            return n


def leiaFloat():
    while True:
        try:
            n = float(input('Digite um número flutuante: '))
        except (ValueError, TypeError):
            print('\033[31mErro! Por favor digite um número real válido\033[m')
        else:
            return n


nint = leiaInt()
nfloat = leiaFloat()

print(f'''
Inteiro: {nint} 
Flutuante: {nfloat}''')