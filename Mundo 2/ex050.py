soma = 0
for n in range(0, 7):
    if n % 2 == 0:
        soma += n
        print(n)

print(f"A soma de todos os pares é: {soma}")