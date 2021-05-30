'''
Faça um algoritmo que leia o preço de um produto e mostre
seu novo preço, com 5% de desconto.

Make an algorithm that reads the price of a product and shows
its new price, with 5% discount.
'''
valor = float(input("Preço do Produto: R$ "))
print(f"Com desconto de 5%: R${valor - (valor * 5/100):.2f}")
