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


def moeda(val=0, moeda='R$'):
    return f'{moeda}{val:>8.2f}'.replace('.', ',')