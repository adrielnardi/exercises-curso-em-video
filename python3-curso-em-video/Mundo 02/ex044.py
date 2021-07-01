'''
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
-à vista dinheiro/cheque: 10% de desconto
-à vista no cartão: 5% de desconto
-em até 2x no cartão: preço normal
-3x ou mais no cartão: 20% de juros
'''
valor = float(input("Qual o valor do produto? R$ "))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
''')
op = int(input("Digite a opção: "))
while (op > 4) or (op < 1):
    print("Opção inválida")
    op = int(input("Digite a opção: "))

if op == 1:
    total = valor - (valor*10/100)
elif op == 2:
    total = valor - (valor*5/100)
elif op == 3:
    total = valor
else:
    total = valor + (valor*20/100)

print(f"O valor do seu produto vai custar {total}")

