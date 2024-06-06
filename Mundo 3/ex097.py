def escreva(msg):

    
    tam_msg = len(msg) + 4

    
    linha_superior = '=' * tam_msg 

    print(linha_superior)
    print(f"  { msg}")
    print(linha_superior)


msg = input("Digite um msg: ")
escreva(msg)
