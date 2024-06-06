def media_velho_novo(nomes, idades, sexos, divisor, soma):
    media = soma / divisor
    velho = max(idades)
    menos = sum(1 for idade in idades if idade < 20)

    return media, velho, menos


divisor = 2
nomes = []
idades = []
sexos = []



for i in range(2):
    nome = input(f"{i+1}° Pessoa Nome: ")
    idade = int(input(f"{i+1}° Pessoa Idade: "))
    sexo = input(f"{i+1}° Pessoa Sexo: ")

    nomes.append(nome)
    idades.append(idade)
    sexos.append(sexos)

soma_idades = sum(idades)

media, velho, menos = media_velho_novo(nomes, idades, sexos, divisor, soma_idades)

for n, (nome, idade, sexo) in enumerate(zip(nomes, idades, sexos)):
    print(f"A Média de idades é: {media}")
    print(f"O mais velho é a Pessoa {n+1}, com idade de {velho}")
    print(f"O que Possuem menos de 20 São: {menos}")
