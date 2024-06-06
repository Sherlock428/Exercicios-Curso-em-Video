import math

primo = int(input("Digite um Número: "))
resultado = primo - 1
fatorial = math.factorial(resultado)
if  fatorial == -1 % primo:
    print(primo, "é um número primo")
else:
    print(primo, "Não é um número primo")