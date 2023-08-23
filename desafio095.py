time = list()
futebol = dict()
dados = list()
while True:
    futebol.clear()
    futebol['jogador'] = str(input('Nome do Jogador: ')).strip()
    tot = int(input(f'Quantas partidas {futebol["jogador"]} jogou? '))
    dados.clear()
    for c in range(0,tot):
        dados.append(int(input(f'   Quantos gols na partida {c+1}? ')))
    futebol['gols'] = dados[:]
    futebol['total'] = sum(dados)
    time.append(futebol.copy())
    while True:
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if resp in 'SN':
            break
        print('ERROR.Por favor digitar apenas S ou N')
    if resp == 'N':
        break
print('-+-'*17)
print('cod ',end='')
for u in futebol.keys():
    print(f'{u:<15}',end='')
print()
print('-+-'*17)
for k,v in enumerate(time):
    print(f'{k:>3} ',end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('-+-'*17)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO. Não existe jogador com código {busca}')
    else:
        print(f'-- Levantamento do JOGADOR {time[busca]["jogador"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-+-' * 17)
print('<< VOLTE SEMPRE >>')