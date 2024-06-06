#jogo par ou ímpar
import random 

rodadas = 0
soma = 0

pontos_p = 0
pontos_c = 0

while rodadas < 5:
    n = int(input("Digite um Valor: "))
    player_escolha = input("Par ou Ímpar: [P/I]").upper()
    number_com = random.randint(0, 10)
    choice_com = random.choice(["P", "I"])
    resultado = n + number_com
    
  

    print(f"soma é {resultado}")

    if resultado % 2 == 0 and player_escolha == "P" or resultado % 2 != 0 and player_escolha == "I":
        print("Você acertou")
        pontos_p += 1
    elif resultado % 2 == 0  and player_escolha == "I" or resultado % 2 != 0 and player_escolha == "P":
        print("Você errou")
    
    if resultado  % 2 == 0 and choice_com == "P" or resultado % 2 != 0 and choice_com == "I":
        print("Maquina acertou")
        pontos_c += 1
    elif resultado % 2 == 0 and choice_com == "I" or resultado % 2 != 0 and choice_com == "P":
        print("Maquina errou")
    
    rodadas += 1

if pontos_p > pontos_c:
    print("Parabéns você ganhou")
else:
    print("Máquina venceu!")

    


