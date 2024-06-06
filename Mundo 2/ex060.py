n = int(input("Digite um número: "))
fatorial = 1
contador = 2

while contador <= n:
    fatorial *= contador
    contador += 1

print(fatorial)

