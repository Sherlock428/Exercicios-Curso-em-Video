"""App que Verifica se Sua cidade tem o Nome 'Santa' """
def names():
    cityname = input("Digite O Nome Da Cidade: ").title()

    return cityname
"""Função que Retorna o Input que é o nome da cidade"""

def prints(cityname):
    cname = cityname
    print(f"""
A Cidade Escolhida é: {cname}
Procurando a palavra: 'Santa'
    """)
    return cname
"""Função que verifica se  possui o nome 'Santa' e mostra se tem ou não"""

def main():
    while True:
        cityname = names()
        cname = prints(cityname)

        if cname.find('Santa') == 0:
            print(f"A Cidade {cname}, Possui 'Santa' no Nome")
        else:
            print(f"A Cidade {cname}, Não possui 'Santa' no Nome")

        cont = input("Deseja Continuar com Operação: (S/N) ").upper()

        if cont != "S":
            break
"""Função principal que roda todo o código"""
main()












# cityname = input("Digite o Nome da Sua Cidade: ")

# Usando find() Para encontrar a palavra 'Santa' na variável cityname
# print(f"""
# A cidade é {cityname}:
# Procurando a palavra:'Santa'
# """)

# if cityname.find("Santa") == 0:
#    print(f"A Cidade {cityname} Começa com a palavra 'Santa' ")

# else:
#   print(f"A Cidade {cityname} Não começa com 'Santa'")
