def leiaInt(texto):
    print(texto, end='')
    n = input("")

    while not n.isnumeric(): 
        print("\033[91mERRO: Digite um número inteiro\033[0m")
        n = input("Digite um número: ")
    
    int(n)     
    
    return n

    
   



#programa principal
n = leiaInt("Digite um Número Inteiro: ")
print(f"Você acabou de digitar o número {n}")