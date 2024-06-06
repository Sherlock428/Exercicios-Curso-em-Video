qual_termo = int(input("Qual termo deseja encontrar: "))
primeiro_termo = int(input("O primeiro Termo: "))
razao = int(input("A Razão é: "))
resultado = primeiro_termo + (qual_termo - 1) * razao

for n in range(primeiro_termo, resultado, razao):
    
    print(n)

print(resultado)
