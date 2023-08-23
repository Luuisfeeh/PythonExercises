from ex113 import leiaInt
def linha(tam = 42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(f'{txt.center(42)}')
    print(linha())


def menu(lista):
    cabeçalho('Menu Principal')
    for c,a in enumerate(lista):
        print(f'{c+1} - {a}')
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc