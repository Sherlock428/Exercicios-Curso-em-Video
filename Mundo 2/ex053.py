# Definição da função polindromo
def polindromo(frase):
    # Remover espaços e caracteres especiais da frase (opcional)
    frase = ''.join(caractere for caractere in frase if caractere.isalnum())

    # Verificar se a frase original é igual à sua inversão (se é um palíndromo)
    return frase == frase[::-1]

# Solicitar ao usuário que digite uma palavra ou frase
frase1 = input("Digite uma Palavra ou Frase: ")

# Verificar se a frase1 é um palíndromo usando a função polindromo
if polindromo(frase1) == True:
    # Se for um palíndromo, imprimir que é um palíndromo
    print(f"""
{frase1}
É um Palíndromo
          """)
else:
    # Se não for um palíndromo, imprimir que não é um palíndromo
    print(f"""
{frase1}
Não é um Palíndromo
""")
