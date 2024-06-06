#Número por extenso

numero_ext = ("zero", "um", "dois", "três", "quatro", "cinco",
             "seis", "sete", "oito", "nove", "dez",
             "onze", "doze", "treze", "quartoze", "quinze",
             "dezeseis", "dezesete", "dezoito", "dezenove", "vinte")

while True:
    n = int(input("Digite um número de 0 a 20: "))

    if n >= 0 and n <= 20:
        print(f"{n} por extenso é {numero_ext[n]}")

    else:
        print("Número invalido, Digite um número de 0 a 20:")
        continue

    continuar = ' '
    while continuar not in "SN":
        continuar = input("Deseja continuar (S/N): ").strip().upper()
    
    if continuar == "N":
        break