primeiro_termo = int(input("Digite o Primeiro Termo: "))
razao = int(input("Digite a razão: "))
termo = 10
pa = []
contador = 0

while contador < termo:
    pa.append(primeiro_termo)
    primeiro_termo += razao
    contador += 1
    
print(pa)