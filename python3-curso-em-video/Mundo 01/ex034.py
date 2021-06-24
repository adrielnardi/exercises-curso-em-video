'''
Escreva um programa que pergunte o salário de um funcionário
e calcule o valor do seu aumento. Para salários superiores a
R$1.200,00. Calcule um aumento de 10%. Para inferiores ou
iguais, o aumento é de 15%.

Write a program that asks an employee's salary
and calculating the value of your increase. For wages over
R $ 1,200.00. Calculate a 10% increase. For lower or
equal, the increase is 15%.
'''
s = float(input("Salário: "))
print(f"Aumento: {s + (s * 10/100)}") if s > 1200 else print(f"Aumento: {s + (s * 15/100)}")
