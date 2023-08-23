import datetime

ano = int(input('Em que ano vc nasceu? '))
militar = datetime.date.today().year - ano

print('Quem nasceu em {} tem {} anos em {}'.format(ano,militar,datetime.date.today().year))

if militar < 18:
    print('Você não precisa se alistar ainda, apenas em {}!'.format(ano + 18))
elif militar > 18:
    print('Você já se alistou em {}, pode ficar tranquilo agora.'.format(ano + 18))
elif militar == 18:
    print('Esse ano você precisa se alistar URGENTE!')