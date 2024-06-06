import random

pedra = "pedra"
tesoura = "tesoura"
papel = "papel"

cr = random.choice([pedra, papel, tesoura])
print("""
Jokenpo, Escolha seu movimento

[1] Pedra
[2] Tesoura
[3] Papel

""")

escolha = int(input("Qual sua Escolha: "))

if escolha == 1 and cr == tesoura:
    escolha = pedra
    print(f"Você jogou {escolha} e o Npc {tesoura}\n"
          f"Você Venceu")
    
elif escolha == 1 and cr == papel:
    escolha = pedra
    print(f"Você jogou {escolha} e o Npc {papel}\n"
          f"Você Perdeu")

elif escolha == 1 and cr == pedra:
    escolha = pedra
    print(f"Você jogou {escolha} e o Npc {pedra}\n"
          f"Vocês Empataram")

elif escolha == 2 and cr == papel:
    escolha = tesoura
    print(f"Você jogou {escolha} e o Npc {papel}\n"
          f"Você Venceu")

elif escolha == 2 and cr == pedra:
    escolha = tesoura
    print(f"Você jogou {escolha} e o Npc {pedra}\n"
          f"Você Perdeu")

elif escolha == 2 and cr == tesoura:
    escolha = tesoura
    print(f"Você jogou {escolha} e o Npc {tesoura}\n"
          "Vocês Empataram")

elif escolha == 3 and cr == pedra:
    escolha = papel
    print(f"Você jogou {escolha} e o Npc {pedra}\n"
          f"Você Venceu")

elif escolha == 3 and cr == tesoura:
    escolha = papel
    print(f"Você jogou {escolha} e o Npc {tesoura}\n"
          "Você Perdeu")

else:
    escolha = papel
    print(f"Você jogou {escolha} e o Npc {papel}\n"
          "Vocês Empataram")