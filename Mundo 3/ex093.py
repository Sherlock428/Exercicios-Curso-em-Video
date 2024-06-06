jogador = {"Nome": input("Jogador: ")}
partida = int(input("Digite quantas partidas foram jogadas? "))
partidas = []
partidas.append(partida)
gols = []

for i in range(partida):
    gol = int(input(f"Quantos gols fez na {i+1}° Partida: "))
    gols.append(gol)

soma = sum(gols)
jogador["Gols"] = gols
jogador["Soma"] = soma


print(jogador)

for k, v in jogador.items():
    print(f"O campo {k} tem o valor de {v}")

print()
for i, g in enumerate(gols):
    print(f"Na partida {i+1}° fez {g} Gols")

