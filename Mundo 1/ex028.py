"""Advinhe o Número"""
import os
from time import sleep
from random import randint

def numero():
    while True:
        try:
            num = int(input("Escolha um Número de 0 a 100: "))
            
            return num
        
        except ValueError:
            print("ERROR: Digite um Número Válido")

def win(num, random_numb, tentativas):
    n = num
    rn = random_numb
    t = tentativas

    if n < rn:
        print(f"O Número que Escolhi é Maior que {n}")
        t += 1
    elif n > rn:
        print(f"O Número que Escolhi é Menor que {n}")
        t += 1
    elif n == rn:
        print(f"""
        ======================================
        Parabéns, O Número que Escolhi foi {n}
        Em Apenas {t} tentativas!
        ======================================
        """)
        t += 1
    

        return True
    
    return False

def design():
    print(f"""
    ===========================================
    =______________|MindMaster|_______________=
    ===========================================
    """)
    start = input("Aperte ENTER Para Iniciar: ")
    print("Iniciando...")
    sleep(2)
    os.system('cls')

    return start

def main():
    while True:
        design()
        random_numb = randint(0, 100)
        tentativas = 0
        while True:
            
            n = numero()
            if n > 100:
                print("ERROR, Apenas Número de 0 a 100")
            tentativas += 1
            if win(n, random_numb, tentativas):
                break

        cont = input("Deseja ir mais uma rodada? (S/N) ").upper()

        if cont != "S":
            print("Fim de Jogo...")
            sleep(2)
            os.system('cls')
            break
            
        else:
            print("Reiniciando...")
            sleep(2)
            os.system('cls')

main()
