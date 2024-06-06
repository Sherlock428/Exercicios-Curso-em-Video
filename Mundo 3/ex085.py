#criar matrizes em python


# Definindo as dimensões da matriz
linhas = 3
colunas = 3

# Inicializando uma matriz vazia
matriz = []

# Preenchendo a matriz com entradas do usuário
for i in range(linhas):  # Loop pelas linhas da matriz
    linha = []  # Inicializa uma nova linha vazia
    for j in range(colunas):  # Loop pelas colunas da matriz
        # Solicita ao usuário que digite um valor para a posição [i][j]
        valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
        linha.append(valor)  # Adiciona o valor à linha atual
    matriz.append(linha)  # Adiciona a linha completa à matriz
# Exibindo a matriz preenchida
for linha in matriz:  # Loop para exibir cada linha da matriz
    print(f"{linha}")  # Exibe a linha atual da matriz