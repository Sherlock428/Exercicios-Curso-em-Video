#Validação de dados
p = 0
soma = 0
lista = []
lista_i = []
n_f = {}
nome = []
acm = {}
while True:
    pessoas = {"Nome": input("Nome: "),
               "Sexo": input("[M/F]: ".upper()),
               "Idade": int(input("Idade: "))}

    while pessoas["Sexo"] not in ['M', 'F']:
        pessoas['Sexo'] = input("ERROR: Digite apenas (M/F)").upper()
    
    p += 1
    lista.append(pessoas)
    lista_i.append(pessoas["Idade"])

    if pessoas["Sexo"] == "F":
        nome.append(pessoas["Nome"])
    cont = ' '
    while cont not in 'SN':
        cont = input("Digite Apenas (S/N) para continuar: ").upper()
    if cont == "N":
        break

soma = sum(lista_i)
media = soma / p

if pessoas["Idade"] > media:
    acm["Nome"] = pessoas['Nome']
    acm["Idade"] = pessoas['Idade']
    

print(f"A) A Quantidade de pessoas cadastradas forma {p}\n"
      f"B) A média de idades de todos foram {media}\n"
      f"C) As Mulheres cadastradas foram", end=' ')

for n in nome:
    print(n, end=' ') 

print("\nD) Pessoas acima da média")

for k, v in acm.items():
    print(f"{k} = {v}", end=' ')

