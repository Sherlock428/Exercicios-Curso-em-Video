#Analisando Dados de um grupo
maior_18 = 0
mas = 0
fem = 0
while True:
    idade = int(input("Digite sua idade: "))
    sexo = ' '
    while sexo  not in "MF":
        sexo = input("Qual seu sexo: (M/F)").upper()

    if idade > 18:
        maior_18 += 1

    if sexo == "M":
        mas += 1

    if sexo == "F" and idade < 20:
        fem += 1
   
    cont = ' '  
    while cont not in "SN":
        cont = input("Deseja continuar S/N: ").upper()

    if cont != "S":
        break

print(f"Total de Pessoas maiores que 18 anos cadastrada são {maior_18}\n"
      f"Total de Homens cadastrados {mas}\n"
      f"Total de Mulheres menores que 20 anos cadastradas {fem}")