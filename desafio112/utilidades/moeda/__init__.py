def aumentar(val=0, taxa=0, formato=False):
    v = val
    v = (taxa/100 * v) + v

    return v if formato is False else moeda(v)


def diminuir(val=0 , taxa=0 , formato=False):
    v = val
    v = v - (taxa/100 * v)
    return v if formato is False else moeda(v)


def metade(val=0, formato=False):
    v = val
    v = v/2
    return v if not formato else moeda(v)



def dobro(val=0, formato=False):
    v = val
    v = v*2
    return v if formato is False else moeda(v)


def moeda(val=0, formt='R$'):
    return f'{formt}{val:>.2f}'.replace('.', ',')


def resumo(val=0, aum=10, dim=5):
    print('-+-' * 12)
    print('          RESUMO DO VALOR ')
    print('-+-' * 12)
    print(f'Preço analisado:{moeda(val):>18}')
    print(f'Dobro do Preço:{dobro(val, True):>18}')
    print(f'Metade do preço:{metade(val,True):>18}')
    print(f'{aum}% de aumento: {aumentar(val,aum,True):>18}')
    print(f'{dim}% de redução: {diminuir(val,dim,True):>18}')
    print('-+-' * 12)