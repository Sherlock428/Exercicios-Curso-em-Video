"""App De Numeração Deciminal Posicional"""
def number():
    """Função que Retorna o Número Digitado de 0 a 9999"""
    num = int(input("Digite Um Número de 0 a 9999 "))
    return num

def prints(num):
    """Função que mostra os valor em Unidade, Dezena, Centena e Milha"""
    n1 = num
    u = n1 // 1 % 10
    d = n1 // 10 % 10
    c = n1 // 100 % 10
    m = n1 // 1000 % 10
    print(f"""
Unidade: [{u}]
Dezena: [{d}]
Centena: [{c}]
Milha: [{m}]
""")

    return u, d, c, m
def design():
    """Função que faz um simples Design"""
    print("==========Bem-Vindo Ao UDCM==========")

def main():
    """Função Principal que Roda todo o código"""
    while True:
        design()
        n1 = number()
        prints(n1)

        cont = input("Deseja Continuar Usando UDCM (S/N) ").upper()
        if cont != "S":
            break
    
main()








#num = input("Digite um número de 0 a 9999: ")

#print(f"""
#Unidade: {num[3]}
#Dezena: {num[2]}
#Centena: {num[1]}
#Milha: {num[0]}\n"""
#)