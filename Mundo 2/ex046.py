from time import sleep

def decolando():
    for n in range(10, 0, -1):
        print(n)
        sleep(1)
    
    print("DECOLANDO")

def design():
    print("""
====================================
          Decolagem de Foguete
====================================       
""")
    
def main():
    while True:
        design()
        decolando()

        cont = input("Deseja Continuar execução do app ? (S/N) ").upper()

        if cont != "S":
            break

main()