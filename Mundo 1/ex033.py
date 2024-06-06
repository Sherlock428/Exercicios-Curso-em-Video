"""Menor e Maior |Valor"""
def min_max(lista):
    
        menor = min(lista)
        maior = max(lista)

        
        return menor, maior
"""Função que Define e Retorna o Menor e Maior Valor"""
def mair_e_menor(lista, menor, maior):
        
        for element in lista:
            if element < menor:
                menor = element
            if element > maior:
                maior = element
"""Função que faz a checagem se do valor"""
def main():
    valores = [20, 30, 10, 5, 40]
    me, ma = min_max(valores)
    print(f"{ma}, {me}")
"""Função Principal que Roda todo o código"""
main()
        