def aumentar(p=0, t=0, f=True):
    aum = (p * t) / 100
    res = p - aum
    return res if f is False else moeda(res)

def diminuir(p=0, t=0, f=True):
    dim = (p * t) / 100
    res = p - dim
    return res if f is False else moeda(res)

def dobro(p=0, f=True):
    res = p * 2
    return res if f is False else moeda(res)

def metade(p=0, f=True):
    res = p / 2
    return res if f is False else moeda(res)

def moeda(p=0, moeda='R$'):
    return f'{moeda}{p:.2f}'.replace('.', ',')

def resumo(p=0, a=0, d=0):
    aum = aumentar(p, a)
    dim = diminuir(p, d)
    do = dobro(p)
    me = metade(p)

    print('=' * 30)
    print('Resumo Do Preço'.center(30))
    print('=' * 30)

    print(f"Preço Analisado: \t{moeda(p)}\n"
          f"Dobro do Preço: \t{do}\n"
          f"Metade do Preço: \t{me}\n"
          f"{a}% de Aumento: \t{aum}\n"
          f"{d}% de Redução: \t{dim}\n")