while True:
    n = int(input('Quer ver a tabuado de qual valor? '))
    print('-~-' * 10)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} X {c:2} = {n * c:2}')
    print('-~-' * 10)


print('Programa TABUADO ENCERRADO. Volte sempre!')