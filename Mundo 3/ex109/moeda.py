def aumentar(preco=0, taxa=0, format=False):
    aum =   (preco * taxa) / 100
    res = preco + aum
    return res if format is False else moeda(res)

def diminuir(preco=0, taxa=0, format=False):
    dim = (preco * taxa) / 100
    res = preco - dim
    return res if format is False else moeda(res)

def metade(preco=0, format=False):
    res = preco / 2
    return res if format is False else moeda(res)

def dobro(preco=0, format=False):
    res = preco * 2
    return res if format is False else moeda(res)

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace(',', 'X').replace('.', ',').replace('.', 'X')

help(aumentar(100, 10, True ))