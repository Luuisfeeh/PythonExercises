import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.geeksforgeeks.org/')
except urllib.error.URLError:
    print("Não é possivel acessar esse site!")
else:
    print('Site foi acessado com sucesso')
    