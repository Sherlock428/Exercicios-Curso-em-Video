def fatorial(n, show=False):
    """
        -> (n) Calcula fatorial de um número
        :param n: O número a ser calculado
        :param show: (opcional) Mostrar como foi realizado a conta
        :return: O Valor do fatorial
    """
    f = 1
    if show == False:
        for c in range(n, 0, -1):
            f *= c
        print(f)
    
    else:
        for c in range(n, 0, -1):
            print(f"{c}", end=' ')
            if c > 1:
                print("x", end=' ')
            else:
                print("=", end=' ')
            
            f *= c
        

    return f
    
f2 = fatorial(5, show=True)
print(f"{f2}", end=' ')
