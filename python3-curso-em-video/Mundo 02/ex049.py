'''
Refaça o EXERCÍCIO 009, mostrando a tabuada de um número que
o usuário escolher, só que agora utilizando um laço for.

Redo EXERCISE 009, showing the multiplication table for a number that
the user chooses, only now using a for loo.
'''
n = int(input("Numero: "))
for i in range(1,11):
    print(f"{n}x{i}={n*i}")