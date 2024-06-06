# Solicita ao usuário que digite uma expressão e armazena-a como uma string na variável 'expr'

expr = str(input("Digite uma expressão aqui: "))

# Inicializa uma lista vazia que será usada como uma pilha para acompanhar os parênteses na expressão
lista_expr = []

# Itera sobre cada caractere na expressão fornecida pelo usuário
for sim in expr:
    # Verifica se o caractere atual é um parêntese de abertura
    if sim == "(":
        # Se sim, adiciona-o à lista (representando a pilha)
        lista_expr.append('(')
    # Verifica se o caractere atual é um parêntese de fechamento
    elif sim == ")":
        # Verifica se a lista (pilha) não está vazia (ou seja, se há um parêntese de abertura correspondente)
        if len(lista_expr) > 0:
            # Se não estiver vazia, remove o último parêntese de abertura adicionado à lista (pilha)
            lista_expr.pop()
        else:
            # Se a lista (pilha) estiver vazia, adiciona um parêntese de fechamento extra e interrompe o loop
            lista_expr.append(')')
            break

# Verifica se a lista (pilha) está vazia (ou seja, se todos os parênteses de abertura têm correspondência)
if len(lista_expr) == 0:
    # Se estiver vazia, significa que a expressão é válida (todos os parênteses estão balanceados)
    print("Você fez uma expressão correta")
else:
    # Se a lista (pilha) não estiver vazia, significa que a expressão é inválida (parênteses não balanceados)
    print("Sua expressão tá errada")
           