def maior_and_menor(pessoas):
    maior = max(pessoas)
    menor = min(pessoas)

    return maior, menor

pessoas = []

for i in range(5):
    peso = int(input(f"Digite O Peso Da {i+1}° Pessoa: "))
    pessoas.append(peso)

maior, menor = maior_and_menor(pessoas)

for i, peso in enumerate(pessoas):
    if peso == maior:
        print(f"A Pessoa com maior Peso é {i+1}, e seu peso é {maior}")
    elif peso == menor:
        print(f"A Pessoa com menor Peso é {i+1}, e seu peso é {menor}")    