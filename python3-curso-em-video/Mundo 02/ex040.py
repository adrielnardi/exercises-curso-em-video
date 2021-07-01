'''
Crie um programa que leia duas notas de um aluno e calcule
sua média, mostrando uma mensagem no final, de acordo com
a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO

Create a program that reads a student's two grades and calculates
their average, showing a message at the end, according to
the average achieved:
- Average below 5.0: FAILED
- Average between 5.0 and 6.9: RECOVERY
- Average 7.0 or higher: APPROVED
'''
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
media = (n1+n2)/2
if media >= 7:
    print("APROVADO")
elif 5 <= media <= 6.99:
    print("RECUPERAÇÃO")
else: print("REPROVADO")