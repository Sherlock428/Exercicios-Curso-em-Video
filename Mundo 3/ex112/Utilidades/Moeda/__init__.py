def aumentar(p=0, t=0, f=True):
    a = (p * t) / 100
    res = p + a
    return res if f is False else moeda(res)

def diminuir(p=0, t=0, f=True):
    d = (p * t) / 100
    res = p - d
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
    print('Resumo de Valor'.center(30))
    print('=' * 30)

    print(f"Preço a Analisado: \t{moeda(p)}\n"
          f"Dobro do preço: \t{do}\n"
          f"A Metade do preço: \t{me}\n"
          f"{a}% de Aumento: \t{aum}\n"
          f"{d}% de Redução: \t{dim}")
