

def aumentar(preco=None, taxa=1):
    aum = (preco * taxa) / 100
    res = preco + aum
    
    return res

def diminuir(preco, taxa):
    dim = (preco * taxa) / 100
    res = preco - dim
    return res 
def dobro(preco):
    res = preco * 2
    return res
def metade(preco):
    res = preco / 2
    return res

diminuir(100, 10)