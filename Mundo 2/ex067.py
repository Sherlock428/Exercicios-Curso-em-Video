#Tabuada

n = 0
contagem = 0

while n >= 0:
    n = int(input("Digite o número que quer checar a tabuada:  "))
    for i in range(1, 11):
        resultado = n * i
    
        print(f"n x {i} = {resultado} ")
    print("______________")
        
