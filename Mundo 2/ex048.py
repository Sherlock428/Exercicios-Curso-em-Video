soma = 0

for i in range(0, 500, 3):
    if i % 2 != 0:
        print(i)
        soma += i
        
print(f"A soma de todos os números é: {soma}")
   