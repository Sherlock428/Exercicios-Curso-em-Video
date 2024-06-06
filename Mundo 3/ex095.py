lista_jogadores = []  # Inicializa uma lista vazia para armazenar os jogadores e seus dados

while True:  # Loop principal para adicionar jogadores

    # Solicita o nome do jogador e armazena em um dicionário
    jogadores = {"Nome": input("Nome Jogador: ")}
    
    # Pede o número de partidas jogadas
    partidas = int(input("Digite o Número de Partidas Jogadas: "))
    gols = []  # Lista para armazenar o número de gols em cada partida

    # Loop para registrar o número de gols em cada partida
    for i in range(partidas):
        gol = int(input(f"Digite o Número de Gols na {i+1}° Partida: "))
        gols.append(gol)  # Adiciona o número de gols à lista

    # Adiciona os dados coletados ao dicionário do jogador
    jogadores['Gols'] = gols
    jogadores['Total'] = sum(gols)  # Calcula o total de gols
    jogadores['Partidas'] = partidas
    lista_jogadores.append(jogadores)  # Adiciona o dicionário do jogador à lista

    # Pergunta se deseja continuar adicionando jogadores
    cont = ' '
    while cont not in 'SN':
        cont = input("Digite apenas (S/N) para Continuar: ").upper()
    
    if cont == "N":  # Se a resposta for 'N', sai do loop
        break

# Exibe os dados dos jogadores
print()
for i, v in enumerate(lista_jogadores):
    nome = v['Nome']
    gols = v['Gols']
    total = v['Total']

    print(f"{i} Nome: {nome} Gols: {gols} Total: {total}")

print()

# Loop para exibir dados de jogadores individualmente
n = 0

while n != 999:

    n = int(input("Selecione qual jogador(999 para finalizar): "))

    if n < len(lista_jogadores):  # Verifica se o índice fornecido está dentro do intervalo válido

        dados = lista_jogadores[n]  # Obtém os dados do jogador selecionado
        nome = dados['Nome']
        gols = dados['Gols']
        partidas = dados['Partidas']

        print(f"Os dados do jogador {nome}")
        for partida, gol in enumerate(gols):  # Exibe o número de gols em cada partida

            print(f"Na {partida+1}° partida fez {gol}: ")
    
    elif n == 999:  # Se o usuário fornecer 999, encerra o programa
        print("Fim da execução")
        

        