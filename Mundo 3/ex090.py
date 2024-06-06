nome = input("Digite nome do aluno:  ")
media = float(input("Digite a média do aluno: "))

aluno = {'Nome': nome, "Média": media}

if aluno["Média"] >= 7:
    aluno["situação"] = 'Aprovado'

elif aluno["Média"] == 6:
    aluno["situação"] = 'Recuperação'

elif aluno['Média'] < 5:
    aluno["situação"] = 'Reprovado'

for c, v in aluno.items():
        
    print(f"{c} igual {v}")