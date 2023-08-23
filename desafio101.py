def voto(ano=0):
    from datetime import date
    atual = date.today().year
    global idade
    idade = atual - ano
    if idade < 16:
        return "Negado"
    elif 16 <= idade < 18 or idade > 60:
        return "Opcional"
    else:
        return "Obrigatório"


idade = 0
year = int(input('Em que ano você nasceu? '))
voto(year)
print('-+-'*20)
print(f'Com {idade} anos, seu voto é {voto(year)}')
