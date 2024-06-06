#gerar resultados da megasena
import random

# Solicita ao usuário a quantidade de jogos que deseja fazer
jogos = int(input("Digite quantos jogos você quer jogar: "))

# Loop para criar a quantidade de jogos solicitada pelo usuário
for i in range(jogos):
    i += 1
    lista = []  # Inicializa uma lista vazia para armazenar os números de cada jogo

    # Loop para gerar 6 números únicos para cada jogo
    while len(lista) < 6:  # Enquanto a lista não tiver 6 números
        n_r = random.randint(0, 60)  # Gera um número aleatório entre 0 e 60
        
        # Verifica se o número gerado não está na lista
        if n_r not in lista:
            lista.append(n_r)  # Adiciona o número à lista se não estiver presente

        organizado = sorted(lista)  # Ordena a lista de números do jogo

    # Imprime a lista de números do jogo atual
    print(f"Jogo{i}: {organizado}")