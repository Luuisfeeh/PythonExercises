from datetime import datetime
atual = datetime.today().year
novo = 0
velho = 0
for c in range(1,8):
    ano = int(input('Em que ano você nasceu? '))
    if atual - ano < 18:
        novo += 1
    else:
        velho += 1
print('No total tivemos {} pessoas menores de idade'.format(novo))
print('E tivemos {} pessoas que são maiores de idade'.format(velho))