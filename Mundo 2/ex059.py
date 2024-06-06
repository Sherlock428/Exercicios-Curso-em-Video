num1 = int(input("Digite primeiro Número: "))
num2 = int(input("Digite segundo Número: "))
f = 0
while f != 5:
    print("""
          
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Fechar Programa
""")
    escolha = int(input("Escolha: "))
    
    if escolha == 1:
        resultado = num1 + num2 
        print(f"A soma de {num1} + {num2} = {resultado}")

    elif escolha == 2:
        resultado = num1 * num2
        print(f"A multiplicação de {num1} x {num2} = {resultado} ")
    elif escolha == 3:
        if num1 > num2:
            print(f"O maior número é {num1}")
        elif num2 > num1:
            print(f"O maior número é {num2}")
        else:
            print("Os números são iguais")
    elif escolha == 4:
        num1 = int(input("Digite os novos números: "))
        num2 = int(input("Diigte os novos números: "))
    elif escolha == 5:
        f = 5
print("FIM")