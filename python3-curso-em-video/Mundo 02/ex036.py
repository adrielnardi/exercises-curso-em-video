'''
Escreva um programa para aprovar o empréstimo bancário para a
compra de uma casa. Pergunte o valor da casa, o salário do
comprador e em quantos anos ele vai pagar. A prestação mensal,
não pode exceder 30% do salário ou então o empréstimo será negado.

Write a program to approve the bank loan for the
buying a house. Ask for the value of the house, the salary of the
buyer and how many years he will pay. The monthly installment,
cannot exceed 30% of the salary or the loan will be denied.
'''
casa = float(input("Valor da casa: R$ "))
salario = float(input("Salário do comprador: R$ "))
anos = float(input("Anos de financiamento: "))

prestacao = casa/(anos * 12)
print(f"Prestação: R${prestacao:.2f}")
minimo = salario * 30 / 100

print("Empréstimo CONCEBIDO!") if prestacao <= minimo else print("Empréstimo NEGADO!")
