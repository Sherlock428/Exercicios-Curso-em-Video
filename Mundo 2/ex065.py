n = 1

contador = 0
soma = quant = maior = menor = 0
cont = "S"
while n != 0:
    n = int(input("Digite aqui um número: "))
    if n != 0:
        soma += n
        contador += 1
        
        if contador == 1:
            maior = menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n

if contador > 0:
    media = soma / contador
    print(f"A media final é {media:.0f}\n"
          f"soma: {soma} "
          f"O número maior digitado é {maior}\n"
          f"O número menor digitado é {menor}\n")

