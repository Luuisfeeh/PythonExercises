galera = list()
dados = list()
p = list()
l = list()
pesado = leve = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(galera) == 0:
        pesado = leve = dados[1]
    else:
        if dados[1] > pesado:
            pesado = dados[1]
        if dados[1] < leve:
            leve = dados[1]

    galera.append(dados[:])
    dados.clear()
    resp = str(input('Deseja continuar?[S/N] ')).strip().upper()
    if resp == 'N':
        break
print('_-_'*20)
print(f'Nessa lista foram cadastradas {len(galera)} pessoas ')
print(f'O maior peso foi {pesado}Kg.Peso de ', end='')
for p in galera:
    if p[1] == pesado:
        print(f'[{p[0]}]', end=' ')
print('')
print(f'O peso mais leve foi {leve}Kg.Peso de ', end='')
for p in galera:
    if p[1] == leve:
        print(f'[{p[0]}]', end=' ')