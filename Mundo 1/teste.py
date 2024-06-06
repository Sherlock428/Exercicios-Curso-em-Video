"""Sistema de Cálculo de Média refeito"""
def notas_env():
    """Essa função pega o valores das notas enviadas"""
    while True:
        try:
            nota1 = float(input("Digite a Primeira Nota do Aluno ")) #Armazena a Primeira nota do aluno
            nota2 = float(input("Digite a Segunda Nota do Aluno ")) #Armazena a Segunda nota do Aluno
            return nota1, nota2

        except ValueError:
            print("ERROR: Digite um número válido") #Caso o valor seja inválido


def calc_media(nota1, nota2):
    """Essa função faz o cálculo da média, ela pega os valores armazenadas da função notas_env"""
    media = (nota1 + nota2) / 2 #faz o cálculo da média
    return media


def verific_aprov(media, nome):
    """Faz a verificação se o Aluno foi ou não aprovado"""
    if media > 5:
        print(f"Sua Média {nome} é {media}\nParabéns, Você foi Aprovado!")
    else:
        print(f"Sua Média {nome} é {media}\nInfelizmente, Você foi Reprovado!")


def entrada():
    """Entrada é fica onde  coloca nome do aluno e um meia interface"""
    print("==========Calculando Média==========")
    nome = str(input("Digite seu Nome "))
    print(f"Seja Bem-vindo, {nome}! Ao Calculando Média")
    return nome


def exe_programa():
    """Função que executa o programa por completoo, e o repete caso queira continuar usando"""
    while True:
        nome = entrada()
        nota1, nota2 = notas_env()
        media = calc_media(nota1, nota2)
        verific_aprov(media, nome)

        continuar = input("Deseja continuar a Operação ? S/N ").upper()
        if continuar != "S":
            break

exe_programa()
