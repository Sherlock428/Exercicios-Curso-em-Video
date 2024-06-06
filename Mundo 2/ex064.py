n = 1
soma = 0
contador = 0
while n != 999:
    n = int(input("Digite um número: "))
    if n != 999:
        contador += 1
        soma += n

print(f"Você digitou {contador} números\n"
      f"A soma deles é {soma}")

