def aumentar(p=0, t=0, format=True):
    a = (p * t) /100
    res = p + a
    return res if format is False else moeda(res)

def diminuir(p=0, t=0, format=True):
    d = (p * t) / 100
    res = p - d
    return res if format is False else moeda(res)

def dobro(p=0, format=True):
    res = p * 2
    return res if format is False else moeda(res)

def metade(p=0, format=True):
    res =  p / 2
    return res if format is False else moeda(res)

def moeda(p=0, moeda='R$'):
    return f'{moeda}{p:.2f}'.replace('.', ',')

def resumo(p=0, au=0, di=0):
    a = aumentar(p, au)
    d = diminuir(p, di)
    do = dobro(p)
    me = metade(p)
    titulo = 'Resumo de Valor'.center(30)
    tam = len(titulo) + 20
    print('=' * 30)
    print(f"{titulo}")
    print('=' * 30)
    print(f"Preço Analisado: \t{moeda(p)}\n"
          f"Dobro do Preço: \t{do}\n"
          f"Metade do Preço: \t{me}\n"
          f"{au}% de Aumento: \t{a}\n"
          f"{di}% de Redução: \t{d}\n")
    
    print('_' * 30)