"""Par ou Impar ?"""
def number():
    num = int(input("Digite um número: "))

    return num
"""Função que Retorna o Número Digitado """
def par_impar(num):
    n = num

    if n % 2 == 0:
        return "Par"
    else: 
        return "Ímpar"
"""Função que Faz a Checagem se o número é par ou ímpar"""
def design():
    print(f"""
============================
=      Par ou  Ímpar ?    = 
============================
    """)
"""Função responsável pelo Design"""
def main():
    while True:
        design()
        n = number()
        r = par_impar(n)

        print(f"O número {n} é {r}")

        cont = input("Deseja Continuar Usando o APP ? (S/N) ").upper()

        if cont != "S":
            break
"""Função Principal Responsável por rodar todo o código"""
main()