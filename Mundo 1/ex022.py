"""App que Faz Modificações no Nome"""
def enter():
    """Função Responsavél por retornar o Nome Completo""" 
    name = input("Digite Seu Nome Completo: ")
        # nname = name.replace(" ", "")
    return name

def prints(nome):
    """Função que mostra as alterações no nome"""
    name = nome
    namef = name.split()
    print(
        f"Seu nome com letras Maiúscula: {name.upper()}\n"
        f"Seu nome com letras Minuscula: {name.lower()}\n"
        f"\nQuantidade de letras em seu Nome: {len(name.replace(' ', ''))}\n"
        f"Quantidade de letras apenas do Primeiro Nome {len(namef[0])}"
    )

def design():
    """Função que Faz um Design Simples"""
    print("==========Bem-Vindo Ao MmNQLPN==========\n")

def main():
    """Função Principal que Roda todo o código"""
    while True:
        name = enter()
        design()
        prints(name)
        cont = input("Desejar Continuar Com Operação ? (S/N) ").upper()
        if cont != "S":
            break

main()

# """ name = input("Digite Seu Nome Completo ")
# print(
#    f"Seu nome com letras Maiúscula: {name.upper()}\n"
#    f"Seu nome com letras Minuscula: {name.lower()}\n"
#    f"Quantidade de letras em seu Nome: {len(name.replace(' ', ''))}\n"
# ) """
