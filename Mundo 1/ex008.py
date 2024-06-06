"""Conversor de Medidas em Metro"""
def valor():
    """Função que retorna o valor digitado, essa função retorna o valor armazenado na variavel metro"""
    while True:
        try:
            metro = int(input("Digite um número em metro "))
            return metro

        except ValueError:
            print("ERROR, Digite um número válido")


def resultado(paralelepipado):
    """Função que faz a conversão de metros para centímetros e milímetros, para retornar os valores cent e mili"""
    cent = paralelepipado * 100 
    mili = paralelepipado * 1000
    quil = paralelepipado / 1000
    #print( f"Valor de {paralelepipado} metros, em centímetros é {cent}, em milímetros é {mili}, em quilometros {quil} ")
    return cent, mili, quil


def run():
    """função principal responsavél por rodar o código"""
    while True:
        m = valor()
        cent, mili, ultron = resultado(m)
        print(f"O valor de {m} em centímetros é: {cent}, e em milímetros {mili}, e em ultrometro {ultron}")

        continuar = input("Deseja continuar executando: S/N ").upper()
        if continuar != "S":
            break


run()
