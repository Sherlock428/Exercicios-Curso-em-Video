from ex112.Utilidades import Moeda
from ex112.Utilidades import Dado

preco = Dado.leiadado('Qual o preço: R$')
Moeda.resumo(preco, 12, 20)