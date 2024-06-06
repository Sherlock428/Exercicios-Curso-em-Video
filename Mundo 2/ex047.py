def contador():
    cont = 1

    return cont

def numeros_pares(cont):
    for n in range(0, 52, 2):
    
        print(n)
        cont += 1

    print(f"Cerca de {cont} são números pares até 50")

def desing():
    print("""
================================
          Números Pares 
                Até
                50
================================
""")
    
def main():
    while True:
        desing()
        a = contador()
        numeros_pares(a)

        cont = input("Deseja continuar usando o App? (S/N) ")

        if cont != "S":
            break

main()