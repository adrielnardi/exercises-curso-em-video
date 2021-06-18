'''
Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra 'A'
- Em que posição ela aparece a primeira vez
- Em que posição ela aparece a última vez

Make a program that reads a sentence on the keyboard and shows:
- How many times does the letter 'A' appear
- In what position does she appear the first time
- In what position does she appear last
'''
f = str(input("Frase: ")).strip().upper()
frase = f.replace('Á', 'A').replace('Â','A')
print(f"Quantidade de A's: {frase.count('A')}")
print(f"Posição da primeira letra A: {frase.find('A')}")
print(f"Posição da última letra A: {frase.rfind('A')}")
