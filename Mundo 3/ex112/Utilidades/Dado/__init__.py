def leiadado(texto):
    p = input(texto).replace(',', '.').strip()
    
    if p.isalpha() or p == '':
        while p.isalpha() or p == '':
            print('\033[0;31merro\033[m')
            p = input('Digite o preço: R$').replace(',', '.').strip()

    else: 
        return float(p)


    # if float(p) == float(p):
    #     return float(p)
    
        


