trabalhador = {"Nome": input("Nome: "),
               "Ano": int(input("Ano de Nascimento: ")),
               "Carteira": int(input("Número da Carteira (Digite 0 caso não tenha): "))}

if trabalhador["Carteira"] != 0:
    trabalhador["Ano_contrato"] = int(input("Digite o Ano de Contratação: "))
    trabalhador["Salario"] = float(input("Digite seu Salario R$"))

    trabalhador["Idade"] = 2024 - trabalhador["Ano"]
    trabalhador["Aposentadoria"] = trabalhador["Idade"] + (trabalhador["Ano_contrato"] + 35) - 2024

for k, v in trabalhador.items():
    print(f"- {k} tem o valor {v}")
    if k == trabalhador["Salario"]:
        print(f"{k} tem o valor de R${v}")