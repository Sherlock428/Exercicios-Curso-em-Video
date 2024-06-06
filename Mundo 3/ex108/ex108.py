import moeda

preco = float(input("Digite o Preço: R$"))
p = f"{preco:,.2f}"

p_f = p.replace(',', 'X').replace('.', ',').replace('X', '.')

met = moeda.metade(preco)
dob = moeda.dobro(preco)
aum = moeda.aumentar(preco, 10)
dim = moeda.diminuir(preco, 10)

met = f"{met:,.2f}"
dob = f"{dob:,.2f}"
aum = f"{aum:,.2f}"
dim = f"{dim:,.2f}"

met = met.replace(',', 'X').replace('.', ',').replace('X', '.')
dob = dob.replace(',', 'X').replace('.', ',').replace('X', '.')
aum = aum.replace(',', 'X').replace('.', ',').replace('X', '.')
dim = dim.replace(',', 'X').replace('.', ',').replace('X', '.')

# print(f"A metade de R${p_f} é R${met}\n"
#       f"O Dobro de R${p_f} é R${dob}\n"
#       f"O Aumento de 10% no R${p_f} é de R${aum}\n"
#       f"O Desconto de 10% no R${p_f} é de R${dim}\n")

print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))} ')