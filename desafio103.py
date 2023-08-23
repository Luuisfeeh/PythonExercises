def ficha(j='<desconhecido>',gols=0):
    print(f'O jogador {j} fez {gols} gol(s) no campeonato.')


print('-+-'*15)
jogador = str(input('Nome do jogador: ')).strip()
gol = input('Número de Gols: ')
if jogador == "":
    if gol.isnumeric():
        ficha(gols=gol)
    else:
        ficha(gols=0)

elif gol == "":
    ficha(j=jogador)

else:
    ficha(jogador,gol)