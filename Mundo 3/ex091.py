from random import randint
from time import sleep
from operator import itemgetter
jogadores = {"jogador1": randint(1, 6),
             "jogador2": randint(1, 6),
             "jogador3": randint(1, 6),
             "jogador4": randint(1, 6)
             }

ranking = []

print("Valores sorteados")
for k, v in jogadores.items():
    sleep(0.5)
    print(f"{k} tirou {v}")
    ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    i += 1
    print(f"{i}° lugar {v[0]}, com valor {v[1]}")