def notas(*n, sit=False):
    maior = 0
    menor = 0
    soma = 0
    c = 0
    for nota in n:
        soma += nota
        c += 1
        if nota > maior:
            maior = nota
        if nota < menor:
            menor = menor
    
    media = soma / c
    if media >= 6:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
    if sit:
        c_notas = {"total": c,
                "Maior": maior,
                "Menor": menor,
                "Media": media,
                "Situacao": situacao
                }
    
    else:
        c_notas = {
            "Total:": c,
            "Maior": maior,
            "Menor": menor,
            "Media": media
        }
    return c_notas

#programa principal
resp = notas(5.5, 2.5, 10, 6.5, sit=True)
print(resp)