listagem = ('Lapis', 1.00, 'Caneta', 1.25, 'Borracha', 0.50, 'Caderno', 20.00)

print('=' * 40)
print("Analises de Preço")
print('=' * 40)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f"{listagem[pos]:.<30}", end=" ")

    else:
        print(f"R$ {listagem[pos]:>7.2f}")