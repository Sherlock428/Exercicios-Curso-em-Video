"""Formatação de um nome"""
def names():
    """Função que Retorna o Nome Completo"""
    name = input("Digite Seu Nome Completo: ")
    
    return name

def primer_end(name):
    """Função que faz formatação e Separa o primeiro e último nome """
    n = name
    nf = n.split()
    primer_name = nf[0]
    end_name = nf[-1]

    return nf, primer_name, end_name

def design():
    """Função que faz um Design Simples"""
    print("==========Bem-Vindo Ao NPE==========")

def main():
    """Função Principal que roda todo o código"""
    design()
    n = names()
    nf, pn, en = primer_end(n)

    print(f"Seu Nome Completo é: {n}\n"
          f"Seu Nome Fragmentado {nf}\n"
          f"Seu Primeiro Nome: {pn}\n"
          f"Seu Último Nome: {en}\n")
        
main()
#name = input("Digite Seu Nome Completo ")
#namef = name.split()
#primer_name = namef[0]
#end_name = namef[-1]

#print(primer_name, end_name)