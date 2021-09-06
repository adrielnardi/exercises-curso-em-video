'''
Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.

Make a mini-system that uses Python's Interactive Help. The user will type the command and the manual will appear.
When the user enters the word 'END', the program will terminate. Important: use colors.
'''
def ajuda(funcao):
    help(funcao)


while True:
    print('~' * 40)
    print(f'{"Sistema de ajuda PyHELP":^30}')
    print('~' * 40)

    aux = (str(input('Função ou Biblioteca (FIM para sair)-> ')))
    if aux == 'FIM':
        break
    ajuda(aux)

