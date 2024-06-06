primeiro_termo = int(input("Digite o Primeiro Termo: "))
razao = int(input("Digite a razão: "))
termo = int(input("Quantidade de termo: "))
contador = 0
pa = []
cont = 1
while contador < termo:
    pa.append(primeiro_termo)
    primeiro_termo += razao
    contador += 1

print(pa)


visualizar_mais = input("Deseja visualizar mais termos? ").upper()

while visualizar_mais == "S":
    termo = int(input("Quantidade de termos: "))
    while contador < termo:
        pa.append(primeiro_termo)
        primeiro_termo += razao
        contador += 1
    print(pa)
print("FIM")

