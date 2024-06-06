sexo = input("M/F: ")

while sexo not in "MF":
    print("Sexo Invalido")
    sexo = input("Digite corretamente: ")

if sexo == "M":
    print("Masculino")
if sexo == "F":
    print("Feminino")