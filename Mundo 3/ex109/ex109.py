import moeda

preco = float(input("Digite o preco: R$"))

print(f"O aumento de 10% no preço {moeda.moeda(preco)} é de {moeda.aumentar(preco, 10, True)}\n"
      f"O Desconto de 10% no preco {moeda.moeda(preco)} é de {moeda.diminuir(preco, 10, True)}\n"
      f"O Dobro de {moeda.moeda(preco)} é de {moeda.dobro(preco, True)}\n"
      f"A metade de {moeda.moeda(preco)} é de {moeda.metade(preco, True)}")

