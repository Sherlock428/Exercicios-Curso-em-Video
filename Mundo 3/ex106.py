import time, random, math

def sistema_ajuda(c):
    help(c)


def design(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
comando = ''    
while True:
    msg = "Sistema de Ajuda Pyhelp"
    design(msg)
    comando = input("Digite uma função ou biblioteca: ")

    if comando.upper() == 'fim':
        break
    else:
        sistema_ajuda(comando)