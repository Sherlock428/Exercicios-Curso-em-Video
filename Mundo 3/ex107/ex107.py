import moeda

preco = float(input("Digite o preço do produto: R$ "))
print(f"A Metade de R${preco:.2f} é R${moeda.metade(preco):.2f}\n"
      f"O Dobro de R${preco:.2f} é R${moeda.dobro(preco):.2f}\n"
      f"O Aumento de 10% em relação a preço de R${preco:.2f} é de R${moeda.aumentar(preco, 10):.2f}\n"
      f"O Desconto de 10% em relação a preço de R${preco:.2f} é de R${moeda.diminuir(preco, 10):.2f}")