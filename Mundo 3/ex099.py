def maior_valor(*args):
    
    print("Analisando Valores Passados...")
    maior = 0 
    cont = 0

    for arg in args:
        
        print(f"{arg}", end=" ")
        cont += 1        
        if arg > maior:
            maior = arg
    print(f"Foram informados {cont} valores ao todo.", end=" ")
    print(f"\nO maior valor é {maior}")


maior_valor( 1, 2, 3 ,4)
maior_valor(9, 7, 6, 5, 9)
maior_valor(100, 20, 40, 50)
maior_valor(0)
maior_valor(1, 2)
maior_valor()