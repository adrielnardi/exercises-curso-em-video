'''
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer
como parâmetro e mostre uma mensagem com tamanho adaptável.

Make a program that has a function called write() that receives any text
as a parameter and display a message with adaptable size.
'''
def escreva(msg):
        tam = len(msg) + 4
        print('~'*tam)
        print(f'  {msg}')
        print('~' * tam)


escreva("Oi")
escreva('Olá Mundo')