lista = []
ta_na_lista = False
while True:

    n = int(input("Quais números você deseja adicionar na lista: "))
    

    for v in lista:
        if v == n:  
            print("O Valor já está na lista")
            ta_na_lista = True
            break

    if not ta_na_lista:
        lista.append(n)

    cont = ' '
    while cont not in "SN":
        cont = input("Deseja continuar S/N: ").strip().upper()

    if cont == "N":
        break

print(lista)