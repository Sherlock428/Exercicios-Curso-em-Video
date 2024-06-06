"""Programa que Cálcula o valor pago por em viagem de Ônibus"""
def distancias():
    """Função que armazena o valores digitados"""
    while True:
        try:
            dist = int(input("Qual a Distância que irá percorrer em km ? "))
            valor_p = float(input("Qual Valor por cobrado por km ? "))
            valor_m = float(input("Valor cobrado por km acima de 200 km "))

            return dist, valor_p, valor_m
        except ValueError:
            print("ERROR: Digite um Valor Válido")
def valores(dist, valor_p, valor_m):

    d = dist
    vp = valor_p
    vm = valor_m

    if d < 200:
        vf = d * vp
        print(f"Valor para Percorrer {d} é de R${vf:.2f} reais")
    else:
        vf = d * vm
        print(f"Valor para Percorrer {d} por acima de 200km o valor será R${vf:.2f} reais ")
    return vf
"""Função que faz o cálculo com os valores"""
def design():
    print(f"""

    ===============================
        Consulte sua passagem!
    ===============================

                """)
"""Função responsável pelo design"""
def main():
    """Função Principal Responsável por rodar todo o código"""
    while True:
        design()
        d, vp, vm = distancias()
        valores(d, vp, vm)
        
        cont = input("Deseja Continuar Consultando o Valor de sua passagem ? (S/N) ").upper()

        if cont != "S":
            break
main()