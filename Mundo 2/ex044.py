valor_do_produto = float(input("Digite o Valor do Produto: "))
"10%"
print("""
O Pagamento será realizado em que forma de pagamento 

[1] Cheque, 10% de desconto
[2] Cartão a vista, 5% de desconto
[3] Em até 2x No Cartão, preço Normal
[4] 3x Ou Mais no Cartão: 20% de Juros

""")

escolha = int(input("Escolha: "))

if escolha == 1:
    desconto = valor_do_produto * (10/100)
    valor_final = valor_do_produto - desconto
    print(f"O valor do produto passará a ser {valor_final:.2f} reais\n"
          f"Sendo descontado o valor de {desconto:.2f} reais")

elif escolha == 2:
    desconto = valor_do_produto * (5/100)
    valor_final = valor_do_produto - desconto
    print(f"O valor do produto passará a ser R$ {valor_final:.2f} reais\n"
          f"Sendo Descontado o valor de R$ {desconto:.2f} reais")
    
elif escolha == 3:
    print(f"O Valor a ser pago será o Mesmo do Produto {valor_do_produto:.2f}")

elif escolha == 4:
    parcelas = int(input("Em quantas vezes serão parcelado: "))
    acrescimo = valor_do_produto * (parcelas/100)
    valor_final = valor_do_produto + acrescimo
    print(f"O valor a Ser Pago pelo Produto Será R${valor_final:.2f} reais\n"
          f"Sendo Parcelado em {parcelas}\n"
          f"Terá um Acresimo de R${acrescimo:.2f} reais")