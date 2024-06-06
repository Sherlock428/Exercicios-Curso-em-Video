linhas = 3
colunas = 3

matriz = []

for l in range(linhas):
    linhas = []
    for c in range(colunas):
        valor = int(input(f"Digite um valor para ser adicionado a matrix [{l}, {c}] "))
        linhas.append(valor)
    matriz.append(linhas)

for linha in matriz:
    print(linha)
somac = 0
for linha in matriz:
    somac += linha[-1]


soma = sum(matriz[-1])
print(soma)
print(somac)