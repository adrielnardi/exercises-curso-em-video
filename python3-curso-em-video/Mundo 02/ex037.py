'''
Escreva um programa que leia um número inteiro qualquer e
peça para o usuário escolher qual será a base de conversão:
-1 para binário
-2 para octal
-3 para hexadecimal

Write a program that reads any integer and
ask the user to choose the conversion basis:
-1 for torque
-2 to octal
-3 to hexadecimal
'''
n = int(input("Digite número inteiro: "))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL
''')
op = int(input("Sua opção: "))
if op == 1:
    print(f"Binário: {bin(n)}")
elif op == 2:
    print(f"Octal: {oct(n)}")
elif op == 3:
    print(f"Hexadecimal: {hex(n)}")
else:
    print("Opção inválida")