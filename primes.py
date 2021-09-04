def primo(n):
    for val in range(2,n):
        if n % val == 0:
            return False
    return True

lista = []
n = int(input('Exibir primos até o número: '))
for val in range(2,n+1):
    if(primo(val)):
        lista.append(val)
print(lista)

#Output
#[IN]: EXibir primos até o número: 10 
#[2, 3, 5, 7]
