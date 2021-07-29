'''
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

Create a program that has a tuple with several words (do not use accents). After that, you must show, for each word, what are your vowels.
'''
palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for palavra in palavras:
    print(f'\nPalavra {palavra.upper()} -> ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')