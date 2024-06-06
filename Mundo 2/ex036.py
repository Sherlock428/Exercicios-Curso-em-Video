def valores():
    while True:
        try:
            valor_da_casa = float(input("Qual o Valor da casa que deseja Comprar? "))
            renda_mensal = float(input("Qual Sua Renda Mensal? "))
            tempo_a_pagar = int(input("Quanto tempo deseja pagar? "))

            return valor_da_casa, renda_mensal, tempo_a_pagar
        except ValueError:
            print("ERROR: Digite um valor válido")

def prestacoes_a_pagar(vdc, rd, tap):

    prest_m = rd * 0.3
    prest_a = prest_m * 12
    total_pago = prest_a * tap

    if vdc <= total_pago:
        print(f"""
Podemos Realizar o Empréstimo 
As Prestações mensais ficaram por R$ {prest_m:.2f} reais
Anualmente ficará por {prest_a}
O valor total pago é {total_pago}
        """)
    else:
        print(f"""
O Emprestimo não poderá ser realizado
{prest_m} reais
{prest_a} Por ano
{total_pago} valor a ser pago        
              """)
def design():
    print("""
===================================
        Financie sua Casa 
            Pela FSC
===================================
    """)

def main():
    while True:
        design()
        vdc, rm, tap = valores()
        prestacoes_a_pagar(vdc, rm, tap)

        cont = input("Deseja continuar a Execução do Programa (S/N) ").upper()
        if cont != "S":
            break

main()