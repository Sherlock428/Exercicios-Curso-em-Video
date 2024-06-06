"""Limite de Velocidade"""
def km_multa():
    while True:
        try:
            km_h = int(input("Qual a velocidade que você estava ? "))
            multa_v = float(input("Qual o valor da multa por Quilometros Ultrapassados ? "))
            velocity_permity = int(input("Qual a velocidade Permitida ? "))
            return km_h, multa_v, velocity_permity
        
        except ValueError:
            print("ERROR: Digite um Número Válido")
"""Função que Armazena o Valores Digitados"""
def velocimetro(km_h, multa_v, velocity_permity):
    km = km_h
    valor_mult = multa_v
    vp = velocity_permity
    if km > vp:
        multa = (km - vp) * valor_mult
        print(f"\nA {km}km/h está Acima da Velocidade Permitida, Receberá uma Multa de R${multa:.2f} reais")
        
    else: 
        print(f"{km}km/h É Velocidade Permitida")
"""Função que faz o Check do Limite de Velocidade"""
def design():
    print(f"""
    ================================
      Descubra qual será sua multa
    ================================
    """)
"""Função que faz um design"""

def main():
    while True:
        design()
        km, m, v = km_multa()
        velocimetro(km, m, v)

        cont = input("Deseja Continuar Consultando sua Multa ? (S/N) ").upper()

        if cont != "S":
            break
"""Função Principal Responsável por rodar todo o código"""
main()