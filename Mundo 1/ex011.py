"""App Que Determina a quantidade de Litros de Tinta para pintar uma Parede"""
def var():
    while True:
        try:
            altura = float(input("Digite a Altura da Parede Em Metros "))
            largura = float(input("Digite a Largura da Parede Em Metros "))       
        except ValueError:
            print("ERROR: Digite um Número Válido")
        return altura, largura, 


def calc(altura, largura):
    area = altura * largura 
    litro = area / 2

    return area, litro

def entrad():
    print("=========Bem-vindo A Pintores.com=========")
    name = input("Digite Seu Nome Pintor: ")

    return name

def principal():
    while True:
        entrada = entrad()
        alt, larg = var()
        area, litro = calc(alt, larg)
        print(f"\n{entrada} A Altura da parede é {alt:.2f} e a Largura {larg:.2f}, totalizando uma Área de {area:.2f}m\u00B2, sendo necessário {litro}l de Tinta")
        continuar = input("Deseja Continuar Com Execução do Aplicativo S/N ? ")
        if continuar != "S":
            break
principal()
