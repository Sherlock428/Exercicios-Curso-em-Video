import urllib as ul
import urllib.request

url = 'https://www.pudim.com.br'

try:
    site = urllib.request.urlopen('https://www.pudim.com.br')

except ValueError:
    print('Não está acessivel')
else:
    print('funcionando')