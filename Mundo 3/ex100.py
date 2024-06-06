from time import sleep
from random import randint

def sortear_num():

    num_sorteados = []

    print("Os números sorteados são: ", end=" ")
    for n in range(5):
        n = randint(0, 9)
        num_sorteados.append(n)
        sleep(0.3)
        
        print(f"{n}", end=' ', flush=True)
    
    print("Pronto")


    return num_sorteados

def somar(num_sorteados):
    numeros_somar = []
    for n in num_sorteados:
        if n % 2 == 0:
            numeros_somar.append(n)

    soma_total = sum(numeros_somar)
    print(f"A Soma dos Valores pares são: {soma_total}" )

a = sortear_num()
somar(a)