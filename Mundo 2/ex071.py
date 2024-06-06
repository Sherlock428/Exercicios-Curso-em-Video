# Banco
notas = [100, 50, 20, 10, 5]  # Valores das notas disponíveis
quantidade_notas = [0, 0, 0, 0, 0]  # Inicializa a lista para rastrear a quantidade de cada nota durante o saque

while True:
    saque = int(input("Quanto você quer sacar? "))  # Solicita ao usuário o valor que deseja sacar

    # Loop para calcular a quantidade de cada nota necessária para o saque
    for i, nota in enumerate(notas):
        quantidade_notas[i] = saque // nota
        saque %= nota  # Atualiza o valor do saque para ser o resto após retirar a quantidade calculada de notas

    # Verifica se o saque foi bem-sucedido e imprime as notas
    if saque == 0 and sum(quantidade_notas) > 0:
        print("Notas entregues:")
        for i, quantidade in enumerate(quantidade_notas):
            if quantidade > 0:
                print(f"{quantidade} notas de {notas[i]}")
    else:
        print("Não foi possível sacar o dinheiro desejado.")

    # Pergunta ao usuário se deseja realizar outro saque
    continuar = " "
    while continuar not in "SN":
        continuar = input("Deseja continuar? (S/N): ").upper()
    
    if continuar == "N":
        break  # Interrompe o loop principal se o usuário decidir não continuar

