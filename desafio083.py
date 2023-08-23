lista = list()
expr = str(input('Escreva uma expressão numérica: '))
for símb in expr:
    if símb == '(':
        lista.append('(')
    elif símb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')
