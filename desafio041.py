import datetime

ano = int(input('Em que ano você nasceu? '))
anoa = datetime.date.today().year
idade = anoa - ano

print('Sua idade é {}'.format(idade))
if  idade <= 9:
    print('Você é atleta MIRIM!')
elif 14 >= idade:
    print('Você é atleta INFANTIL!')
elif 19 >= idade:
    print('Você é atleta JUNIOR!!')
elif 25 >= idade:
    print('Você é atleta SÊNIOR!!!')
elif 100 >= idade:
    print('Você é atleta MASTER!!!!')
