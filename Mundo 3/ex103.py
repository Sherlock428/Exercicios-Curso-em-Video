def ficha_jogador(nome_j='', n_gols=''):

    if nome_j == '':
        nome_j = "<desconhecido>"

    if n_gols == '':
        n_gols = 0
        int(n_gols)
    return nome_j, n_gols

nome = input("Digite o nome do jogador: ")
gols = input("Digite a quantidade de gols feitos: ")
nome_jogador, numero_gols = ficha_jogador(nome, gols)
print(f"{nome_jogador} fez {numero_gols} gol(s) no campeonato")

# def ficha_jogador(nome_j="<desconhecido>", n_gols=0):
#     print(f"{nome_j} fez {n_gols} gols(s) no campeonato.")

# nome = input("Digite o nome do jogador: ")
# gols = input("Digite a quantidade de gols feitos: ")

# if gols.isnumeric():
#     gols = int(gols)
# else:
#     gols = 0

# if nome.strip() == '':
#     ficha_jogador(n_gols=gols)

# else:
#     ficha_jogador(nome, gols)