"""Aumento de Sálario"""
def salarios():
    while True:
        try:
            salario = float(input("Digite seu Sálario Atual: "))
            aumento = int(input("Digite a Taxa de Aumento para sálarios Abaixo de R$1200,00 reais: "))
            aumento1 = int(input("Digite a Taxa de Aumento para Sálarios Acima de R$1200,00 reais: "))
            return salario, aumento, aumento1
        except ValueError:
            print("ERROR: Digite um Valor Válido")
"""Função que Retorna os Valores Digitados Pelo Úsuario"""
def aumento(salario, aumento, aumento1):
    s = salario
    taxa = aumento
    taxa1 = aumento1
    
    if s > 1200.00:
        aum = s * (taxa1/100)
        aum1 = s + aum

        print(f"\nSeu Sálario atual de R${s:.2f} reais\n"
              f"Sofrerá Auemnto de {taxa1} no valor de {aum}\n"
              f"Ficará R${aum1:.2f} reais\n")
    else:
        aum = s * (taxa/100)
        aum1 = s + aum
        print(f"\nSeu Sálario atual de R${s:.2f} reais\n"
              f"Sofrerá Aumento de {taxa} no valor de {aum}\n"
              f"e ficará {aum1}\n")

    return taxa, aum, aum1
"""Função que faz os Cálculos de Aumento"""
def design():
    print(f"""
    ===================================
             Aumento de Sálario
    ===================================
    """)
"""Função que faz o Design"""
def main():
    while True:
        design()
        s, a, a1 = salarios()
        aumento(s, a, a1)

        cont = input("Deseja Continuar usando o app ? (S/N): ").upper()

        if cont != "S":
            break
"""Função Principal Responsável por rodar todo o código"""
main()