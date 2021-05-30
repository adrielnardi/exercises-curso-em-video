'''
Faça um algoritmo que leia o salário de um funcionário e mostre
seu novo salário, com 15% de aumento.

Make an algorithm that reads an employee's salary and shows
his new salary, with a 15% increase.
'''
salario = float(input("Salário Atual: R$ "))
print(f"Aumento de 15%: R${salario + (salario * 15/100):.2f}")
