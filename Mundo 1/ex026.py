"""App  que Verifiaca quantas vezes apareceu uma letra na frase"""
def phraser():
    """Função que Retorna a Frase Escrita"""
    phrase = input("Digite Uma Frase: ")

    return phrase

def prints(phrase):
    """Função que procura a letra na frase, e mostra quantas vezes ela aparece"""
    phr = phrase

    #if phr.find("a") != -1 or phr.rfind("a"):
    print(f"""
Na frase {phr}
A Letra "a" Aparece {phr.count('a')}
E a Primeira Vez {phr.find("a")}
E a Última Vez {phr.rfind("a")}
        """)

def design():
    """Função que faz um Design simples"""
    print("==========Bem Vindo Ao Tem 'a' ?==========")

def main():
    """Função Principal Responsável por rodar todo o código"""
    while True:
        design()
        phr = phraser()
        prints(phr)

        cont = input("Deseja Continuar Usando o App (S/N) ").upper()

        if cont != "S":
            break





#phrase = input("Digite um frase ")

#if phrase.find("a") != -1 or phrase.rfind("a"):
#print(f"""
#Na Frase {phrase}
#A Letra 'a' Aparece {phrase.count('a')} 3 Vezes
#E a Primeira Vez No Caractere {phrase.find('a')}
#E a Última vez no {phrase.rfind('a')}""")
#else:
#print(
    #f"Na Frase {phrase} Não Possui a letra 'a'")
