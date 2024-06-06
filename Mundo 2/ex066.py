contador = 0
soma = 0
n = 0

while n != 999:
    n = int(input("Digite um número: "))
    if n != 999:
        soma += n
        contador += 1

if contador > 0:
    print(f"Quantidade de números {contador}\n"
          f"Soma dos números {soma}")