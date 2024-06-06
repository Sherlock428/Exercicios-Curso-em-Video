from random import randint

numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

for n in numeros:
    print(f"{n}", end=' ')
print(f"\nO maior número é: {max(numeros)}\n"
    f"O menor número é: {min(numeros)}")