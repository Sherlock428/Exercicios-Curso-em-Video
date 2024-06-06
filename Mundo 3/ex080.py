lista = []

for v in range(0, 4):
    n = int(input(f"Adicione {v} a lista: "))
    lista.append(n)

o_lista = sorted(lista)

print(o_lista)