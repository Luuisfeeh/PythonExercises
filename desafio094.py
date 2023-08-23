dados = dict()
pessoas = list()
soma = media = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: ')).strip()
    while True:
        dados['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
        if dados['sexo'] in 'MF':
            break
        print('ERRO. Por favor digite M ou F.')
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    pessoas.append(dados.copy())
    while True:
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if resp in 'SN':
            break
        print('ERRO.Por favor digite S ou N.')
    if resp == 'N':
        break
print('-+-'*17)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas')
media = soma / len(pessoas)
print(f'B) A média de idade é de {media:.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in pessoas:
    if p['sexo'] in 'F':
        print(f'{p["nome"]} ', end='')
print()
print(f'D) Lista das pessoas que estão acima da média: ')
for p in pessoas:
    if p['idade'] >=media:
        print('    ', end='')
        for k,v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<<  ENCERRADO  >>>')