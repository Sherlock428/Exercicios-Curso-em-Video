lista = []
maior = 0
menor = 99999

for p in range(0, 4):
    n = int(input(f"Digite um número na posição {p}: "))
    lista.append(n)

    if n == 0:
        maior = menor = lista[p]
    else:
        if lista[p] > maior:
            maior = lista[p]
        if lista[p] < menor:
            menor = lista[p]

print(lista)
print(f"O maior número {maior}", end='\n')

for i, na in enumerate(lista):
    if na == maior:
        print(i, end=' ')

print(f'\nO menor número {menor}')
for i, na in enumerate(lista):
    if na == menor:
        print(i, end=' ')
    
    # print(f"{i} {na}")