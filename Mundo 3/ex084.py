#impares e pares em uma lista:

numeros = [[], []]

for i in range(1, 8):
    n = int(input(f"Digite o {i}° número: "))

    if n % 2 == 0:
        numeros[0].append(n)

    if n % 2 == 1:
        numeros[1].append(n)

print(f"Os Números Pares são: {numeros[0]}\n"
      f"Os Números Ímpares são: {numeros[1]}\n")