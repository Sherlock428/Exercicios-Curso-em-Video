#analises de estatisticas
acima_1000 = 0
precos =  []
quantidade =  0
total = 0
produto_m = 0

while True:
    produto = input("Digite o nome do produto: ")
    preco = float(input("digite o preço do produto: "))
    precos.append(preco)

    if preco > 1000:
        acima_1000 += 1
    
    
    menor_preco = min(precos)
    
    if menor_preco:
        produto_m = produto

    quantidade += 1

    continuar = ' '
    while continuar not in "SN":
        continuar = input("Deseja continuar comprando? (S/N)").upper()
    
    if continuar != "S":
        break

for preco in precos:
    total += preco
    
print(f"Total da compra foi R${total:.2f}\n"
      f"Você comprou {quantidade} produtos\n"
      f"Comprou {acima_1000} produto a cima de R$ 1000\n"
      f"O Produto com menor preço {produto_m} custando R$ {menor_preco:.2f}")