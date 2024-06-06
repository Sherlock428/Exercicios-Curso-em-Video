def inteiro_i():
    while True:
        try:
            i = int(input("Digite um número inteiro: "))
            return i
        except (ValueError, TypeError):
            print("\033[91mError: Digite um número inteiro\033[0m")

def float_f():
    while True:
        try:
            f = float(input('Digite um número real: '))
            return f
        except (ValueError, TypeError):
            print("\033[91mErro digite um número Real\033[0m")


i = inteiro_i()
f =float_f()
print(f"Você digitou número inteiro {i} e número real {f}")