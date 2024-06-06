def aumentar(preco, taxa):
    aum = (preco * taxa) / 100
    res = preco + aum
    return res

def diminuir(preco, taxa):
    res = (preco * taxa) / 100  
    dim = preco - res
    return res

def dobro(preco):
    res = preco * 2
    return res

def metade(preco):
    res = preco / 2
    return res

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace(',', 'X').replace('.', ',').replace('.', 'X')