'''
Faça um programa que leia algo pelo teclado e mostre na tela
o seu tipo primitivo e todas as informações possíveis sobre ele.
'''
s = input("Digite algo: ")
print(f"Tipo Primitivo: {type(s)}")
print(f"Tem espaço? {s.isspace()}")
print(f"É número? {s.isnumeric()}")
print(f"É alfabético? {s.isalpha()}")
print(f"É alfanumérico? {s.isalnum()}")
print(f"Está em maiúsculo? {s.isupper()}")
print(f"Está em minúsculo? {s.islower()}")
print(f"Capitalizado? (nem maiúsculo, nem minúsculo) {s.istitle()}")

