def ano_atleta():
    try:
        ano_do_atleta = int(input("Digite O Ano que você Nasceu: "))
        ano_atual = int(input("Digite O Ano Atual: "))

        return ano_do_atleta, ano_atual
    
    except ValueError:
        print("ERROR: Digite um Valor Válido")

def conversor(ada, aa):
   
    idade = aa - ada

    if aa < ada:
        print("Você Ainda não Nasceu Viajante do Tempo")

    elif idade <= 10:
        print("Você é um atleta MIRIM")
    elif idade <= 14:
        print("Você é um atleta INFANTIL")
    elif idade <= 19:
        print("Você é um atleta JUNIOR")
    elif idade <= 20:
        print("Você é um atleta SÊNIOR")
    else:
        print("Você é um atleta MASTER")
    
def design():
    print("""
==============================
        Nível Natação    
==============================
    """)

def main():
    while True:
        design()
        ada, aa = ano_atleta()
        conversor(ada, aa)

        cont = input("Deseja Continuar Executando o APP (S/N) ").upper()

        if cont != "S":
            break

main()

    