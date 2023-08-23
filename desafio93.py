futebol = dict()
dados = list()
futebol['jogador'] = str(input('Nome do Jogador: ')).strip()
tot = int(input(f'Quantas partidas {futebol["jogador"]} jogou? '))
for c in range(0,tot):
    dados.append(int(input(f'   Quantos gols na partida {c+1}? ')))
futebol['gols'] = dados[:]
futebol['total'] = sum(dados)
print('-+-'*17)
print(futebol)
print('-+-'*17)
for k,v in futebol.items():
    print(f'O campo {k} tem o valor {v}')
print('-+-'*17)
print(f'O Jogador {futebol["jogador"]} jogou {tot} partidas.')
for c in range(0,tot):
        print(f'   => Na partida {c+1}, fez {futebol["gols"][c]} gols.')
print(f'Foi um total de {futebol["total"]} gols.')
