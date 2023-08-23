def cadastrar(arq, nome='desconhecido', idade='?'):
    try:
        a = open(arq, 'at')
    except:
        print('HOuve um Error na abertura')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('HOuve um erro para escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado!!')
            a.close()