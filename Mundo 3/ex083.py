cont = "S"
lista = []
lista2 = []
maior = menor = 0
while True:
    lista.append(input("Nome: "))
    lista.append(float(input("Peso: ")))
    if len(lista2) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]
    lista2.append(lista[:])
    lista.clear()

    
    cont = ' '
    while cont not in "SN":
        cont = input("Desejar Continuar S/N: " ).upper()
    if cont == "N":
        break

print(f"Os dados {lista2}\n"
      f"{len(lista2)} Dados Cadastrados\n")
for p in lista2:
    if p[1] == maior:
        print(f"A pessoa mais pesada é {p[0] }")
    if p[1] == menor:
        print(f"A pessoa com menor peso é {p[0]}")
print(f"O Maior peso foi de {maior} kg\n"
      f"O menor peso foi de {menor} kg\n")