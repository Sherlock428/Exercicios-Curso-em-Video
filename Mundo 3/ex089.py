#boletim

boletim = []
deco = "=" * 50

while True:
    
    aluno = input(f"Digite o nome do aluno: ")
    nota1 = int(input(f"Digite a nota1 do aluno: "))
    nota2 = int(input(f"Digite a nota2 do aluno: "))
    media = (nota1 + nota2) / 2

    alunos = [aluno, nota1, nota2, media]
    boletim.append(alunos)





    cont = ' '
    while cont not in "SN":
        cont = input("Deseja continuar (S/N)").upper()
    if cont == "N":
        break
n = 0

print(deco)

for i, a in enumerate(boletim):
    print(f"{i} Nome: {a[0]:^7}  Nota1: {a[1]:^3}  Nota2: {a[2]:^3}  Média: {a[3]:^3}")
print(deco)

while n < 999:


    n = int(input("Deseja conferir a nota de qual aluno: (interromper 999)"))

    if n < len(boletim):
        a_s = boletim[n]
        a_nome = a_s[0]
        a_nota1 = a_s[1]
        a_nota2 = a_s[2]

        print(
            deco,
              f"\nAs Notas do Aluno: {a_nome}\n"
              f"Nota1: {a_nota1}\n"
              f"Nota2: {a_nota2}\n", deco)
      

