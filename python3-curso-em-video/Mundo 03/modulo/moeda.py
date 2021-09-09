def aumentar(valor, bonus):
    return valor + (valor * bonus / 100)


def diminuir(valor, onus):
    return valor - (valor * onus / 100)


def dobro(valor):
    return valor * 2


def metade(valor):
    return valor / 2


def moedaEx108(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')


def aumentarEx108(valor=0, bonus=0):
    return moedaEx108(valor + (valor * bonus / 100))


def diminuirEx108(valor=0, onus=0):
    return moedaEx108(valor - (valor * onus / 100))


def dobroEx108(valor=0):
    return moedaEx108(valor * 2)


def metadeEx108(valor=0):
    return moedaEx108(valor / 2)


def moedaEx109(valor):
    return f'R${valor:.2f}'.replace('.', ',')


def aumentarEx109(valor, bonus, view=False):
    return moedaEx109(valor + (valor * bonus / 100)) if view else valor + (valor * bonus / 100)


def diminuirEx109(valor, onus, view=False):
    return moedaEx109(valor - (valor * onus / 100)) if view else valor - (valor * onus / 100)


def dobroEx109(valor, view=False):
    return moedaEx109(valor * 2) if view else valor * 2


def metadeEx109(valor, view=False):
    return moedaEx109(valor / 2) if view else valor / 2