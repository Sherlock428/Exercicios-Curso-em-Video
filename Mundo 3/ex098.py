from time import sleep

def contagem():

    for n in range(1, 11, 1):
        print(n, end=' ')

    
    print("FIM!!!")

    print('=================================')

    for n in range(10, -2, -2):
        print(n, end=' ')
        sleep(0.5)
    
    print("FIM!!!")


    print("Agora é sua vez de personalizar: ")

    num_one = int(input("Digite o primeiro número da razão: "))
    num_final = int(input("Digite o último número da sequencia: "))
    razao = int(input("Digite os passos: "))

    for n in range(num_one, num_final, razao):
        print(n, end=' ')
        sleep(0.5)
    
    print("FIM!!!")
contagem()