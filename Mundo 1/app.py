#Conversor de temperatura de Celsius para Fahrenheit e Kelvin

"""Função que Armazena o Valor da Temperatura"""
def temp():

    while True:
        try:
            temp = float(input("Digite a Temperatura: ")) 
        except ValueError:
            print("ERROR: Digite um Valor Válido")
        
        return temp    
"""Função que Faz os Cálculos da Temperatura"""
def calc(temp):
    print(f"Escolha O que Desejar Converter Para:\n"
          f"\n[1] = Celsius\n"
          f"[2] = Fahrenheit\n"
          f"[3] = Kelvin\n")
    
    choice = int(input("Digite Aqui: "))

    if choice == 1:
        grau = "Celsius"
        sgrau = "C°"
        mgrau1 = "Farenheit"
        mgrau2 = "Kelvin"
        smgrau1, smgrau2 = "F°", "K°"
        celsiusf = (temp - 32) * 5 /9
        celsiusk = temp - 273
        return celsiusf, celsiusk, grau, sgrau, mgrau1, mgrau2, smgrau1, smgrau2

    elif choice == 2:
        grau = "Farenheit"
        sgrau = "F°"
        mgrau1 = "Celsius"
        mgrau2 = "Kelvin"
        smgrau1 = "C°"
        smgrau2 = "K°"
        farenc = temp * 1.8 + 32
        farenk = (temp + 459.67) * 5/9
        return farenc, farenk, grau, sgrau, mgrau1, mgrau2, smgrau1, smgrau2
    
    elif choice == 3:
        grau = "Kelvin"
        sgrau = "K°"
        mgrau1 = "Celsius"
        mgrau2 = "Farenheit"
        smgrau1 = "C°"
        smgrau2 = "F°"
        kelvinc = temp + 273
        kelvinf = temp * 1.8 + 459.67
        return kelvinc, kelvinf, grau, sgrau, mgrau1, mgrau2, smgrau1, smgrau2    
"""Funçção que Retorna um mini Design"""
def entrada():
    print("==========Bem-Vindo Ao Conversor de Temperatura CFK=========\n")
    print("Essa é uma versão básica v2 do Projeto Primário")
"""Função Principal Que Roda Todo o Código"""
def main():
    while True:
        entrada()
        tem = temp()
        res1, res2, g, sg, mg1, mg2, smg1, smg2 = calc(tem)

        print(f"A Temperatura de {tem} {smg1}/{smg2} Convertida para {g} é:\n"
            f"De {mg1} para {g} É: {res1:.0f} {sg}\n"
            f"De {mg2} para {g} É: {res2:.0f} {sg}\n")
        cont = input("Deseja Continuar Usando o APP: S/N\n"
                    "Digite Aqui: ").upper()
        
        if cont != "S":
            break

main()



#Melhorar todo o conversor, tentar fazer opções de escolhas, de qual converter