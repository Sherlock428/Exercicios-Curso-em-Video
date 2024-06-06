"""Calculador de Aumento de Salário"""
def inputs():
    """Função Responsável por armazenar os inputs"""
    while True:
        try:
            salario = float(input("Digite Seu Salário: "))
            tax = int(input("Digite A Porcentagem do Aumento: "))
        except ValueError:
            print("ERROR: Digite um Número Válido")
        return salario, tax
    
def calc(salario, taxa):
    """Função Responsável por Realizar os Calculos """
    sal, tax = salario, taxa
    desc = sal * (tax / 100)
    desc2 = sal + desc

    return desc, desc2

def entrada():
    """Função Responsável Pelo Design"""
    print("=========Bem-Vindo Ao Serviço Da Empresa AMSS=========")
    name = input("Digite Seu Nome Funcionário: ")

    return name

def main():
    """Função Principal Roda tudo"""
    while True:
        design = entrada()
        osal, tax = inputs()
        aum, aumr = calc(osal, tax)
        print(f"\n{design:=^40}\nSeu Salário é de R$ {osal:.2f} reais\nCom Aumento de {tax}%\nPassará a Receber R$ {aumr:.2f} reais\nValor de aumento de R$ {aum:.2f} reais")
        continuar = input("\nDesejar Continuar com Operação ? S/N ").upper()

        if continuar != "S":
            break

main()




#Código versão simples
#sal = float(input("Digite seu Sálario: "))
#tax = int("Digite Seu aumento")

#aum = sal * (15 / 100)
#aumr = sal + aum

#print(f"O Valor do Seu {sal} Salário, Sofrerá um Aumento de 15%, Valor do Seu Novo Salário é {aumr}, Com Reformulação de {aum}")