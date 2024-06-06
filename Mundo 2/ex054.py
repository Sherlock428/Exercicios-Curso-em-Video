# Função para verificar se uma pessoa é maior de idade
def eh_maior_idade(ano_nascimento):
    idade = 2023 - ano_nascimento

    return idade >= 21

# Lista para armazenar os anos de nascimento
ano_nascimento = []

# Loop para solicitar os anos de nascimento das 7 pessoas
for i in range(7):
    ano = int(input(f"Ano da pessoa{i+1}: "))
    ano_nascimento.append(ano)

# Loop para verificar se cada pessoa é maior de idade e imprimir o resultado
for i, ano in enumerate(ano_nascimento):
    if eh_maior_idade(ano):
        print(i, "É maior de idade")
    else: 
        print(i, "Não é maior de idade")


