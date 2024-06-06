"""Aplicativo que ver se o Ano é bissexto"""
def year():
    while True:
        try: 
            ano = int(input("Digite um Ano: "))

            return ano
        except ValueError:
            print("ERROR, Digite um número válido")
"""Função que armazena o dado do Ano"""
def bissexto(ano):
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f"O Ano {ano} é Bissexto")
    else:
        print(f"O Ano {ano} Não é Bissexto")

def desing():
    print(f"""
    ==============================
     Será que o Ano é Bissexto ?
    ==============================
    """)
"""Função Responsável pelo Design"""
def main():
    while True:
        desing()
        ano = year()
        bissexto(ano)

        cont = input("Desejar Continuar utilizando o App (S/N) ").upper()

        if cont != "S":
            break
"""Função Principal Responsável por rodar o código"""
main()