import random



def numero_digitado():
    n = int(input("Digite um número: "))
    return n


def win_lose(num, random_num, tentativas):

    n = num
    rn = random_num
    t = tentativas

    if n > rn:
        print("O número que escolhi é menor")
        t += 1
    elif n < rn:
        t += 1
        print("O número que escolhi é maior")
    elif n == rn:
        print(f"Parabéns, você acertou o número que eu escolhi é: {random_num} "
              f"Você acertou em {t} tentativas")
        t += 1
        return True
    
    return False


def main():
    tentativas = 0
    random_num = random.randint(0, 100)
    while True:
        num = numero_digitado()

        if win_lose(num, random_num, tentativas):
            break
        tentativas += 1


main()
