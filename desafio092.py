dados = dict()
dados['nome'] = str(input('Digite seu nome: ')).strip()
ano = int(input('Em que ano você nasceu? '))
dados['idade'] = 2023 - ano
dados['ctps'] = int(input('Digite o número da sua carteira de trabalho: [0 caso não tenha]'))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de contrtação: '))
    dados['salario'] = int(input('Salário: R$'))
    dados['aposentadoria'] = (dados['contratacao'] - ano) + 35
print('-+-'*20)
for k,v in dados.items():
    print(f'  - {k} tem o valor {v}')