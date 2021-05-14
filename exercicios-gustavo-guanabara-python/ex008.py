'''
Escreva um programa que leia um valor em metros e o exiba
convertido em centímetros e milímetros.

Write a program that reads a value in meters and displays it
converted to centimeters and millimeters.
'''
medida = float(input('Uma distância em metros: '))
mm = medida * 1000
print(f"mm: {mm}")
cm = medida * 100
print(f"cm: {cm}")
dm = medida * 10
print(f"dm: {dm}")
dam = medida / 10
print(f"mm: {dam}")
hm = medida / 100
print(f"hm: {hm}")
km = medida / 1000
print(f"km: {km}")