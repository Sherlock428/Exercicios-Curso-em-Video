def votação(ano):
    idade = 2024 - ano
    print(idade)
    if idade > 15 and idade > 60:
        print("Voto OPCIONAL")
    elif idade > 18:
        print("Voto OBRIGATÓRIO")
    else:
        print("Não pode VOTAR")


a = int(input("Digite seu Ano de Nascimento: "))

votação(a)
    
    
