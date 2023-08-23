from desafio15.interface import *
from desafio15.arquivo import *
from desafio15.cadastro import *
from time import sleep

arquivo = 'Pessoas.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar uma nova pessoa', 'Sair do sitema'])
    if resposta == 1:
        lerArquivo(arquivo)
    elif resposta == 2:
        cabeçalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arquivo, nome, idade)
    elif resposta == 3:
        linha()
        cabeçalho('Saindo do Sistema.. Até logo')
        break
    else:
        print('ERRO X__X Digite uma resposta correta')
    sleep(3.5)

