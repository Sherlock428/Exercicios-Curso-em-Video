lista = []
contador = 0

while True:
    n = int(input("Digite um número: "))
    contador += 1

    lista.append(n)
    cont = ' '
    while cont not in "SN":
        cont = input("Deseja continuar (S/N): ").upper()

    if cont == "N":
        break

lista.sort(reverse=True)
print(f"A lista em ordem descrente é {lista}")

for  v in lista:
    if v == 5:
        print("Tem 5")
        break
    elif len(lista) <= v:
        print("não tem")