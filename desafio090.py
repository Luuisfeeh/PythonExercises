alunos = list()
dados = dict()
while True:
    dados['aluno'] = str(input('Nome do aluno: ')).strip()
    dados['media'] = float(input('Média do aluno: '))
    if dados['media'] < 7:
        dados['situacao'] = 'REPROVADO'
    else:
        dados['situacao'] = 'APROVADO'
    alunos.append(dados.copy())
    resp = str(input('Deseja adicionar mais um aluno? [S/N]')).strip().upper()
    if resp == 'N':
        break
print('-+-'*16)
for i in alunos:
    print(f'O aluno {i["aluno"]} ficou com {i["media"]} de média.')
    print(f'Sua situação foi de {i["situacao"]}')
