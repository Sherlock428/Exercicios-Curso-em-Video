
numeros = (int(input("Digite um número: ")),
     int(input("Digite um número: ")),
     int(input("Digite um número: ")),
     int(input("Digite um número: ")))
     

numero_setados = set(numeros)
for n in numero_setados:
    repeticao = numeros.count(n)   

    if repeticao > 1:
        print(f"O número {n} se repetiu {repeticao} vezes ")  

print(f"O número na segunda posição é: {numeros[1]}")
quantidade = 0

for i in numeros:
    if i % 2 == 0:
        quantidade += 1

print(f"Tem cerca {quantidade} números pares")        


           