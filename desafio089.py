lista = list()

while True:
    nome = str(input('Digite seu nome: ')).strip()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1+n2)/2
    lista.append([nome,[n1,n2],media])

    resp = str(input('Deseja continuar? [S/N]')).strip().upper()
    if resp == 'N':
        break
print('-+-'*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8} ')
print('_'*22)
for n,i in enumerate(lista):
    print(f'{n:<4}{i[0]:<10}{i[2]:>8.1f}')

while True:
    print('_'*30)
    resp = int(input('Mostrar notas de qual aluno? (999 interrompe):'))
    if resp == 999:
        print('Finalizando..')
        break
    if resp <= len(lista) - 1:
        print(f'O aluno {lista[resp][0]} teve a média {lista[resp][2]}.')